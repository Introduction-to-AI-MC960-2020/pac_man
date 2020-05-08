from pac_man.search import hill_climbing
from pac_man.utils import manhattan_distance
from pac_man.pacman_problem_astar import PacManProblem
from pac_man.maze_generator import generator

def h(node, goal, maze):
    return manhattan_distance(node, goal)

maze = generator.MAZE_simple_coin

pacman_problem = PacManProblem(maze.start_position, maze.goal_position, maze.maze_map, heuristic=h)
root = hill_climbing(pacman_problem)
path = root[1]
print(path)
maze.show_search_path()
maze.show_search_path(reached=path)