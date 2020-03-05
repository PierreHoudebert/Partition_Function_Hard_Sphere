import numpy as np

#by Pierre Houdebert
#Computation of the partition function of the (continuum) HardS-Phere model
# on a square box

#dim        dimension
#z          intensity of the PPP
#lln        number of time we are doing the experiment
#wdth_box   size of the box
#radius     radius of exclusion (two points can't be closer than radius)
#BoundaryConf 

def PartitionFunction (dim,z,lln,wdth_box,radius,BoundaryConf):
    poi = np.random.poisson(z*(wdth_box ** dim),lln)
    conf = wdth_box * np.random.rand(lln,max(poi),dim) 
    # we have lln configurations (some contains too much points)
    D1 = np.full(lln,False)
    
    for i in range(0,lln):
        j = 0
        while (D1[i] == False) & (j<np.size(BoundaryConf,axis=0)):
            D1[i] = True in (np.linalg.norm(conf[i,0:poi[i],:] - BoundaryConf[j,:],axis=1) <= radius)
            j = j+1
            
        j=0
        while (D1[i] == False) & (j<poi[i]):
            D = (np.linalg.norm( conf[i,j+1:poi[i],:] - conf[i,j,:],axis=1 ) ) <= radius
            D1[i] = True in D
            j = j+1
        
    result = np.sum(1-D1)
    return result;


dim = 2  #dimension
z = 0.167 #intensity of the PPP
lln = 300000 #number of time we are doing the experiment
wdth_box = 1 #2/np.sqrt(5)   #size of the box
radius = 1 # radius of exclusion (two points can't be closer than radius)

BoundaryConf = np.array([])
a = PartitionFunction(dim,z,lln,wdth_box,radius,BoundaryConf)

#BoundaryConf = np.array([ [wdth_box/2 , 0 ]  ] )
#b1 = PartitionFunction(dim,z,lln,wdth_box,radius,BoundaryConf)
BoundaryConf = np.array([ [wdth_box , 0 ],[0 , 0 ]  ] )
b = PartitionFunction(dim,z,lln,wdth_box,radius,BoundaryConf)

BoundaryConf = np.array([ [wdth_box , 0]  ] )
c = PartitionFunction(dim,z,lln,wdth_box,radius,BoundaryConf)

Dobru1 = 4*(1- b/a) + 4*(1- c/a) #+ 4*(1- d/a) + 8*(1- e/a)
print(Dobru1)


BoundaryConf = np.array([ [wdth_box/2 , 0 ]  ] )
b = PartitionFunction(dim,z,lln,wdth_box,radius,BoundaryConf)


Dobru0 = 4*(1- b/a) + 4*(1- c/a) #+ 4*(1- d/a) + 8*(1- e/a)
print(Dobru0)

#PartitionFunction(dim,z,lln,wdth_box,radius,BoundaryConf)