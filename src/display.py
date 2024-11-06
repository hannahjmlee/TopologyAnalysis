import matplotlib.pyplot as plt

# Function: helper that finds the positions of all obstacles and the bounds of the map
def PreprocessMap(bool_grid):
    obstacles = []
    for x in range(bool_grid.shape[1]):
        for y in range(bool_grid.shape[0]):
            if not bool_grid[y][x]:
                obstacles.append((x, y))

    bounds = ((0, bool_grid.shape[1]), (0, bool_grid.shape[0]))

    return bounds, obstacles


# Function: displays environment with betweenness centrality values overlayed as a heat map
def DisplayTopology(grid, topology, map_name, output_name):
    bounds, obstacles = PreprocessMap(grid)
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.clear()
    ax.set_aspect('equal')
    ax.autoscale(False)
    ax.set_xlim(bounds[0][0] - 0.5, bounds[0][1] - 0.5)
    ax.set_ylim(bounds[1][0] - 0.5, bounds[1][1] - 0.5)
    # ax.set_xlabel('X Position')
    # ax.set_ylabel('Y Position')

    cmap = plt.get_cmap('coolwarm')  # You can choose a different colormap if desired
    im = ax.imshow(topology, cmap=cmap, origin='lower', extent=[-0.5, grid.shape[1] - 0.5, -0.5, grid.shape[0] - 0.5])

    for obstacle in obstacles:
        plt.fill_between([obstacle[0] - 0.5, obstacle[0] + 0.5],
                        obstacle[1] - 0.5, obstacle[1] + 0.5,
                        color='black')

    cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
    cb = plt.colorbar(im, cax=cax, label='Betweenness Centrality',fraction=0.046, pad=0.04)
    cb.set_label('Betweenness Centrality', fontsize=13)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    ax.set_title("Topology of " + map_name)
    plt.savefig(output_name, bbox_inches='tight')
    plt.close()
