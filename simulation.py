#This file carries out the simulation, with a given number of agents in the environment background of size L. This is currently incomplete.

import numpy as np
import matplotlib.pyplot as plt
from agents import agent
from environment import environment
n_agents=10

L=10
environment=environment(L)

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

plt.scatter(xposdat, yposdat)
plt.axis('square')
plt.savefig('scatterplot_initial.pdf')
plt.matshow(environment.resource_field)
plt.savefig('environment_initial.pdf')
plt.show()