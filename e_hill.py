import math

nodes={}
heuristic={}

def add_edge(fro,to,w=1):
    if fro not in nodes:
        nodes[fro]={}
    if to not in nodes:
        nodes[to]={}
    nodes[fro][to]=w

def set_heuristic(node,h):
    heuristic[node]=h

def hill(start,goal,restr):
    current=start
    path=[start]
    while current!=goal:
        if current not in nodes or len(nodes[current])==0:
            print("Stuck at local maxima No more node to visit")
            print(*path)
            return None
        
        next_n=None
        ne_heurisitc=math.inf
        for neigbhor in nodes[current] :
            if neigbhor not in restr:
                if ne_heurisitc>heuristic[neigbhor]:
                    next_n=neigbhor
                    ne_heurisitc=heuristic[neigbhor]
                    
            
        if ne_heurisitc>heuristic[current]:
                print("Reached local maximum No more optimal sol found")
                print(*path)
                return None
        current=next_n
        path.append(current)
    
    print("Goal node reached : ")
    return path
# Example usage
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('A', 'D')
add_edge('C', 'Z')
add_edge('C', 'E')

restr=["B","D"]

# Set heuristic values for each node
set_heuristic('A', 2)
set_heuristic('B', 5)
set_heuristic('C', 3)
set_heuristic('D', 4)
set_heuristic('E', 2)
set_heuristic('Z', 1)

start=input("Enter start node :   ")
goal=input("Enter Goal node     :   ")

res=hill(start,goal,restr)
if res:
    print(res)
