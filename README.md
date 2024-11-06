
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
