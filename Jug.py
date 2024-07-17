import heapq

def is_valid_state(state, capacities):
    jug1, jug2 = state
    return 0 <= jug1 <= capacities[0] and 0 <= jug2 <= capacities[1]

def is_goal_state(state, target):
    return state[0] == target or state[1] == target

def calculate_h_value(state, target):
    return min(abs(state[0] - target), abs(state[1] - target))

def a_star_water_jug(jug1_capacity, jug2_capacity, target):
    start_state = (0, 0)
    if is_goal_state(start_state, target):
        return [start_state]

    capacities = (jug1_capacity, jug2_capacity)
    closed_list = set()
    open_list = []
    heapq.heappush(open_list, (0, start_state))

    parent_map = {start_state: None}
    g_values = {start_state: 0}

    while open_list:
        _, current_state = heapq.heappop(open_list)

        if current_state in closed_list:
            continue

        closed_list.add(current_state)

        if is_goal_state(current_state, target):
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1]

        jug1, jug2 = current_state
        successors = [
            (jug1_capacity, jug2), # Fill Jug1
            (jug1, jug2_capacity), # Fill Jug2
            (0, jug2),             # Empty Jug1
            (jug1, 0),             # Empty Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)), # Pour Jug1 to Jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))  # Pour Jug2 to Jug1
        ]

        for next_state in successors:
            if not is_valid_state(next_state, capacities) or next_state in closed_list:
                continue

            g_new = g_values[current_state] + 1
            h_new = calculate_h_value(next_state, target)
            f_new = g_new + h_new

            if next_state not in g_values or g_new < g_values[next_state]:
                g_values[next_state] = g_new
                heapq.heappush(open_list, (f_new, next_state))
                parent_map[next_state] = current_state

    return None

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

path = a_star_water_jug(jug1_capacity, jug2_capacity, target)
if path:
    print("Path to target:")
    for state in path:
        print(state)
else:
    print("No solution found.")
