#This file contains the environment class and its internal functions. This class can be modified to add new environmental characteristics, including additional resources, consumption of resources, and environmental productivity.

import numpy as np

class environment:
    def __init__(self, L):
        self.gridsize=L
        #self.resource_field=100*np.random.rand(L, L)
        self.resource_field=np.array([np.array([10]*L)]*L)
        self.initial_resource=self.resource_field
        
    def get_value(self, i, j):
        return self.resource_field[i, j]
    
    def add_resource(self, i, j):
        if self.resource_field[i, j]<self.initial_resource[i, j]:
            self.resource_field[i, j]+=1
            
    def subtract_resource(self, i, j):
        if self.resource_field[i, j]>1:
            self.resource_field[i, j]-=1

class agent:
    def __init__(self, L):
        self.x=np.random.randint(1, L-1)
        self.y=np.random.randint(1, L-1)
        self.stored_resource=0
    
    def get_pos(self):
        return np.array([self.x, self.y])
    
    def choose_element(self, array, probabilities):
        length=len(array)
        cum_sum=np.zeros(length)
        cum_sum[0]=probabilities[0]
        for i in range(length):
            cum_sum[i]=cum_sum[i-1]+probabilities[i]
        r=np.random.rand()

        if r<=cum_sum[0]:
            return array[0]

        for i in range(length):
            if r<=cum_sum[i]:
                return array[i]

    def move_condition(self, environment):
        param=np.random.randint(10)
        background=environment.resource_field
        i=self.get_pos()[0]
        j=self.get_pos()[1]
        if param>background[i, j]:
            return True
        if param<=background[i, j]:
            return False
    
    def random_update(self, L):
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
    
    def resourcedriven_update(self, environment):
        background=environment.resource_field
        L=len(background)
        
        if self.x<1:
            self.x=self.x+L-1
        if self.y<1:
            self.y=self.y+L-1
        if self.x>=L-1:
            self.x=self.x-L+1
        if self.y>=L-1:
            self.y=self.y-L+1
        
        i=self.get_pos()[0]
        j=self.get_pos()[1]
        
        denom=background[i+1, j]+background[i-1, j]+background[i, j+1]+background[i, j-1]
        probabilities=np.array([background[i+1, j], background[i-1, j], background[i, j+1], background[i, j-1]])/denom
        options=[np.array([i+1, j]), np.array([i-1, j]), np.array([i, j+1]), np.array([i, j-1])]
        new_pos=self.choose_element(options, probabilities)
        self.x=new_pos[0]
        self.y=new_pos[1]

    def get_resource(self, environment):
        i=self.get_pos()[0]
        j=self.get_pos()[1]
        
        if environment.resource_field[i, j]>1:
            self.stored_resource+=1
            environment.subtract_resource(i, j)
            
