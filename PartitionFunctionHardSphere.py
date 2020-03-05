import numpy as np

#by Pierre Houdebert
#Computation of the partition function of the (continuum) HardS-Phere model
# on a square box

dim = 2  #dimension
z = 1 #intensity of the PPP
lln = 100000 #number of time we are doing the experiment
wdth_box = 1   #size of the box
radius = 1 # radius of exclusion (two points can't be closer than radius)

poi = np.random.poisson(z*(wdth_box ** dim),lln);
conf = wdth_box * np.random.rand(lln,max(poi),dim) # we have lln configurations (some contains too much points)

BoundaryConf = np.array([ [wdth_box , wdth_box/2 ]  ] )

D1 = np.full(lln,False)

for i in range(0,lln):
    j = 0
    while (D1[i] == False) & (j<np.size(BoundaryConf,axis=0)):
        D1[i] = True in (np.linalg.norm(conf[i,0:poi[i],:] - BoundaryConf[j,:],axis=1) <= radius)
        j = j+1
    #print(D1)
    
    j=0
    while (D1[i] == False) & (j<poi[i]):
        D = (np.linalg.norm( conf[i,j+1:poi[i],:] - conf[i,j,:],axis=1 ) ) <= radius
        D1[i] = True in D
        j = j+1

PartitionFunction = np.sum(1-D1)
print(PartitionFunction)

#print(np.linalg.norm(conf[0,0,:]))