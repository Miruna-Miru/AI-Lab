











'''
SOURCE CODE : //Minimax without using alpha beta pruning
class TreeNode:
 def __init__(self, label=None):
 self.label = label
 self.children = []
def build_tree_from_input():
 print("Enter the tree nodes in a parent-children format (use '.' for no children):")
 root_label = input("Enter label for root node: ")
 root = TreeNode(root_label)
 queue = [root]
 
 while queue:
 current_node = queue.pop(0)
 
 children_input = input(f"Enter children for {current_node.label} (comma-separated 
labels or '.' if no children): ").strip()
 
 if children_input == '.':
 continue
 
 child_labels = list(map(str.strip, children_input.split(',')))
 for label in child_labels:
 if label == '.':
 continue
 new_child = TreeNode(label)
 current_node.children.append(new_child)
 queue.append(new_child)
 
 return root
def minimax(node, maximizingPlayer):
 if not node.children:
 return int(node.label) # Convert the label to an integer if necessary
 
 if maximizingPlayer:
 best = float('-inf')
 for child in node.children:
 val = minimax(child, False)
 best = max(best, val)
 return best
 else:
 best = float('inf')
 for child in node.children:
 val = minimax(child, True)
 best = min(best, val)
 return best
# Example usage:
if __name__ == "__main__":
 # Build the tree dynamically from user input
 root = build_tree_from_input()
 
 if root is None:
 print("Empty tree!")
 else:
 # Perform basic minimax
 optimalValue = minimax(root, True)
 print("The optimal value is:", optimalValue)
'''

'''
def build_tree_from_input():
   
    root_label = input("Enter label for root node: ")
    root = (root_label, [])
    queue = [root]
    print("Enter  nodes  (parent-children) . --> No childern")
    
    while queue:
        current_label, children = queue.pop(0)
        
        children_input = input(f"Enter children for {current_label} : ").strip()
        
        if children_input == '.':
            continue
        
        child_labels = list(map(str.strip, children_input.split(',')))
        for label in child_labels:
            if label == '.':
                continue
            new_child = (label, [])
            children.append(new_child)
            queue.append(new_child)
    
    return root

def minimax_ab(node, maximizingPlayer, alpha, beta):
    label, children = node
    
    if not children:
        return int(label)
    
    if maximizingPlayer:
        best = float('-inf')
        for child in children:
            val = minimax_ab(child, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in children:
            val = minimax_ab(child, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Build the tree dynamically from user input
root = build_tree_from_input()

if root is None:
    print("Empty tree!")
else:
    # Perform minimax with alpha-beta pruning
    optimalValue = minimax_ab(root, True, float('-inf'), float('inf'))
    print("The optimal value is:", optimalValue)

    
'''