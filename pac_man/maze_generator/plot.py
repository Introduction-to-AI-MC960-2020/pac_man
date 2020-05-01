import matplotlib.pyplot as plt
from pac_man.maze_generator.state import WALL, FREE, COIN, START, GOAL, GHOST

def plot_maze_search_path(start, goal, map, reached):
    maze_map = [[[0,0,0] if x == WALL 
    else ([255,255,255] if x == FREE 
    else ([255,255,0] if x == COIN 
    else ([0,0,255] if x == START
    else ([0,255,0] if x == GOAL else [255,0,0] #ghost
    )))) for x in row][:] for row in map]

    reached = [node for node in reached if node != start and node != goal]

    for state in reached:
        i, j = state
        maze_map[i][j] = [128,128,128]
        
    plt.axis('off')    
    plt.imshow(maze_map)
    #plt.savefig('./output_search/{}-{}.png'.format(str(start),str(goal)))
    plt.show()

def save_heatmap(start, goal, map, reached, seq, file_name):
    mmap = [row[:] for row in map]
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            mmap[i][j] = -2.0 if map[i][j] == WALL else -6.0
    mmap[start[0]][start[1]] = 32
    mmap[goal[0]][goal[1]] = 32
    wave = 0
    reached = [node for node in reached if node != start and node != goal]
    reached_amount = len(reached)

    for node in reached:
        i, j = node
        if node != start and node != goal:
            wave += 1
            wave_ratio = int (10 * wave / reached_amount)
            mmap[i][j] = wave_ratio * 1.6 + 4

    for i, j in seq[:-1]: # seq[-1] == goal
        mmap[i][j] = 24

    plt.cla()
    plt.matshow(mmap, fignum=0)
    plt.savefig(file_name, bbox_inches='tight')

def print_heatmap(start, goal, map, reached, seq):
    mmap = [row[:] for row in map]
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            mmap[i][j] = -2.0 if map[i][j] == WALL else -6.0
    mmap[start[0]][start[1]] = 32
    mmap[goal[0]][goal[1]] = 32
    wave = 0
    reached = [node for node in reached if node != start and node != goal]
    reached_amount = len(reached)

    for node in reached:
        i, j = node
        if node != start and node != goal:
            wave += 1
            wave_ratio = int (10 * wave / reached_amount)
            mmap[i][j] = wave_ratio * 1.6 + 4

    for i, j in seq[:-1]: # seq[-1] == goal
        mmap[i][j] = 24

    plt.cla()
    plt.matshow(mmap, fignum=0)
    plt.show()
