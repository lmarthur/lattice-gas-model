#This file contains the environment class and its internal functions. This class can be modified to add new environmental characteristics, including additional resources, consumption of resources, and environmental productivity.

import numpy as np

class environment:
    def __init__(self, L):
        self.gridsize=L
        self.resource_field=np.random.rand(L, L)
        self.initial_resource=self.resource_field
        
    def get_value(self, i, j):
        return self.resource_field[i, j]
    
    def add_resource(self, i, j, frac):
        if self.resource_field[i, j]<self.initial_resource[i, j]:
            self.resource_field[i, j]+=1
            
    def subtract_resource(self, i, j, frac):
        if self.resource_field[i, j]>0
            self.resource_field[i, j]-=1