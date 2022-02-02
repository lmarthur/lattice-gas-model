#This file contains the agent class and its internal functions. The class can be modified or new ones can be written to adjust the movement algorithm. 
import numpy as np

class agent:
    def __init__(self, L):
        self.x=np.random.randint(0, L)
        self.y=np.random.randint(0, L)
        self.stored_resource=0
    
    def get_pos(self):
        return np.array([self.x, self.y])
    
    def pos_update(self):
        self.x=self.x+np.random.randint(-1, 2)
        self.y=self.y+np.random.randint(-1, 2)
        if self.x<0:
            self.x=self.x+L
        if self.y<0:
            self.y=self.y+L
        if self.x>=L:
            self.x=self.x-L
        if self.y>=L:
            self.y=self.y-L