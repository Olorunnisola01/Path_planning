import random

obstacles_list = []
with open('results/obstacles.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        splited = line.split(',')
        obstacles_list.append((float(splited[0]), float(splited[1]), float(splited[2][:-1])/2))

def ComputeLine(x1, y1, x2, y2):
    # return (a, b, c) s.t. ax + by + c = 0
    delta_y, delta_x = y2 - y1, x2 - x1
    if delta_x == 0: return (1, 0, -x1)
    elif delta_y == 0: return (0, 1, -y1)
    else:
        m = delta_y / delta_x
        c = y1 - m * x1
        return (-m, 1, -c)

def DistFromPtToLine(line, x, y):
    return abs(line[0]*x + line[1]* y + line[2]) / ((line[0])**2 + (line[1])**2)**0.5

def CollisionCheck(obstacles, line):
    for oX, oY, oR in obstacles:
        if DistFromPtToLine(line, oX, oY) < oR: return True
    return False

def EuclidDist(x1, y1, x2, y2): return ((x1-x2)**2 + (y1-y2)**2)**0.5

def kClosestPts(pt, points, k):
    dists = []
    for point in points:
        dists.append((EuclidDist(pt[1], pt[2], point[1], point[2]), point))
    dists.sort()
    return [dist[1] for dist in dists[1:k+2]]

def PRM(obstacles, k, n):
    points = [(1,-0.5,-0.5),]
    points += [(i+2,random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)) for i in range(n-2)]
    points.append((n,0.5,0.5))
    edges = []
    heuristic_ctg = [EuclidDist(0.5,0.5,point[1],point[2]) for point in points]
    graph = [[] for _ in range(n)]
    for point in points:
        nbrs = kClosestPts(point, points, k)
        assert point not in nbrs
        for nbr in nbrs:
            dist = EuclidDist(point[1],point[2],nbr[1],nbr[2])
            if (nbr[0], dist) in graph[point[0]-1] or \
               CollisionCheck(obstacles, ComputeLine(nbr[1],nbr[2],point[1],point[2])): continue
            graph[point[0]-1].append((nbr[0], dist))
            graph[nbr[0]-1].append((point[0], dist))
            edges.append((nbr[0], point[0], dist))
    return (graph, heuristic_ctg, points, edges)

def AStarSearch(num_nodes, heuristic_ctg, graph):
    past_costs = [1e10 for _ in range(num_nodes)]
    past_costs[0] = 0
    parents = [-1 for _ in range(num_nodes)]
    est_total_cost = [1e10 for _ in range(num_nodes)]
    est_total_cost[0] = heuristic_ctg[0]
    open_list = {(est_total_cost[0], 1)}
    closed_list = set()
    while len(open_list) != 0:
        curr = open_list.pop()[1]
        closed_list.add(curr)
        if curr == num_nodes:
            path = [curr, ]
            p = parents[curr-1]
            while p != -1:
                path.append(p)
                p = parents[p-1]
            path.reverse()
            return True, path
        for nbr in graph[curr-1]:
            if nbr[0] in closed_list: continue
            tentative_past_cost = past_costs[curr-1] + nbr[1]
            if tentative_past_cost < past_costs[nbr[0]-1]:
                past_costs[nbr[0]-1] = tentative_past_cost
                parents[nbr[0]-1] = curr
                try:
                    open_list.remove((est_total_cost[nbr[0]-1], nbr[0]))
                    est_total_cost[nbr[0]-1] = past_costs[nbr[0]-1] + heuristic_ctg[nbr[0]-1]
                    open_list.add((est_total_cost[nbr[0]-1], nbr[0]))
                except:
                    est_total_cost[nbr[0]-1] = past_costs[nbr[0]-1] + heuristic_ctg[nbr[0]-1]
                    open_list.add((est_total_cost[nbr[0]-1], nbr[0]))
    return (False, [1,])

graph, heuristic_ctg, nodes, edges = PRM(obstacles_list, 10, 100)
num_nodes = len(graph)

success, path = AStarSearch(num_nodes, heuristic_ctg, graph)
print(success)

with open('results/path.csv', 'w') as f:
    if not success:
        f.write('1')
    else:
        for i, node in enumerate(path):
            if i == 0:
                f.write(str(node))
            else:
                f.write(', '+str(node))

with open('results/nodes.csv', 'w') as f:
    for node in nodes:
        f.write(f"{node[0]},{node[1]},{node[2]}\n")

with open('results/edges.csv', 'w') as f:
    for edge in edges:
        f.write(f"{edge[0]}, {edge[1]}, {edge[2]}\n")