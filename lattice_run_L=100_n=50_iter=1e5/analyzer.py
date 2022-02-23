import numpy as np
import matplotlib.pyplot as plt
import math
import os

path=os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(path,'rundata.npy')
print("Reading", filename)
rundata=np.load(filename, allow_pickle=True)

L=rundata[0]
t=rundata[1]
disc=1
densitydata=rundata[2][disc:L-disc,disc:L-disc]/t
movedata=rundata[3]
popdata=rundata[4]
timedata=np.arange(t)
rt=len(movedata)
rtimedata=np.arange(rt)
staterror=1/np.sqrt(popdata)

densitymap=plt.figure(1)
plt.imshow(densitydata)
plt.colorbar()
plt.title('Density Map')
plt.savefig(os.path.join(path,'densitymap.png'))

densityhist=plt.figure(2)
plt.hist((densitydata).ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.title('Density Histogram')
plt.savefig(os.path.join(path,'densityhist.png'))

moveplot=plt.figure(3)
plt.plot(rtimedata, movedata, "k.")
plt.title('Movement Probability')
plt.xlabel('Time (t)')
plt.ylabel('Probability of Movement')
#plt.errorbar(rtimedata, movedata, yerr=movedata*staterror, )
plt.savefig(os.path.join(path,'moveplot.png'))

movehist=plt.figure(4)
plt.hist(movedata, bins=20, fc='k', ec='k')
plt.title('Movement Probability Histogram')
plt.xlabel('Probability of Movement per Iteration')
plt.ylabel('Frequency')
#plt.errorbar(rtimedata, movedata, yerr=movedata*staterror, )
plt.savefig(os.path.join(path,'movehist.png'))

popplot=plt.figure(5)
plt.plot(rtimedata, popdata, "k.")
plt.title('Population History')
plt.xlabel('Time (t)')
plt.ylabel('Population')
plt.yscale('log')
plt.savefig(os.path.join(path,'popplot.png'))