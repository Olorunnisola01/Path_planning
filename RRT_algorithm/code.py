import os
import numpy as np
import pandas as pd


def get_linear_equation(point1, point2):
    
    # estimate coeffs of line equation
    # y = a*x + b
    
    if (np.abs(point2[0]-point1[0])!=0):
        a = (point2[1]-point1[1])/(point2[0]-point1[0])
        b = point1[1] - a*point1[0]
        return (a,b)
    else:
        return (point2[1]-point1[1])

def get_det(linear_coeffs, circle_coeffs):
    
    # estimate discriminant quadratic equation
    # if discriminant < 0 no intersection between line and circle
    
    h, k, r = circle_coeffs
    if len(linear_coeffs)>1:
        a,b = linear_coeffs
        det = (a*b-a*k-h)**2 - (1+a**2)*(h**2+b**2+k**2-2*b*k-r**2)
    else:
        x_const = linear_coeffs
        det = r**2 - ( x_const-h)**2
    return det

def euclid_dist(point1, point2):
    
    # estimate euclidian distance between two points
    
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)

def check_intersection(point1, point2, obstacles):
    
    # func, check does intersection of streight line (between 2 points) and circle exist
    
    # get coeffs of line based on 2 points
    lin_coeffs = get_linear_equation(point1, point2)
    
    # the 3 methods to check is intersection observed:
    for obs in obstacles:
        #print(obs)
        # method 1: check is 2nd point intersects with obstacle
        if (euclid_dist(point2, (obs[0], obs[1]))<= obs[2]/2):
            return 1
        # method 2: check intersection of infinite line with circle of obstacle
        cir_coeffs = [obs[0], obs[1], obs[2]/2]
        dis = get_det(lin_coeffs, cir_coeffs)
        #print(dis)
        if dis<0:
            # discriminant < 0 => no intersection
            continue
        else:
            # method 3: sample predifined number of points from the streight line 
            for tmp_point in zip(np.linspace(point1[0],point2[0], LINE_SMPL+2)[1:-1],
                                 np.linspace(point1[1],point2[1], LINE_SMPL+2)[1:-1]):
                # check does these points in intersects with obstacles
                #print('euclid:', (euclid_dist(tmp_point, (obs[0], obs[1]))))
                if (euclid_dist(tmp_point, (obs[0], obs[1])) <= obs[2]/2):
                    return 1
                
    return 0

def return_path(parent_dict, start_node, goal_node):
    # function, which return target path from parent dictionary
    path = []
    prev_node = goal_node
    while True:
        path.append(prev_node)
        if tuple(prev_node)==tuple(start_node):
            return path[::-1]
        prev_node = parent_dict[tuple(prev_node.astype(np.float32))]
    print ('This is the path you are looking for: ', path)


# setup params required for algorithm
LINE_SMPL = 10
NUM_SAMPLING = 10
SEARCH_RAD = 0.4
MAX_ITER = 100000

# read obstacles from disk
obstacles = np.array(pd.read_csv('results/obstacles.csv', header=None))

# setup start and goal nodes coords
start = (-0.5, -0.5)
goal = (0.5,0.5)


# status variable, will be 1 if solution if dfound
solve_status = 0

parent = {}
queue_points = []
queue_points.append([start])

# main loop
for j in range(MAX_ITER):
    if solve_status:
            break
    for curr_point in queue_points.pop(0):
        if solve_status:
            break
        new_points = np.copy([np.random.uniform(np.max([-0.5, curr_point[0]-SEARCH_RAD]), np.min([0.5, curr_point[1]+SEARCH_RAD]), size=2) for i in range(NUM_SAMPLING)])
        good_points = np.copy([i for i in new_points if check_intersection(curr_point, i, obstacles)==0])
        
        queue_points.append(good_points)
        
        for good_coord in good_points:
            if solve_status:
                continue
            parent[tuple(good_coord.astype(np.float32))] = curr_point
            if euclid_dist(good_coord, goal) < 0.02:
                print('Solution found!', good_coord)
                print('Number of explored nodes=',len(list(parent.keys())))
                solve_status = 1
                solution = np.copy(good_coord)
                break

if solve_status:
    # extract solution from all nodes
    solution_path_np = np.array(return_path(parent, start, solution))

    # save results to disk
    pd.DataFrame(solution_path_np,index=list(range(1, len(solution_path_np)+1))).to_csv("results/nodes.csv", header=None)
    pd.DataFrame([[i,i+1,euclid_dist(solution_path_np[i-1], solution_path_np[i])] for i in (range(1,len(solution_path_np)))]).to_csv("results/edges.csv", index=None, header=None)
    pd.DataFrame([i for i in (range(1,len(solution_path_np)+1))]).T.to_csv("results/path.csv", index=None, header=None)