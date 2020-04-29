from pac_man.maze_generator.state import START, GOAL, GHOST
from pac_man.maze_generator.plot import plot_maze_search_path

class MazePacman():
  def __init__(self, start_position, goal_position, ghosts_position, maze_map):
    self.start_position = start_position
    self.goal_position = goal_position
    self.ghosts_position = ghosts_position
    self.maze_map = maze_map

    self.maze_map[start_position[0]][start_position[1]] = START
    self.maze_map[goal_position[0]][goal_position[1]] = GOAL
    
    if len(ghosts_position) > 0:
      first_ghost_position = ghosts_position[0]
      second_ghost_position = ghosts_position[1]
      third_ghost_position = ghosts_position[2]

      self.maze_map[first_ghost_position[0]][first_ghost_position[1]] = GHOST
      self.maze_map[second_ghost_position[0]][second_ghost_position[1]] = GHOST
      self.maze_map[third_ghost_position[0]][third_ghost_position[1]] = GHOST

  def show_search_path(self, reached=[], seq=[]):
    plot_maze_search_path(self.start_position, self.goal_position, 
      self.maze_map, reached, seq, False)
