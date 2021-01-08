from helper.solver import MazeSolver

def main(maze):
    solver = MazeSolver()
    print("Robot maze solution is ", solver.solve_maze(maze))



if __name__=="__main__":
    maze = [
    [".","x",".",".","."],
    [".",".",".","x","."],
    [".","x","x",".","."],
    [".","x","x",".","x"],
    [".","x","x",".","."]]
    main(maze)
