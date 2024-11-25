import heapq

def calculate_mismatched_tiles(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    mismatched = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                mismatched += 1
    return mismatched

def get_neighbors(board):
    neighbors = []
    x, y = next((i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == 0)

    # Possible moves: up, down, left, right
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for nx, ny in moves:
        if 0 <= nx < 3 and 0 <= ny < 3:  # Check bounds
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]  # Swap tiles
            neighbors.append(new_board)
    return neighbors

def is_goal(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def a_star(initial_board):
    start = (calculate_mismatched_tiles(initial_board), 0, initial_board, None)  # (f, g, board, parent)
    open_set = []
    heapq.heappush(open_set, start)
    visited = {}

    while open_set:
        _, g, current_board, parent = heapq.heappop(open_set)

        # If the goal is reached, reconstruct the path
        if is_goal(current_board):
            path = []
            while current_board:
                path.append(current_board)
                current_board = parent
                parent = visited.get(tuple(tuple(row) for row in current_board))
            return path[::-1]  # Return reversed path

        # Mark current board as visited
        visited[tuple(tuple(row) for row in current_board)] = parent

        # Explore neighbors
        for neighbor in get_neighbors(current_board):
            if tuple(tuple(row) for row in neighbor) not in visited:
                h = calculate_mismatched_tiles(neighbor)
                heapq.heappush(open_set, (g + 1 + h, g + 1, neighbor, current_board))

    return None  # No solution found

# Example usage:
initial_board = [[1, 2, 3],
                 [4, 0, 5],
                 [7, 8, 6]]

solution = a_star(initial_board)
if solution:
    print("Solution found:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists.")
