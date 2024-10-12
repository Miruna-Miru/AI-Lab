import heapq

def ucs(graph, start, goal):
    # Priority queue to explore nodes based on cost
    queue = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)

        if node == goal:
            return path, cost  # Return path and total cost

        # Explore neighbors
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return None, float('inf')  # If goal is unreachable

# Graph represented as adjacency list with edge weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Example usage
start = 'A'
goal = 'F'
path, total_cost = ucs(graph, start, goal)

if path:
    print(f"Path: {path}, Total Cost: {total_cost}")
else:
    print("No path found")
