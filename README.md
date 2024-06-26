# Path Planning Algorithms for Obstacle Avoidance

This repository contains implementations of various motion planning algorithms for obstacle avoidance, developed as part of the Modern Robotics, Course 4: Robot Motion Planning and Control. The algorithms included are the A* Algorithm, Probabilistic Roadmap (PRM), and Rapidly-exploring Random Tree (RRT). These algorithms, fundamental in robotics for navigating environments while avoiding obstacles, are implemented in CoppeliaSim.

## Directory Structure

```
Path_planning/
│
├── Astar_algorithm/
│   ├── code_.py
│   ├── results/
│   └── screenshot.png
│
├── PRM/
│   ├── PRM_code.py
│   ├── results/
│   │   ├── edges.csv
│   │   ├── nodes.csv
│   │   ├── obstacles.csv
│   │   └── path.csv
│   └── screenshot.png
│
└── RRT_algorithm/
    ├── code.py
    ├── pseudo.txt
    ├── results/
    │   ├── edges.csv
    │   ├── nodes.csv
    │   ├── obstacles.csv
    │   └── path.csv
    └── Screenshot.JPG
```

## Algorithms

### A* Algorithm


The A* algorithm is a widely-used and highly efficient pathfinding algorithm that excels in navigating graphs from a start node to a goal node. It combines the strengths of both Dijkstra's algorithm and a heuristic approach to achieve optimal and speedy results. By employing a heuristic function, A* estimates the cost of the cheapest path from the current node to the goal, allowing it to prioritize paths that are more likely to lead to the goal quickly.

#### Implementation
- `Astar_algorithm/code_.py`: This script contains the implementation of the A* algorithm.
- `Astar_algorithm/results/`: This directory stores the results of the A* algorithm execution.
- `Astar_algorithm/screenshot.png`: A screenshot showing the results of the A* algorithm.

![A* Algorithm Results](Astar_algorithm/screenshot.png)

### Probabilistic Roadmap (PRM)

The Probabilistic Roadmap (PRM) algorithm is used for robot path planning in high-dimensional configuration spaces. It constructs a roadmap of possible paths through randomly sampled points in the space and connects these points using simple paths. PRM is effective for planning in environments with numerous obstacles, leveraging randomness to explore the space efficiently.


#### Implementation
- `PRM/PRM_code.py`: This script contains the implementation of the PRM algorithm.
- `PRM/results/`: This directory includes:
  - `edges.csv`: The edges of the roadmap.
  - `nodes.csv`: The nodes of the roadmap.
  - `obstacles.csv`: The obstacles in the environment.
  - `path.csv`: The computed path from the start to the goal.
- `PRM/screenshot.png`: A screenshot showing the results of the PRM algorithm.


### Rapidly-exploring Random Tree (RRT)

The Rapidly-exploring Random Tree (RRT) algorithm is a highly efficient path planning method designed for high-dimensional spaces, often used in robotics and autonomous systems. RRT excels in finding feasible paths in complex environments by incrementally building a tree that explores the space rapidly and thoroughly. RRT operates by randomly sampling points in the configuration space and extending the tree from the nearest node towards each sampled point. This incremental process ensures that the tree quickly covers large areas of the space, effectively exploring potential paths while avoiding obstacles.

#### Implementation
- `RRT_algorithm/code.py`: This script contains the implementation of the RRT algorithm.
- `RRT_algorithm/pseudo.txt`: A pseudocode description of the RRT algorithm.
- `RRT_algorithm/results/`: This directory includes:
  - `edges.csv`: The edges of the RRT.
  - `nodes.csv`: The nodes of the RRT.
  - `obstacles.csv`: The obstacles in the environment.
  - `path.csv`: The computed path from the start to the goal.
- `RRT_algorithm/Screenshot.JPG`: A screenshot showing the results of the RRT algorithm.


![RRT Algorithm Results](RRT_algorithm/Screenshot.JPG)


## Results

The results of each algorithm are stored in their respective `results` directories. You can visualize the output using the provided screenshots.

## Educational Value

These implementations demonstrate key concepts in robot motion planning and control, including heuristic-based search, probabilistic sampling, and tree-based path planning. Understanding these algorithms is essential for developing autonomous navigation systems in robotics.

## Contributing

Contributions are welcome! 

