from src.parse import GetLines, CreateBooleanGrid
from src.search import * 

import os
import numpy as np
from collections import deque, defaultdict


class BetweennessCentrality:
    def __init__(self, map_name, debug = True):
        self.bool_grid = self.BuildBooleanGrid(map_name)
        self.scored_grid = np.zeros_like(self.bool_grid, dtype='float')
        self.pathfinder = Dijkstra(self.bool_grid, debug)

        self.n, self.m = self.bool_grid.shape
        self.vertices = list(self.pathfinder.neighbors.keys())

        self.save_name = os.path.join(os.getcwd(), "scored_benchmarks", map_name + ".npy")
        self.debug = debug 
        self.completed = set()

    def Brandes(self):
        betweenness = dict.fromkeys(self.vertices, 0.0)
        
        for s in self.vertices:
            # Single-source shortest-paths problem
            stack = []
            pred = {v: [] for v in self.vertices}  # Predecessors
            sigma = dict.fromkeys(self.vertices, 0)  # Number of shortest paths
            dist = dict.fromkeys(self.vertices, -1)  # Distance from source
            
            sigma[s] = 1
            dist[s] = 0
            
            Q = deque([s])
            while Q:
                v = Q.popleft()
                stack.append(v)
                for w in self.pathfinder.neighbors[v]:
                    # Path discovery
                    if dist[w] < 0:
                        Q.append(w)
                        dist[w] = dist[v] + 1
                    # Path counting
                    if dist[w] == dist[v] + 1:
                        sigma[w] += sigma[v]
                        pred[w].append(v)
            
            # Accumulation
            delta = dict.fromkeys(self.vertices, 0)
            while stack:
                w = stack.pop()
                # Calculate contributions from predecessors
                total_paths = sum(sigma[v] for v in pred[w])
                for v in pred[w]:
                    contribution = (sigma[v] / total_paths) * (1 + delta[w])
                    delta[v] += contribution
                if w != s:
                    betweenness[w] += delta[w]
        
        # Store the betweenness scores in self.scored_grid
        for v in betweenness:
            x, y = v  # Assuming v is a tuple representing (y, x) coordinates
            self.scored_grid[y, x] = betweenness[v] / 2.0

        np.save(self.save_name, self.scored_grid)
        return
    

    def LoadGrid(self): 
        self.scored_grid = np.load(self.save_name)
        self.NormalizeGrid()
    
    def NormalizeGrid(self): 
        min_val = np.min(self.scored_grid[self.scored_grid > 0])
        max_val = np.max(self.scored_grid)
        
        if min_val == max_val: 
            self.scored_grid = np.full(self.scored_grid.shape, min_val) 
            return
        self.scored_grid = (self.scored_grid - min_val) / (max_val - min_val)

    def BuildBooleanGrid(self, map_name):
        map_file = map_name + ".map"
        map_path = os.path.join(os.getcwd(), "benchmarks", map_file)

        map_lines = GetLines(map_path, 4)
        bool_grid = CreateBooleanGrid(map_lines)

        return bool_grid

