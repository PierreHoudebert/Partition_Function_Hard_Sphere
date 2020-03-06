import numpy as np
from math import pi

#by Pierre Houdebert
#Computation of the partition function of the (continuum) HardS-Phere model
# on a square box

#dim        dimension
#z          intensity of the PPP
#lln        number of time we are doing the experiment
#wdth_box   size of the hexagon
#radius     radius of exclusion (two points can't be closer than radius)
#BoundaryConf 

#even if there is a parameter dim, the code is written for dimension 2

def PartitionFunction_Hexa (dim,z,lln,radius,BoundaryConf):
    poi = np.random.poisson(z*(np.sqrt(3) * 2),lln)
    PartitionFunction = 0
    #print(poi)
    for i in range(lln):
        pre_conf = np.array([])
        #conf = np.empty_like( np.array([[1,2]])  )
        taille = 0
        for j in range(poi[i]):
            x = np.random.uniform(-0.5,1.5)
            y = np.random.uniform(0,np.sqrt(3))
            
            A = (x>=0) & (x<=1)
            B = (x<0) & (y >= -x * np.tan(pi/6)) & (np.sqrt(3) - y >= -x * np.tan(pi/6))
            C = (x>1) & (y >= (x-1) * np.tan(pi/6)) & (np.sqrt(3) - y >= (x-1) * np.tan(pi/6))
            
            if A|B|C:
                taille = taille  + 1
                pre_conf = np.append(pre_conf,np.array([x,y]))
            
        conf = np.zeros((taille,2))
        for j in range(taille):
            conf[j,0] = pre_conf[2*j]
            conf[j,1] = pre_conf[2*j+1]
            
        #the configuration is built (it is not at all a nice part...)
        #print(conf)
        
        k=0 
        Rep=False
        while (Rep == False) & (k < np.size(BoundaryConf,axis=0)):
            Rep = True in (np.linalg.norm(conf - BoundaryConf[k,:],axis=1) <= radius)
            k = k +1
            
        k = 0
        taille = np.size(conf,axis=0)
        while (Rep == False) & (k < taille):
            Rep = True in ( (np.linalg.norm( conf[k+1:taille,:] - conf[k,:],axis=1 ) ) <= radius)
            k =k+1
            
        #print(Rep)
        if Rep == False:
            PartitionFunction = PartitionFunction +1
    
    return PartitionFunction;

z = 0.17

a = PartitionFunction_Hexa (2,z,1000000,1,np.array([]))
print(a)

#b = PartitionFunction_Hexa (2,z,1000000,1,np.array( [[0.5,0]] ) )
#print(b)

#result = 6*(1 - b/a)
#print(result)
