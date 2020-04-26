from maze_generator.maze import MazePacman

MAZE_1 = MazePacman((5,1), (1,5), [],
  [[1,1,1,1,1,1,1],
  [1,0,0,0,1,0,1],
  [1,0,0,0,1,0,1],
  [1,0,1,0,1,0,1],
  [1,0,1,0,0,0,1],
  [1,0,1,0,0,0,1],
  [1,1,1,1,1,1,1]]
)

MAZE_2 = MazePacman((12,2), (2,12), [(2,3),(3,4),(1,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,1,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)

MAZE_3 = MazePacman((12,1), (11,8), [(11,9),(3,4),(1,10)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,1,1,4,4,4,4,0,0,0,0,0,1],
  [1,0,1,1,1,1,0,1,1,0,0,0,0,1],
  [1,0,0,1,0,0,0,0,1,0,1,1,0,1],
  [1,1,0,1,0,0,0,1,1,4,4,1,0,1],
  [1,1,4,4,4,1,0,0,1,4,1,1,1,1],
  [1,1,4,1,0,1,4,1,1,4,1,0,4,1],
  [1,1,4,4,0,1,0,0,1,0,0,0,4,1],
  [1,1,0,1,0,1,4,1,1,0,1,1,0,1],
  [1,1,1,1,0,1,4,0,0,0,0,1,0,1],
  [1,0,0,0,0,1,4,1,1,1,1,1,0,1],
  [1,1,1,1,0,1,0,1,0,0,0,0,0,1],
  [1,0,0,0,0,1,0,1,0,0,0,1,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)