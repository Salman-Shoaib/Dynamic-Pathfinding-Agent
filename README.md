# Dynamic Pathfinding Agent

## Overview

This project implements a **Dynamic Pathfinding Agent** capable of navigating a grid-based environment using **informed search algorithms**.
The agent can compute paths from a **Start node** to a **Goal node** while avoiding obstacles. In **Dynamic Mode**, obstacles may appear randomly while the agent is moving, forcing the agent to **detect blocked paths and re-plan a new route in real time**.

The project includes a **Graphical User Interface (GUI)** built with **Pygame** that visualizes the search process and displays performance metrics.

---

## Features

### 1. Grid-Based Environment

* User-defined **grid size (Rows × Columns)**.
* Fixed **Start node** and **Goal node**.
* **Random maze generation** with adjustable obstacle density.
* **Interactive map editor**:

  * Click cells to add or remove obstacles.
* No static map files – the environment is generated dynamically.

---

### 2. Implemented Algorithms

#### Greedy Best-First Search (GBFS)

Uses only the heuristic function:

f(n) = h(n)

The algorithm always expands the node that appears closest to the goal.

#### A* Search

Uses both path cost and heuristic:

f(n) = g(n) + h(n)

Where:

* **g(n)** = cost from start to node
* **h(n)** = estimated cost to goal

A* generally finds the **optimal path**.

---

### 3. Heuristic Functions

#### Manhattan Distance

Used for grid movement in four directions.

D = |x1 − x2| + |y1 − y2|

#### Euclidean Distance

Straight-line distance between nodes.

D = √((x1 − x2)² + (y1 − y2)²)

Users can switch heuristics before starting the search.

---

### 4. Dynamic Obstacles

To simulate real-world navigation:

* New obstacles can spawn randomly during agent movement.
* If an obstacle blocks the current path:

  * The agent **detects the blockage**
  * A **new path is calculated from the current position**

This demonstrates **real-time re-planning**.

---

## Visualization

The GUI highlights different node states:

| Color      | Meaning        |
| ---------- | -------------- |
| Orange     | Start Node     |
| Purple     | Goal Node      |
| Black      | Obstacles      |
| Yellow     | Frontier Nodes |
| Blue / Red | Visited Nodes  |
| Green      | Final Path     |

---

## Performance Metrics

The system displays real-time statistics:

* **Nodes Visited** – number of expanded nodes
* **Path Cost** – length of the final path
* **Execution Time** – time taken to compute the solution (ms)

---

## Installation

Make sure Python is installed, then install the required library:

```
pip install pygame
```

---

## How to Run

Run the program using Python:

```
python pathfinding.py
```

You will be asked to enter:

```
Rows
Columns
```

Example:

```
Enter number of rows: 20
Enter number of columns: 20
```

---

## Controls

| Key / Action | Function                        |
| ------------ | ------------------------------- |
| Mouse Click  | Add / Remove obstacle           |
| R            | Generate random map             |
| 1            | Select Greedy Best First Search |
| 2            | Select A* Search                |
| M            | Use Manhattan heuristic         |
| E            | Use Euclidean heuristic         |
| D            | Toggle dynamic obstacles        |
| SPACE        | Start pathfinding               |

---

## Example Workflow

1. Run the program.
2. Enter grid size.
3. Press **R** to generate a random map.
4. Select algorithm (**1** or **2**).
5. Choose heuristic (**M** or **E**).
6. Press **SPACE** to start the search.

---

## Advantages of Algorithms

### Greedy Best-First Search

**Pros**

* Fast exploration
* Simple implementation

**Cons**

* Does not guarantee optimal path
* Can be misled by heuristic

### A* Search

**Pros**

* Finds optimal path
* Efficient combination of cost and heuristic

**Cons**

* Requires more memory
* Slightly slower than GBFS

---

## Applications

This project demonstrates concepts used in:

* Robotics navigation
* Autonomous vehicles
* Game AI
* Route planning systems
* Real-time pathfinding

---

## Technologies Used

* Python
* Pygame
* Priority Queue
* Heuristic Search Algorithms

---

## Author

**Salman Shoaib**
Computer Science Student
