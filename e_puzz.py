import heapq

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def is_goal(board, goal):
    return board == goal

def get_mismatched(board, goal):
    mis = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                mis += 1
    return mis

def get_n(board):
    x, y = next((i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == 0)
    neig = []
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for nx, ny in moves:
        if 0 <= nx <= 2 and 0 <= ny <= 2:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neig.append(new_board)
    return neig

def a_puzz(board, goal):
    start = (get_mismatched(board, goal), 0, board, None)
    open_list = []
    visited = {}
    parent_map = {}  # Tracks parent-child relationship for path reconstruction

    heapq.heappush(open_list, start)

    while open_list:
        _, g, current, parent = heapq.heappop(open_list)

        # Track the parent of the current state
        current_tuple = tuple(tuple(row) for row in current)
        if current_tuple not in parent_map:
            parent_map[current_tuple] = parent

        if is_goal(current, goal):
            path = []
            # Path reconstruction using parent_map
            while current is not None:
                path.append(current)
                current = parent_map.get(tuple(tuple(row) for row in current))
            return path[::-1]

        visited[current_tuple] = True

        for nxt in get_n(current):
            nxt_tuple = tuple(tuple(row) for row in nxt)
            if nxt_tuple not in visited:
                h = get_mismatched(nxt, goal)
                heapq.heappush(open_list, (g + h + 1, g + 1, nxt, current))
    return None

initial_board = [[4, 1, 3],
                 [7, 2, 5],
                 [0, 8, 6]]

solution = a_puzz(initial_board, goal)
if solution:
    print("Solution found:")
    for idx, step in enumerate(solution):
        print(f"Step {idx + 1}:")
        for row in step:
            print(row)
        print()
else:
    print("No solution exists.")
