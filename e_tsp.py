import heapq
import math

def tsp(graph):
    min_cost=math.inf
    best_path=[]
    pq=[(0,0,0,[0])]
    num_cities=len(graph)

    while pq:
        estimated,curr_cost,cur_city,path=heapq.heappop(pq)
        
        if(len(path)==num_cities+1 and path[-1]==0):
            if curr_cost<min_cost:
                min_cost=curr_cost
                best_path=path
            continue

        for nxt in range(num_cities):
            if nxt not in path or(len(path)==num_cities and nxt==0):
                nw_cost=curr_cost+graph[cur_city][nxt]
                if nw_cost<min_cost:
                    heapq.heappush(pq,(nw_cost,nw_cost,nxt,path+[nxt]))

    return best_path,min_cost
        

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP
path, cost = tsp(graph)
print("Shortest path:", path)
print("Minimum cost:", cost)