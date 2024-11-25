import heapq

def astar_search(graph, start, goal, heuristic):
    
    pq = []
    heapq.heappush(pq, (0 + heuristic[start], start))  # (f_value, node)
     
    g = {start: 0}
    parent = {start: None}
   
    while pq:       
        current_cost, current_node = heapq.heappop(pq)
       
       
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path
       
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
           
            new_cost = g[current_node] + weight
            
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f_value = new_cost + heuristic[neighbor] 
                heapq.heappush(pq, (f_value, neighbor))
                parent[neighbor] = current_node
   
    # If goal node is not found
    return None

# Example usage
graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D':3,'G': 4},
    'D':{'G':0},
    'G': {}
}

heuristic = {
    'S': 5,  
    'A': 3,
    'B': 4,
    'C': 2,
    'D':6,
    'G': 0
}

start = 'S'
goal = 'G'

path = astar_search(graph, start, goal, heuristic)
if path:
    print(f"Shortest path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}")
