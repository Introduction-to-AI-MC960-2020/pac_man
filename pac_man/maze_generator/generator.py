from pac_man.maze_generator.maze import MazePacman

# 7 x 7
MAZE_1 = MazePacman((5,1), (1,5), [(1,2),(1,4),(4,4)],
  [[1,1,1,1,1,1,1],
  [1,4,0,4,0,0,1],
  [1,4,4,4,1,0,1],
  [1,0,1,0,1,0,1],
  [1,0,1,0,0,0,1],
  [1,0,1,0,0,0,1],
  [1,1,1,1,1,1,1]]
)

# 8 x 8
MAZE_X = MazePacman((1,1), (6,6), [(2,4),(3,5),(5,2)],
  [ [1,1,1,1,1,1,1,1],    
    [1,2,0,0,0,0,0,1],
    [1,4,0,0,5,0,0,1],
    [1,1,4,0,1,5,0,1],
    [1,1,4,0,1,1,0,1],
    [1,1,5,4,4,1,4,1],
    [1,1,1,1,1,1,3,1],
    [1,1,1,1,1,1,1,1]]
)

# 9 x 9
MAZE_9 = MazePacman((1,1), (1,7), [(7,1),(1,5),(5,6)],
  [ [1,1,1,1,1,1,1,1,1],    
    [1,2,1,4,4,5,1,3,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,5,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,5,4,4,1,4,4,4,1],
    [1,1,1,1,1,1,1,1,1]]
)

# 14 x 14
MAZE_14 = MazePacman((1,3), (12,8), [(8,4),(5,8),(6,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,0,0,2,1,4,4,4,4,4,4,4,4,1],
   [1,0,0,0,1,4,1,1,0,1,1,1,4,1],
   [1,1,0,1,1,4,4,4,4,4,4,4,4,1],
   [1,1,0,1,4,4,4,1,0,1,0,1,4,1],
   [1,1,0,4,4,1,4,0,5,0,0,1,4,1],
   [1,1,0,1,0,1,4,1,0,1,1,1,5,1],
   [1,1,0,0,0,1,4,1,1,1,1,1,0,1],
   [1,1,0,1,5,1,4,0,0,0,0,0,0,1],
   [1,1,0,1,0,1,4,1,1,1,1,1,0,1],
   [1,1,0,1,0,1,4,1,0,0,0,1,0,1],
   [1,1,0,1,0,1,0,0,0,0,0,0,0,1],
   [1,1,0,0,0,0,0,1,3,0,0,1,0,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)


MAZE_teste = MazePacman((1,2), (4,4), [],
  [ [1,1,1,1,1,1],
    [1,0,2,0,0,1],
    [1,0,0,1,0,1],
    [1,1,0,0,0,1],
    [1,1,1,1,3,1],
    [1,1,1,1,1,1]]
)

MAZE_teste_coin = MazePacman((1,2), (4,4), [],
  [ [1,1,1,1,1,1],
    [1,0,2,0,0,1],
    [1,0,0,1,0,1],
    [1,1,4,0,0,1],
    [1,1,1,1,3,1],
    [1,1,1,1,1,1]]
)

MAZE_simple_coin = MazePacman((1,2), (4,4), [],
  [ [1,1,1,1,1,1],
    [1,0,2,0,0,1],
    [1,0,4,1,0,1],
    [1,1,4,4,0,1],
    [1,1,1,1,3,1],
    [1,1,1,1,1,1]]
)
MAZE_teste_coin_2 = MazePacman((1,2), (4,4), [],
  [ [1,1,1,1,1,1],
    [1,0,2,0,0,1],
    [1,0,0,1,0,1],
    [1,0,0,0,0,1],
    [1,4,0,1,3,1],
    [1,1,1,1,1,1]]
)

# 14 x 14
MAZE_2 = MazePacman((12,1), (11,8), [(11,9),(3,4),(1,10)],
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

# 21 x 21
MAZE_3 = MazePacman((8,2), (8,19), [(7,6),(15,13),(2,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,1,4,4,4,4,4,4,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,0,1,0,0,0,0,4,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1],
  [1,4,4,4,4,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,1,0,0,1,0,0,0,0,1,0,4,1,4,0,1],
  [1,0,1,1,1,0,0,1,0,0,1,4,0,1,0,4,1,4,0,0,1],
  [1,0,1,0,1,0,0,0,1,0,0,4,1,0,4,1,4,0,0,0,1],
  [1,0,0,0,1,0,0,0,0,1,0,4,0,4,1,4,0,0,1,0,1],
  [1,4,1,0,1,1,0,1,1,0,4,0,4,1,4,0,0,1,1,1,1],
  [1,4,1,0,0,0,0,0,0,4,0,1,0,0,0,0,1,1,1,0,1],
  [1,4,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1],
  [1,4,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1],
  [1,4,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,4,4,4,1],
  [1,4,4,1,0,0,1,0,0,1,4,1,0,0,0,1,4,0,1,0,1],
  [1,0,4,1,0,1,0,0,0,1,4,1,0,0,0,0,1,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,4,4,1,0,0,0,0,0,0,1,0,1],
  [1,1,1,1,1,1,0,0,0,1,4,1,1,1,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,1,1,1,1,1,0,4,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,4,0,4,0,4,0,4,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)

# 42 x 42
MAZE_4 = MazePacman((6,38), (40,40), [(32,38),(15,13),(35,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,4,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
  [1,4,1,4,0,1,1,1,0,1,4,4,4,4,0,0,0,1,4,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1],
  [1,4,1,4,4,1,1,1,0,1,4,0,0,0,0,0,0,1,4,4,4,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1],
  [1,4,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1],
  [1,4,1,1,1,1,1,1,0,0,4,4,4,4,1,0,0,1,0,4,4,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,4,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,4,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
  [1,4,4,4,4,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
  [1,4,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1],
  [1,4,0,1,4,4,0,0,0,0,1,4,4,0,0,0,0,1,4,0,0,0,1,4,4,0,0,1,4,0,1,0,1,0,0,1,0,0,1,1,1,1],
  [1,4,0,1,4,4,4,0,0,0,1,4,0,4,0,0,0,0,4,0,1,0,0,0,4,1,0,1,4,0,1,0,1,0,0,1,0,1,1,1,1,1],
  [1,4,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,4,0,1,0,1,0,0,1,0,1,1,1,1,1],
  [1,4,0,1,4,4,4,0,0,0,1,4,4,0,0,0,0,1,4,4,1,0,1,0,4,1,0,0,4,4,1,0,1,0,0,1,0,1,1,1,1,1],
  [1,4,0,1,4,0,0,0,0,0,1,4,0,0,0,0,0,1,4,0,1,0,1,0,4,1,0,1,0,0,1,0,1,4,0,1,0,1,1,1,1,1],
  [1,0,0,1,4,0,0,0,0,0,1,4,4,0,0,0,0,1,4,0,1,0,1,0,0,1,0,1,0,0,1,0,1,4,4,1,0,0,1,1,1,1],
  [1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1],
  [1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,4,1,4,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1],
  [1,0,0,1,4,4,0,0,0,0,0,0,0,0,1,0,4,1,4,4,1,0,0,4,4,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1],
  [1,0,1,0,0,0,4,0,4,4,4,4,4,4,4,1,4,1,0,4,1,0,4,1,4,1,0,0,0,0,1,0,0,4,1,0,0,1,1,1,0,1],
  [1,0,1,4,0,1,1,4,4,4,1,1,0,4,4,1,4,1,0,4,1,4,4,1,1,1,1,0,0,0,0,0,0,0,4,1,0,0,0,1,0,1],
  [1,0,1,4,1,4,4,4,0,4,4,4,1,0,4,1,4,1,0,4,1,0,4,1,0,0,0,0,1,0,1,0,1,0,0,4,1,0,0,1,0,1],
  [1,0,1,4,1,0,4,0,1,0,0,4,1,4,4,1,4,1,4,4,1,0,0,1,0,0,0,1,0,4,0,1,0,0,0,0,4,1,0,1,0,1],
  [1,0,1,4,1,0,4,1,1,1,4,4,1,0,4,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,4,1,0,0,0,0,1],
  [1,0,1,0,1,0,4,1,1,1,4,4,1,4,4,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,4,0,4,4,4,1,0,0,0,1,1,1],
  [1,0,1,0,1,0,4,4,1,4,4,4,1,0,4,1,0,1,4,4,1,0,0,0,1,0,0,0,0,0,0,0,4,0,1,0,0,0,0,1,0,1],
  [1,0,1,0,0,1,0,4,1,4,0,0,1,4,4,0,0,1,0,4,1,0,0,1,0,1,0,1,0,0,0,1,4,1,0,4,4,4,4,1,0,1],
  [1,0,1,4,0,0,1,4,4,4,0,1,0,0,0,1,0,1,0,4,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,4,1,1,0,1,0,1],
  [1,0,1,4,0,0,0,1,1,1,1,0,0,4,0,1,0,1,4,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,4,4,1,0,0,1,0,1],
  [1,0,1,4,0,0,1,0,0,0,4,4,4,4,0,1,0,1,4,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1],
  [1,0,1,0,4,0,1,0,1,0,1,1,0,4,4,1,0,1,4,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
  [1,0,1,0,0,4,1,1,1,4,0,1,0,0,4,1,0,1,0,4,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
  [1,0,0,1,0,4,4,0,4,4,0,1,0,0,1,0,0,1,4,4,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1],
  [1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
  [1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)

# 42 x 42
MAZE_5 = MazePacman((6,9), (37,27), [(22,32),(15,13),(35,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,0,0,0,0,0,0,1,4,1,0,1,0,0,0,0,0,1,0,1,0,1,0,4,0,0,0,0,0,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,0,0,0,1,4,4,0,1,0,1,0,1,0,1,0,1,0,4,0,1,0,1,4,0,0,0,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,0,0,0,0,1,4,4,0,1,0,1,0,1,0,1,0,1,4,1,0,1,4,1,4,1,4,1,4,4,0,0,0,1,1,1,1,1],
  [1,1,1,1,0,0,0,1,4,4,0,1,0,1,0,0,0,1,4,1,4,1,4,1,0,1,0,4,0,1,0,4,0,1,0,0,0,0,1,1,1,1],
  [1,1,1,0,0,1,4,4,0,1,0,1,0,1,0,1,0,1,4,1,4,1,0,1,0,1,0,1,4,0,0,1,0,1,0,1,0,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,4,4,4,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,4,4,4,0,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,1,4,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,4,1,1,1,0,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,0,4,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,4,1,4,1,0,0,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,4,4,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,4,1,4,1,4,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,4,0,1,0,1,0,0,1,0,1,4,4,4,1,0,1,0,1,0,0,1,4,1,4,1,4,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,4,4,1,0,1,0,0,1,0,1,0,4,4,4,0,1,0,1,0,0,1,4,1,4,0,4,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,4,1,1,1,1,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,4,4,4,0,4,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,4,0,1,4,4,0,0,0,1,1,1],
  [1,1,1,1,0,4,4,4,0,0,0,1,4,4,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,4,4,0,1,0,0,1,1,1,1],
  [1,1,1,1,1,0,0,1,4,1,0,4,4,1,0,1,0,1,0,4,4,4,0,1,0,1,0,1,4,4,4,1,0,1,0,0,0,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,4,1,0,1,0,1,0,1,0,1,4,1,1,1,4,1,0,0,0,1,4,1,0,1,0,0,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,0,0,4,4,1,0,1,0,1,0,1,0,4,4,4,0,1,0,1,0,1,4,1,0,0,0,0,0,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)

MAZE_6 = MazePacman((1,1), (6,6), [(2,4),(3,5),(5,2)],
  [[1,1,1,1,1,1,1,1],    
  [1,2,0,0,0,0,0,1],
  [1,4,0,0,5,0,0,1],
  [1,1,4,0,1,5,0,1],
  [1,1,4,0,1,1,0,1],
  [1,1,5,4,4,1,4,1],
  [1,1,1,1,1,1,3,1],
  [1,1,1,1,1,1,1,1]]
)

# 5 x 5
MAZE_5x5 = MazePacman((3,3), (1,1), [],
  [[1,1,1,1,1],    
  [1,3,0,4,1],
  [1,0,4,0,1],
  [1,0,0,2,1],
  [1,1,1,1,1]]
)

# 6 x 6
MAZE_6x6 = MazePacman((2,1), (3,4), [(2,2), (2,3), (3,2)],
  [[1,1,1,1,1,1],    
  [1,0,0,0,0,1],
  [1,2,5,5,0,1],
  [1,0,5,4,3,1],
  [1,0,0,0,0,1],
  [1,1,1,1,1,1]]
)

# 7 x 7
MAZE_7x7 = MazePacman((5,1), (1,5), [(1,2),(1,4),(4,4)],
  [[1,1,1,1,1,1,1],
  [1,4,0,4,0,0,1],
  [1,4,4,4,1,0,1],
  [1,0,1,0,1,0,1],
  [1,0,1,0,0,0,1],
  [1,0,1,0,0,0,1],
  [1,1,1,1,1,1,1]]
)

# 8 x 8
MAZE_8x8 = MazePacman((1,1), (6,6), [(2,4),(3,5),(5,2)],
  [ [1,1,1,1,1,1,1,1],    
    [1,2,0,0,0,0,0,1],
    [1,4,0,0,5,0,0,1],
    [1,1,4,0,1,5,0,1],
    [1,1,4,0,1,1,0,1],
    [1,1,5,4,4,1,4,1],
    [1,1,1,1,1,1,3,1],
    [1,1,1,1,1,1,1,1]]
)

# 9 x 9
MAZE_9x9 = MazePacman((1,1), (1,7), [(7,1),(1,5),(5,6)],
  [ [1,1,1,1,1,1,1,1,1],    
    [1,2,1,4,4,5,1,3,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,5,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,5,4,4,1,4,4,4,1],
    [1,1,1,1,1,1,1,1,1]]
)

# 10 x 10
MAZE_10x10 = MazePacman((1,4), (8,4), [(1,2),(1,5),(4,3)],
  [ [1,1,1,1,1,1,1,1,1,1],    
    [1,0,5,0,2,5,4,4,0,1],
    [1,0,0,0,0,0,0,0,4,1],
    [1,0,0,0,0,0,0,0,4,1],
    [1,0,0,5,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,4,1],
    [1,0,0,0,0,0,0,0,4,1],
    [1,0,1,1,1,1,1,0,0,1],
    [1,0,0,0,3,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]]
)


# 11 x 11
MAZE_11x11 = MazePacman((3,5), (8,8), [(6,3),(7,3),(7,2)],
   [[1,1,1,1,1,1,1,1,1,1,1],    
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,0,0,2,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,5,4,4,4,4,4,0,1],
    [1,0,5,5,4,4,0,1,1,0,1],
    [1,0,0,0,4,4,0,1,3,0,1],
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1]]
)


# 14 x 14
MAZE_14x14 = MazePacman((12,1), (11,8), [(11,9),(3,4),(1,10)],
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

# 21 x 21
MAZE_21x21 = MazePacman((8,2), (8,19), [(7,6),(15,13),(2,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,1,4,4,4,4,4,4,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,0,1,0,0,0,0,4,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1],
  [1,4,4,4,4,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,1,0,0,1,0,0,0,0,1,0,4,1,4,0,1],
  [1,0,1,1,1,0,0,1,0,0,1,4,0,1,0,4,1,4,0,0,1],
  [1,0,1,0,1,0,0,0,1,0,0,4,1,0,4,1,4,0,0,0,1],
  [1,0,0,0,1,0,0,0,0,1,0,4,0,4,1,4,0,0,1,0,1],
  [1,4,1,0,1,1,0,1,1,0,4,0,4,1,4,0,0,1,1,1,1],
  [1,4,1,0,0,0,0,0,0,4,0,1,0,0,0,0,1,1,1,0,1],
  [1,4,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1],
  [1,4,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1],
  [1,4,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,4,4,4,1],
  [1,4,4,1,0,0,1,0,0,1,4,1,0,0,0,1,4,0,1,0,1],
  [1,0,4,1,0,1,0,0,0,1,4,1,0,0,0,0,1,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,4,4,1,0,0,0,0,0,0,1,0,1],
  [1,1,1,1,1,1,0,0,0,1,4,1,1,1,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,1,1,1,1,1,0,4,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,4,0,4,0,4,0,4,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)

# 42 x 42
MAZE_42x42 = MazePacman((6,9), (37,27), [(22,32),(15,13),(35,12)],
  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,0,0,0,0,0,0,1,4,1,0,1,0,0,0,0,0,1,0,1,0,1,0,4,0,0,0,0,0,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,0,0,0,1,4,4,0,1,0,1,0,1,0,1,0,1,0,4,0,1,0,1,4,0,0,0,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,0,0,0,0,1,4,4,0,1,0,1,0,1,0,1,0,1,4,1,0,1,4,1,4,1,4,1,4,4,0,0,0,1,1,1,1,1],
  [1,1,1,1,0,0,0,1,4,4,0,1,0,1,0,0,0,1,4,1,4,1,4,1,0,1,0,4,0,1,0,4,0,1,0,0,0,0,1,1,1,1],
  [1,1,1,0,0,1,4,4,0,1,0,1,0,1,0,1,0,1,4,1,4,1,0,1,0,1,0,1,4,0,0,1,0,1,0,1,0,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,4,4,4,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,4,4,4,0,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,1,4,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,4,1,1,1,0,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,0,4,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,4,1,4,1,0,0,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,4,4,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,4,1,4,1,4,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,4,0,1,0,1,0,0,1,0,1,4,4,4,1,0,1,0,1,0,0,1,4,1,4,1,4,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,4,4,1,0,1,0,0,1,0,1,0,4,4,4,0,1,0,1,0,0,1,4,1,4,0,4,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,4,1,1,1,1,1,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,4,4,4,0,4,4,1,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
  [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
  [1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,4,0,1,4,4,0,0,0,1,1,1],
  [1,1,1,1,0,4,4,4,0,0,0,1,4,4,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,4,4,0,1,0,0,1,1,1,1],
  [1,1,1,1,1,0,0,1,4,1,0,4,4,1,0,1,0,1,0,4,4,4,0,1,0,1,0,1,4,4,4,1,0,1,0,0,0,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,4,1,0,1,0,1,0,1,0,1,4,1,1,1,4,1,0,0,0,1,4,1,0,1,0,0,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,0,0,4,4,1,0,1,0,1,0,1,0,4,4,4,0,1,0,1,0,1,4,1,0,0,0,0,0,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
)
