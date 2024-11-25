from collections import deque
import math
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


def bfs(graph,start,goal=None):
    visited=set()
    queue=deque([(start,[start],0)])
    order_of_visit=[]
  

    while queue:
        current,path,cost=queue.popleft()
        if current not in visited:
            visited.add(current)
            order_of_visit.append(current)
            for node , weight in graph[current].items():
                if node==goal:
                    return path+[node],cost+weight , order_of_visit
                queue.append((node,path+[node],cost+weight))
    return None,math.inf,order_of_visit

def dfs(graph,start,goal=None):
    visited=set()
    stack=[(start,[start],0)]
    order_of_visi=[]

    while stack:
        current,path,cost=stack.pop()
        if current not in visited:
            visited.add(current)
            order_of_visi.append(current)

            for node,weight in graph[current].items():
                if node==goal:
                    return path+[node],cost+weight,order_of_visi
                stack.append((node,path+[node],cost+weight))
    return None,math.inf,order_of_visi


start=input("Enter start :  ")
goal =input("Enter goal  :  ")

bp,bc,bo=bfs(graph,start,goal)
dp,dc,do=dfs(graph,start,goal)
print("BFS : \n")
print(bp)
print(bo)
print("DFS")
print(dp)
print(do)
if bc>dc:
    print("DFS is good :  ",dc)
    print("BFS : ",bc)
else:
      print("BFS is good :  ",bc)
      print("DFS : ",dc)

