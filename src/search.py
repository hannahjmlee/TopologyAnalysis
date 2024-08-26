import numpy as np
from heapq import heappop, heappush, heapify
from collections import defaultdict

class Dijkstra():
    # Constructor: Initializes the AStarSearch instance with a grid and optional debug mode.
    def __init__(self, grid, debug=True):
        self.neighbors = dict()         # Dictionary to store neighbors of each grid cell
        self.InitializeNeighbors(grid)  # Initialize neighbors based on the grid
        self.debug = debug              # Debug mode flag

    class Node:
        # Constructor: Initializes a Node with a vertex, g-cost, and h-cost.
        def __init__(self, vertex, g):
            self.vertex = vertex    # Grid position of the node
            self.g = g              # Cost from start to the current node

        # Hash function for Node, based on its vertex and g-cost.
        def __hash__(self):
            return hash((self.vertex[0], self.vertex[1], self.g))

        # Less than operator: Defines priority in the priority queue based on f-cost (g + h).
        def __lt__(self, other):
            return self.g < other.g

        # Greater than operator: Inverse of the less than operator.
        def __gt__(self, other):
            return self.g > other.g

        # Equality operator: Two nodes are equal if they have the same vertex and g-cost.
        def __eq__(self, other):
            return self.vertex == other.vertex and self.g == other.g

    # Method: Finds all shortest paths from a start point to all other positions    
    def ShortestPathsFromStart(self, start): 
        if self.debug: 
            print(f"Solving shortest path from: {start}")

        parent = defaultdict(set) # tracks the parents of each shortest path 
        seen = set() # tracks evaluated nodes
        distances = defaultdict(lambda: float('inf')) # tracks minimum distance to each node

        current = self.Node(start, 0)
        pq = [current]
        heapify(pq)

        # run until all nodes have been evaluated 
        while len(pq) > 0: 
            current = heappop(pq)
            if current in seen: # if node has already been evaluated, skip it
                continue
            seen.add(current)

            new_g = current.g + 1 
            for neighbor in self.neighbors[current.vertex]: 
                # if this path is longer than the shortest path, continue
                if new_g > distances[neighbor]: 
                    continue 

                    
                new_node = self.Node(neighbor, new_g)
                # if the new path is shorter than the current path, remove all parents and
                # update the shortest distance
                if new_g < distances[neighbor]: 
                    distances[neighbor] = new_g
                    parent[neighbor].clear()
                
                # add vertex to parent list 
                parent[neighbor].add(current.vertex)
                # add node to priority queue 
                heappush(pq, new_node) 

        # returns a shortest paths parent dictionary 
        return parent 
                    

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
