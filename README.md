# Mini-Courier Planner

## Project Overview

Mini-Courier Planner is a Python-based courier planning system.

It performs:
- Parcel prioritization using sorting
- Optimal parcel selection using Dynamic Programming
- Shortest path calculation using Dijkstra's Algorithm
- Delivery route planning using Nearest Neighbor TSP

## Project Structure

Mini-Courier-Planner/
- src/
- datasets/
- images/
- README.md
- requirements.txt
- .gitignore

## Dataset

The project uses:
- parcels.csv for parcel information
- routes.csv for delivery route information

## Algorithms Used

1. Sorting
2. 0/1 Knapsack using Dynamic Programming
3. Dijkstra's Shortest Path
4. Nearest Neighbor TSP Approximation

## How to Run

Open the project in VS Code.

Run:

python src/courier_planner.py

## Output

The program displays:
- Parcel priority list
- Optimal packing plan
- Shortest paths
- Delivery route
- Runtime performance

## Future Scope

The system can be improved by using larger datasets, better route optimization and a graphical user interface.