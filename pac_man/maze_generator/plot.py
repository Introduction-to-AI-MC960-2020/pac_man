import matplotlib.pyplot as plt
from pac_man.maze_generator.state import WALL, FREE, COIN

def plot_maze_search_path(start, goal, map, reached, seq, animate):
    mmap = [[255 if x == WALL else (0 if x == FREE else (160 if x == COIN else 100)) for x in row][:] for row in map]
    mmap[start[0]][start[1]] = 150
    mmap[goal[0]][goal[1]] = 200
    reached = [node for node in reached if node != start and node != goal]

    if animate:
        plt.matshow(mmap, fignum=0)
        plt.pause(.5)
        frame_pause = .01
        last = reached[0]

    for node in reached: # reached[1] == start, reached[-1] == goal
        i, j = node
        mmap[i][j] = 75
        if animate:
            mmap[last[0]][last[1]] = 4
            last = node
            plt.cla()
            plt.matshow(mmap, fignum=0)
            plt.pause(frame_pause)
    if animate:
        mmap[last[0]][last[1]] = 4

    for i, j in seq[:-1]: # seq[-1] == goal
        mmap[i][j] = 8
        if animate:
            plt.cla()
            plt.matshow(mmap, fignum=0)
            plt.pause(frame_pause)

    plt.axis('off')
    if not animate:
        plt.matshow(mmap, fignum=0, vmin=0, vmax=255, cmap='tab20b_r')
        plt.savefig('./output_search/{}-{}.png'.format(str(start),str(goal)))
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
