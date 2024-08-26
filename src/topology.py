from src.parse import GetLines, CreateBooleanGrid
from src.search import * 

import os
import numpy as np


class TopologyMap:
    def __init__(self, map_name, debug = True):
        self.bool_grid = self.BuildBooleanGrid(map_name)
        self.scored_grid = np.zeros_like(self.bool_grid)
        self.pathfinder = Dijkstra(self.bool_grid, debug)

        self.n, self.m = self.bool_grid.shape
        self.vertices = list(self.pathfinder.neighbors.keys())

        self.save_name = os.path.join(os.getcwd(), "scored_benchmarks", map_name + ".npy")
        self.debug = debug 

    def LoadGrid(self): 
        self.scored_grid = np.load(self.save_name) 
        self.NormalizeGrid() 


    def ScoreGrid(self):
        for (x, y) in self.vertices: 
            path_tracker = self.pathfinder.ShortestPathsFromStart((x, y))
            mini_grid = self.ScoreStartingPoint(path_tracker, (x, y))
            self.scored_grid = self.scored_grid + mini_grid

        np.save(self.save_name, self.scored_grid)
        return 
    
    def NormalizeGrid(self): 
        min_val = np.min(self.scored_grid)
        # min_val = 0
        max_val = np.max(self.scored_grid)
        
        if min_val == max_val: 
            self.scored_grid = np.full(self.scored_grid.shape, min_val) 
            return
        print(self.scored_grid) 
        self.scored_grid = (self.scored_grid - min_val) / (max_val - min_val )
        print(self.scored_grid)  


    def ScoreStartingPoint(self, parents, start): 
        global_cost_grid = np.zeros_like(self.bool_grid, dtype = 'int')
        cost_grid = np.zeros_like(self.bool_grid, dtype='int')
        
        def dfs(node):
            # If we reach the start node, there is one valid path
            x, y = node
            cost_grid[y,x] += 1
            if node == start:
                return 1
            # If the node has no parent, there is no valid path (this case should not happen if the graph is connected)
            if node not in parents:
                return 0
            # Sum up the number of paths by recursively exploring all parents
            return sum(dfs(p) for p in parents[node])

        count = 0
        for (x, y) in self.vertices: 
            if (x, y) == start: 
                continue
            
            paths = []
            cost_grid = np.zeros_like(self.bool_grid, dtype='int')
            num_paths = dfs((x, y)) 

            cost_grid[y, x] = 0
            global_cost_grid = global_cost_grid + cost_grid

        global_cost_grid[start[1], start[0]] = 0
        return global_cost_grid

    def BuildBooleanGrid(self, map_name):
        map_file = map_name + ".map"
        map_path = os.path.join(os.getcwd(), "benchmarks", map_file)

        map_lines = GetLines(map_path, 4)
        bool_grid = CreateBooleanGrid(map_lines)

        return bool_grid

