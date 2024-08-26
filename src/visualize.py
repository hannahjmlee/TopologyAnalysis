import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from PIL import Image

def PreprocessMap(bool_grid):
    obstacles = []
    for x in range(bool_grid.shape[1]):
        for y in range(bool_grid.shape[0]):
            if not bool_grid[y][x]:
                obstacles.append((x, y))

    bounds = ((0, bool_grid.shape[1]), (0, bool_grid.shape[0]))

    return bounds, obstacles

def DisplayEnvironment(grid, map_name, output_name):
    bounds, obstacles = PreprocessMap(grid)
    fig, ax = plt.subplots(figsize = (8,8))

    ax.clear()
    ax.set_aspect('equal')
    ax.autoscale(False)
    ax.set_xlim(bounds[0][0] - 0.5, bounds[0][1] - 0.5)
    ax.set_ylim(bounds[1][0] - 0.5, bounds[1][1] - 0.5)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')

    for obstacle in obstacles:
        plt.fill_between([obstacle[0] - 0.5, obstacle[0] + 0.5],
                        obstacle[1] - 0.5, obstacle[1] + 0.5,
                        color='black')
    # ax.set_title(map_name)
    plt.savefig(output_name)

def DisplayTopology(grid, topology, map_name, output_name): 
    bounds, obstacles = PreprocessMap(grid) 
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.clear() 
    ax.set_aspect('equal')
    ax.autoscale(False)
    ax.set_xlim(bounds[0][0] - 0.5, bounds[0][1] - 0.5)
    ax.set_ylim(bounds[1][0] - 0.5, bounds[1][1] - 0.5)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')

    cmap = plt.get_cmap('viridis')  # You can choose a different colormap if desired
    im = ax.imshow(topology, cmap=cmap, origin='lower', extent=[-0.5, grid.shape[1] - 0.5, -0.5, grid.shape[0] - 0.5])
    plt.colorbar(im, ax=ax, label='Normalized Value')

    for obstacle in obstacles:
        plt.fill_between([obstacle[0] - 0.5, obstacle[0] + 0.5],
                        obstacle[1] - 0.5, obstacle[1] + 0.5,
                        color='black')




        plt.figure(figsize=(8, 6))

    ax.set_title(map_name)
    plt.savefig(output_name)