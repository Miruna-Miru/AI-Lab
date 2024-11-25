import heapq

def tsp_best_first_search(graph):
    num_cities = len(graph)
    min_cost = float('inf')
    best_path = []

    # Priority queue: (estimated_cost, current_cost, current_city, path)
    pq = [(0, 0, 0, [0])]

    while pq:
        estimated_cost, current_cost, current_city, path = heapq.heappop(pq)

        # If all cities are visited and we're back at the start
        if len(path) == num_cities + 1 and path[-1] == 0:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        # Expand the current city
        for next_city in range(num_cities):
            if next_city not in path or (len(path) == num_cities and next_city == 0):
                new_cost = current_cost + graph[current_city][next_city]
                if new_cost < min_cost:  # Prune paths with higher cost
                    heapq.heappush(pq, (new_cost, new_cost, next_city, path + [next_city]))

    return best_path, min_cost


# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP
path, cost = tsp_best_first_search(graph)
print("Shortest path:", path)
print("Minimum cost:", cost)
