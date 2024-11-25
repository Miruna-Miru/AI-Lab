import heapq

def astar_search(graph, start, goal, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))

    g_v = {start: 0}  # Initialize g_v before the loop
    parent = {start: None}  # Initialize parent before the loop

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return the path in reverse order

        for nxt, we in graph[current].items():
            n_g = g_v[current] + we
            if nxt not in g_v or n_g < g_v[nxt]:
                g_v[nxt] = n_g
                f = n_g + heuristic[nxt]
                heapq.heappush(pq, (f, nxt))
                parent[nxt] = current

    return None

# Example usage
graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 0},
    'G': {}
}

heuristic = {
    'S': 5,  
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

start = 'S'
goal = 'G'

path = astar_search(graph, start, goal, heuristic)
if path:
    print(f"Shortest path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}")
