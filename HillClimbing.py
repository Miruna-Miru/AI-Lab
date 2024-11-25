nodes = {}
heuristic = {}

def add_edge(from_node, to_node, weight=1):
    if from_node not in nodes:
        nodes[from_node] = {}
    if to_node not in nodes:
        nodes[to_node] = {}
    nodes[from_node][to_node] = weight

def set_heuristic(node, value):
    heuristic[node] = value

def hill_climbing(start, goal):
    current_node = start
    path = [start]

    while current_node != goal:
        print(f"Current Node: {current_node}")

        if current_node not in nodes or len(nodes[current_node]) == 0:
            print("No more nodes to visit. Stuck at a local maximum.")
            return path

        neighbors = nodes[current_node]
        next_node = None
        next_heuristic = float('inf')

        for neighbor in neighbors:
            if heuristic[neighbor] < next_heuristic:
                next_node = neighbor
                next_heuristic = heuristic[neighbor]

        if next_heuristic >= heuristic[current_node]:
            print("No better neighbors found. Reached a local maximum.")
            return path

        current_node = next_node
        path.append(current_node)

    print(f"Goal Node {goal} reached.")
    return path

# Example usage
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('A', 'D')
add_edge('C', 'Z')
add_edge('C', 'E')

# Set heuristic values for each node
set_heuristic('A', 2)
set_heuristic('B', 5)
set_heuristic('C', 3)
set_heuristic('D', 4)
set_heuristic('E', 2)
set_heuristic('Z', 1)

# Perform hill climbing
start_node = input("Enter start node : ")
goal_node = input("Enter goal node : ")
path,val = hill_climbing(start_node, goal_node)
print(f"Path from {start_node} to {goal_node}: {path}")
