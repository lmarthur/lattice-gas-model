#This file contains the environment class and its internal functions. This class can be modified to add new environmental characteristics, including additional resources, consumption of resources, and environmental productivity.

import numpy as np

class environment:
    def __init__(self, L):
        self.gridsize=L
        self.resource_field=np.random.rand(L, L)
    
    def get_value(self, i, j):
        return self.resource_field[i, j]
    
    def resource_update(self, i, j, frac):
        self.resource_field[i, j]=(1-frac)*self.resource_field[i, j]