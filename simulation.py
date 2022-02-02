#This file carries out the simulation, with a given number of agents in the environment background of size L. This is currently incomplete.

import numpy as np
import matplotlib.pyplot as plt
from agents import agent
from environment import environment

n_agents=100
L=1000
iter=10000


environment=environment(L)

n_agents=100
agentlist=list()
for i in range(n_agents):
    agentlist.append(agent(L))

poslist=list()
for i in range(n_agents):
    poslist.append(agentlist[i].get_pos())

xposdat=np.zeros(n_agents)
yposdat=np.zeros(n_agents)
for i in range(n_agents):
    xposdat[i]=poslist[i][0]
    yposdat[i]=poslist[i][1]

history=np.zeros((L, L))
for step in range(iter):
    for i in range(n_agents):
        agentlist[i].pos_update()
        history[agentlist[i].get_pos()[0], agentlist[i].get_pos()[1]]+=1
        
plt.matshow(history)
plt.show()