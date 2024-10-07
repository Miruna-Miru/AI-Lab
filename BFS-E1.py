from collections import deque

# Define the graph
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def bfs_explore(graph, start, goal=None):
    visited = set()
    queue = deque([(start, [start])]) 
    order_of_visit = []

    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order_of_visit.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    
    return order_of_visit if goal is None else None

start_node = input("Enter the start node: ").strip()

if start_node not in graph:
    print(f"Error: '{start_node}' is not a valid node in the graph.")
else:
    goal_node = input("Enter the goal node (or press Enter to explore the whole graph): ").strip()
    
    if goal_node:
        path = bfs_explore(graph, start_node, goal_node)
        if path:
            print(f"Path from {start_node} to {goal_node}: {path}")
        else:
            print(f"No path found from {start_node} to {goal_node}.")
    else:
        exploration_order = bfs_explore(graph, start_node)
        print(f"Order of nodes visited starting from {start_node}: {exploration_order}")
