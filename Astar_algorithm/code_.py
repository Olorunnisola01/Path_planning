import csv
import copy
from queue import PriorityQueue


# Read edge information
# Represent edges as an adjacent list
adj_list = {}
with open("results/edges.csv", "r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if line[0].startswith("#"):
            continue
        x, y, d = line
        x, y = int(x), int(y)
        if x not in adj_list:
            adj_list[x] = set()
        adj_list[x].add(y)
        if y not in adj_list:
            adj_list[y] = set()
        adj_list[y].add(x)

# Read node information
# Represent heurisitic costs as a dictionary
cost_to_go = {}
with open("results/nodes.csv", "r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if line[0].startswith("#"):
            continue
        i, x, y, h = line
        cost_to_go[int(i)] = h

# A* algorithm based on priority queue
priority_queue = PriorityQueue()
priority_queue.put((cost_to_go[1], [1]))
goal_state = 12
visited  = set()
while not priority_queue.empty():
    cur_cost, cur_path = priority_queue.get()
    visited.add(tuple(cur_path))
    if cur_path[-1] == goal_state:
        with open("results/path.csv", "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(cur_path)
            break
    else:
        for next_node in adj_list[cur_path[-1]]:
            next_cost = cost_to_go[next_node]
            next_path = copy.deepcopy(cur_path) + [next_node]
            if tuple(next_path) not in visited:
                priority_queue.put((next_cost, next_path))

        


    


    

