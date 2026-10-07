import csv

# Load parcel data
def load_parcels(filename):
    parcels = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["weight"] = int(row["weight"])
            row["value"] = int(row["value"])
            row["deadline"] = int(row["deadline"])
            row["priority"] = int(row["priority"])
            parcels.append(row)

    return parcels


# Sort parcels by priority
def sort_parcels(parcels):
    return sorted(parcels, key=lambda x: x["priority"], reverse=True)


# Main program
parcels = load_parcels("datasets/parcels.csv")

sorted_parcels = sort_parcels(parcels)

print("=== Parcel Priority List ===")

for parcel in sorted_parcels:
    print(
        parcel["parcel_id"],
        "Weight:", parcel["weight"],
        "Value:", parcel["value"],
        "Deadline:", parcel["deadline"],
        "Priority:", parcel["priority"]
    )
    # Dynamic Programming - 0/1 Knapsack
def knapsack(parcels, capacity):
    n = len(parcels)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(1, capacity + 1):

            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - weight]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    return selected, dp[n][capacity]


# Select parcels for one delivery trip
capacity = 15

selected_parcels, maximum_value = knapsack(parcels, capacity)

print("\n=== Optimal Packing Plan ===")
print("Van Capacity:", capacity, "kg")

for parcel in selected_parcels:
    print(
        parcel["parcel_id"],
        "Weight:", parcel["weight"],
        "Value:", parcel["value"]
    )

print("Maximum Value:", maximum_value)
# Dijkstra's Shortest Path Algorithm
import heapq


def load_routes(filename):
    graph = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            source = row["source"]
            destination = row["destination"]
            distance = int(row["distance"])

            if source not in graph:
                graph[source] = []

            if destination not in graph:
                graph[destination] = []

            graph[source].append((destination, distance))
            graph[destination].append((source, distance))

    return graph


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


# Load route graph
graph = load_routes("datasets/routes.csv")

# Find shortest paths from Warehouse
shortest_paths = dijkstra(graph, "Warehouse")

print("\n=== Shortest Paths from Warehouse ===")

for location, distance in shortest_paths.items():
    print(location, ":", distance)
    # Nearest Neighbor TSP Approximation
def nearest_neighbor_route(graph, start):
    route = [start]
    unvisited = set(graph.keys())
    unvisited.remove(start)

    current = start
    total_distance = 0

    while unvisited:

        nearest = None
        shortest_distance = float("inf")

        for neighbor, distance in graph[current]:

            if neighbor in unvisited and distance < shortest_distance:
                nearest = neighbor
                shortest_distance = distance

        if nearest is None:
            break

        route.append(nearest)
        total_distance += shortest_distance

        unvisited.remove(nearest)
        current = nearest

    # Return to warehouse
    for neighbor, distance in graph[current]:
        if neighbor == start:
            total_distance += distance
            route.append(start)
            break

    return route, total_distance


# Create delivery route
delivery_route, route_distance = nearest_neighbor_route(
    graph, "Warehouse"
)

print("\n=== Delivery Route ===")
print(" -> ".join(delivery_route))
print("Total Route Distance:", route_distance)
# Runtime Testing
import time

start_time = time.perf_counter()

load_parcels("datasets/parcels.csv")
load_routes("datasets/routes.csv")

end_time = time.perf_counter()

runtime = end_time - start_time

print("\n=== Runtime Performance ===")
print("Data Loading Runtime:", runtime, "seconds")