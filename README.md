
# TopologyAnalysis

This Python library facilitates the analysis of environment topologies for robotic navigation and pathfinding. Leveraging Brandes' Betweenness Centrality Algorithm, it computes a normalized betweenness centrality score for a given environment representation and visualizes the results as a heatmap overlay.

## Dependencies
This library requires:

 1. `numpy`
 2. `matplotlib`

## Usage

To reproduce our results, start by extracting all benchmarks:

    ./init.sh

Next, score the benchmarks. This process may take time; all scores will be saved in the `scored_benchmarks` directory:

    python score.py

Finally, generate visualizations with the following command. All images will be saved in the `figures` directory:

    python visualize.py

If you do not wish to reproduce the results for all benchmarks, you will need to modify the list of maps that are evaluated in both `score.py` and `visualize.py`.



## Betweenness Centrality Visualization
| Map Name| Betweenness Centrality Visualization | 
|--|--|
|  empty-8-8 | ![bc-empty-8-8](./figures/empty-8-8.png) | 
|  empty-16-16 | ![bc-empty-16-16](./figures/empty-16-16.png) | 
|  empty-32-32 | ![bc-empty-32-32](./figures/empty-32-32.png) | 
|  empty-48-48 | ![bc-empty-48-48](./figures/empty-48-48.png) | 
|  random-32-32-10 | ![bc-random-32-32-10](./figures/random-32-32-10.png) | 
|  random-32-32-20 | ![bc-random-32-32-20](./figures/random-32-32-20.png) | 
|  random-64-64-10 | ![bc-random-64-64-10](./figures/random-64-64-10.png) | 
|  random-64-64-20 | ![bc-random-64-64-20](./figures/random-64-64-20.png) | 
|  room-32-32-4 | ![bc-room-32-32-4](./figures/room-32-32-4.png) |
|  room-64-64-8 | ![bc-room-64-64-8](./figures/room-64-64-8.png) |
|  room-64-64-16 | ![bc-room-64-64-16](./figures/room-64-64-16.png) | 
|  maze-32-32-2 | ![bc-maze-32-32-2](./figures/maze-32-32-2.png) |
|  maze-32-32-4 | ![bc-maze-32-32-4](./figures/maze-32-32-4.png) 
|  maze-128-128-10 | ![bc-maze-128-128-10](./figures/maze-128-128-10.png) |  
|  maze-128-128-2 | ![bc-maze-128-128-2](./figures/maze-128-128-2.png) | 
|  Berlin_1_256 | ![bc-Berlin_1_256](./figures/Berlin_1_256.png) |
|  Boston_0_256 | ![bc-Boston_0_256](./figures/Boston_0_256.png) 
|  Paris_1_256 | ![bc-Paris_1_256](./figures/Paris_1_256.png) | 
|  ht_chantry | ![bc-ht_chantry](./figures/ht_chantry.png) | 
|  ht_mansion_n | ![bc-ht_mansion_n](./figures/ht_mansion_n.png) 
|  lak303d | ![bc-lak303d](./figures/lak303d.png) | 
|  lt_gallowstemplar_n | ![bc-lt_gallowstemplar_n](./figures/lt_gallowstemplar_n.png) | 
|  den312d | ![bc-den312d](./figures/den312d.png) | 
|  ost003d | ![bc-ost003d](./figures/ost003d.png) | 
|  brc202d | ![bc-brc202d](./figures/brc202d.png) | 
|  den520d | ![bc-den520d](./figures/den520d.png) | 
|  w_woundedcoast | ![bc-w_woundedcoast](./figures/w_woundedcoast.png) |

