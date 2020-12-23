from .greetings import Greetings
class MazeSolver:
    def __init__(self):
        self.greetings = Greetings()
    def solve_maze(self,maze):
        self.greetings.print_maze(maze)
        if len(maze) < 1 or len(maze[0]) < 1:
            return None

        return self.solve_maze_helper(maze, [], 0,0)

    def solve_maze_helper(self, maze, sol, row, col):
        row_num = len(maze)
        col_num = len(maze[0])

        if row == row_num -1 and col == col_num -1:
            maze[row][col] = "\033[1;32;40m*"
            print()
            self.greetings.print_maze(maze)
            print()
            return sol

        if row >= row_num or col >= col_num:
            return None

        if maze[row][col] == "x":
            return None


        sol.append("r")
        maze[row][col] = "\033[1;32;40m*"
        going_right = self.solve_maze_helper(maze, sol, row, col +1)
        if going_right is not None:
            return going_right
        sol.pop()
        maze[row][col] = "."


        sol.append("d")
        maze[row][col] = "\033[1;32;40m*"
        going_down = self.solve_maze_helper(maze, sol, row +1, col)
        if going_down is not None:
            return going_down
        sol.pop()
        maze[row][col] = "."

        return None
