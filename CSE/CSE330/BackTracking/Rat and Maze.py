def rat_maze(maze):
    res = []
    n = len(maze)
    board = [["0"]*n for _ in range(n)]

    def btrack(x, y):

        if x < n and y < n and maze[x][y] == "1":
            board[x][y] = "1"

            if x == n - 1 and y == n - 1:
                res.append(board.copy())
                return True

            if btrack(x, y + 1):
                return True

            if btrack(x + 1, y):
                return True

            board[x][y] = "0"
            return False

        else:
            return False

    if btrack(0, 0):
        return res
    else:
        return "No path"


if __name__ == "__main__":
    # n = int(input())
    # maze = []
    # for _ in range(n):
    #     maze.append(list(input()))
    maze = ["1000", "1100", "0110", "0011"]
    print(*rat_maze(maze)[0], sep="\n")

