from src.parse import GetLines, CreateBooleanGrid

import os
import numpy as np
from collections import deque


class BetweennessCentrality:
    def __init__(self, map_name):
        # boolean grid indicating free space and obstacle space positions
        self.bool_grid = self.BuildBooleanGrid(map_name)

        # empty initialized scoring grid
        self.scored_grid = np.zeros_like(self.bool_grid, dtype='float')
        
        # finds stores the neighbors for all free vertices
        self.neighbors = dict()
        self.InitializeNeighbors(self.bool_grid)
        
        # list of all free vertices
        self.vertices = list(self.neighbors.keys())

        # default name for saving the scoring for a map in the scored_benchmarks directory
        self.save_name = os.path.join(os.getcwd(), "scored_benchmarks", map_name + ".npy")      

    # Method: Uses Brandes' Betweenness Centrality Algorithm to score a given map
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
                for w in self.neighbors[v]:
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


    # Method: Parses map file and creates a boolean grid indicating free and obstacle space
    def BuildBooleanGrid(self, map_name):
        map_file = map_name + ".map"
        map_path = os.path.join(os.getcwd(), "benchmarks", map_file)

        map_lines = GetLines(map_path, 4)
        bool_grid = CreateBooleanGrid(map_lines)

        return bool_grid


    # Method: Initializes neighbors for each grid cell based on the grid structure.
    def InitializeNeighbors(self, grid):
        max_y, max_x = grid.shape

        for x in range(max_x):
            for y in range(max_y):
                if not grid[(y, x)]:
                    continue

                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                valid_neighbors = set()
                for neighbor in neighbors:
                    if neighbor[0] < 0 or neighbor[0] >= max_x:
                        continue
                    if neighbor[1] < 0 or neighbor[1] >= max_y:
                        continue
                    if not grid[(neighbor[1], neighbor[0])]:
                        continue
                    valid_neighbors.add(neighbor)
                self.neighbors[(x, y)] = valid_neighbors
    
    # Method: Loads an existing scoring and normalizes it
    def LoadGrid(self): 
        self.scored_grid = np.load(self.save_name)
        self.NormalizeGrid()

    # Method: Normalizes the betweenness centrality values between [0, 1]
    def NormalizeGrid(self): 
        min_val = np.min(self.scored_grid[self.scored_grid > 0])
        max_val = np.max(self.scored_grid)
        
        if min_val == max_val: 
            self.scored_grid = np.full(self.scored_grid.shape, min_val) 
            return
        self.scored_grid = (self.scored_grid - min_val) / (max_val - min_val)