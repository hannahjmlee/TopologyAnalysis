from src.betweenness import BetweennessCentrality
from src.visualize import *

import os

def main():
    map_list = ['empty-8-8', 'empty-16-16', 'empty-32-32', 'empty-48-48',
                'random-32-32-10', 'random-32-32- 20', 'random-64-64-10', 'random-64-64-20',
                'room-32-32-4', 'room-64-64-8', 'room-64-64-16',
                'maze-32-32-2', 'maze-32-32-4', 'maze-128-128-2', 'maze-128-128-10',
                'Berlin_1_256', 'Boston_0_256', 'Paris_1_256',
                'ht_chantry', 'ht_mansion_n', 'lak303d', 'lt_gallowstemplar_n', 'den312d', 'ost003d',
                'brc202d', 'den520d', 'w_woundedcoast']

    fig_dir = os.path.join(os.getcwd(), "figures")
    if not os.path.isdir(fig_dir): 
        os.mkdir(fig_dir)
        print("Making a new directory to hold the heatmap visualizations.")

    for map_name in map_list: 
        bc = BetweennessCentrality(map_name)
        bc.LoadGrid()

        image_name = os.path.join(os.getcwd(), "figures", map_name + ".png")
        
        print(f"Generating [{map_name}] visualization...")
        DisplayTopology(bc.bool_grid, bc.scored_grid, map_name, image_name)

if __name__=="__main__":
    main()