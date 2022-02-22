#This file carries out the simulation, with a given number of agents in the environment background of size L. This is currently incomplete.

#Define the parameters for the model run. 
###
n_agents=10
L=50
iter=int(1e4)
productivity=True
reducedlength=1000
###

import numpy as np
import matplotlib.pyplot as plt
import os
from classes import agent
from classes import environment

#Instantiate the environment
environment=environment(L)

#Creates a list of instantiations of the agent class. This forms the population.
agentlist=list()
for agentnumber in range(n_agents):
    agentlist.append(agent(L))

#Defines position and move history data objects
history=np.zeros((L, L))
movehistory=np.zeros(iter)
populationdata=np.zeros(iter)

#Total iteration loop
for step in range(iter):
    movecount=0
    occupancydata=np.zeros((L, L))
    #Iterates through list of agents
    for agentnumber in range(n_agents):
        #Check to see if agent has stored resources
        if agentlist[agentnumber].stored_resource >= 1:
            if agentlist[agentnumber].move_condition(environment) == True:
                #If agent has stored resources and move condition true, initiates move
                agentlist[agentnumber].resourcedriven_update(environment)
                movecount+=1
                agentlist[agentnumber].stored_resource-=1
        #Logs data
        occupancydata[agentlist[agentnumber].x, agentlist[agentnumber].y]+=1
        history[agentlist[agentnumber].get_pos()[0], agentlist[agentnumber].get_pos()[1]]+=1
        
        #Agent collects resource
        agentlist[agentnumber].get_resource(environment)
        
    #Population growth counter
    birthcount=0
        
    for agentnumber in range(n_agents):
        #Agent birth
        if n_agents<L**2:
            if agentlist[agentnumber].stored_resource > 2:
                if occupancydata[agentlist[agentnumber].x, agentlist[agentnumber].y]>=2:
                    newagent=agent(L)
                    newagent.x=agentlist[agentnumber].x
                    newagent.y=agentlist[agentnumber].y
                    newagent.stored_resource=1
                    agentlist.append(newagent)
                    birthcount+=1
                    
    n_agents+=birthcount
    deathcount=0
    for agentnumber in range(n_agents):
        #Agent death
        if agentlist[agentnumber].stored_resource < 1:
            agentlist[agentnumber]=None
            deathcount+=1
    
    agentlist=list(filter(None, agentlist))
    #Add population growth to n_agents
    n_agents-=deathcount


    #Logs move history data
    if n_agents>0:
        movehistory[step]=movecount/n_agents
    elif n_agents==0:
        movehistory[step]=0
    populationdata[step]=n_agents
    
    #Stochastic but homogeneous ecological productivity
    if productivity==True:
        param=np.random.randint(100)
        if param<=1:
            environment.resource_field+=1

#Data reduction step
reducedmovehistory=np.zeros(reducedlength)
reducedpopulationdata=np.zeros(reducedlength)

for i in range(reducedlength):
    moveavg=np.mean(np.split(movehistory, reducedlength)[i])
    reducedmovehistory[i]=moveavg
    popavg=np.mean(np.split(populationdata, reducedlength)[i])
    reducedpopulationdata[i]=popavg
    
data=np.array([n_agents, L, history, reducedmovehistory, reducedpopulationdata], dtype=object)
np.save(os.path.join(os.getcwd(), "rundata.npy"), data)

print("Run Complete")