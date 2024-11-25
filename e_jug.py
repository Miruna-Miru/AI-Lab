import heapq

def is_valid(state, capacities):
    return 0 <= state[0] <= capacities[0] and 0 <= state[1] <= capacities[1]

def is_goal(state, target):
    return state[0] == target or state[1] == target

def get_h(state, target):
    return min(abs(state[0] - target), abs(state[1] - target))

def water(j1, j2, target):
    capacities = (j1, j2)
    open_list = []
    closed_list = set()
    start = (0, 0)

    if is_goal(start, target):
        return [start]
    
    heapq.heappush(open_list, (0, start))
    parent = {start: None}
    g_v = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current in closed_list:
            continue
        closed_list.add(current)
        if is_goal(current, target):
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        jug1, jug2 = current
        succ = [
            (j1, jug2),
            (jug1, j2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, j2 - jug2), jug2 + min(jug1, j2 - jug2)),
            (jug1 + min(jug2, j1 - jug1), jug2 - min(jug2, j1 - jug1))
        ]

        for nxt in succ:
            if not is_valid(nxt, capacities) or nxt in closed_list:
                continue

            g_n = g_v[current] + 1
            h = get_h(nxt, target)
            f = g_n + h

            if nxt not in g_v or g_n < g_v[nxt]:
                g_v[nxt] = g_n
                parent[nxt] = current
                heapq.heappush(open_list, (f, nxt))

    return None

def water_dfs(j1,j2,target):
    start=(0,0)
    visited=set()
    capacities=(j1,j2)
    if is_goal(start,target):
        return [start]
    stack=[(start,[start])]
  

    while stack:
        current,path = stack.pop()
        if is_goal(current,target):
            return path
        
        if current in visited:
            continue
        visited.add(current)

        jug1, jug2 = current
        succ = [
            (j1, jug2),
            (jug1, j2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, j2 - jug2), jug2 + min(jug1, j2 - jug2)),
            (jug1 + min(jug2, j1 - jug1), jug2 - min(jug2, j1 - jug1))
        ]

        for nxt in succ:
            if  is_valid(nxt,capacities) and nxt not in visited:
                stack.append((nxt,path+[nxt]))
    return None

# Input and Execution
ju1 = int(input("Enter jug1: "))
ju2 = int(input("Enter jug2: "))
tar = int(input("Enter target: "))
path = water(ju1, ju2, tar)
if path:
    print("Solution found!")
    print(*path)
else:
    print("No solution")
pat=water_dfs(ju1,ju2,tar)
if pat:
    print("From DFS")
    print(*pat)
else:
    print("No solution")
