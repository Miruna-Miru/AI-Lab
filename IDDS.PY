def depth_limited_search(node, goal, depth, graph):
   
    if depth == 0:
        print(node,end="--> ")
        if node == goal:
            return [node]
        return None
    
    if depth > 0:
        for neighbor in graph.get(node, []):
            result = depth_limited_search(neighbor, goal, depth - 1, graph)
            if result is not None:
                return [node] + result
    return None

def iterative_deepening_search(start, goal, graph):
    
    depth = 0
    while True:
        print(f"\nSearching with depth limit: {depth}\n")
        result = depth_limited_search(start, goal, depth, graph)
        if result is not None:
            return result
        depth += 1

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

# Test the IDS algorithm
start_node = 'A'
goal_node = 'I'
path = iterative_deepening_search(start_node, goal_node, graph)
if path:
    print(f"Path found: {path}")
else:
    print("Goal not found.")
