import numpy as np

#by Pierre Houdebert
#Computation of the partition function of the (continuum) HardS-Phere model
# on a square box

#dim        dimension
#z          intensity of the PPP
#lln        number of time we are doing the experiment
#wdth_box   size of the hexagon
#radius     radius of exclusion (two points can't be closer than radius)
#BoundaryConf 

def PartitionFunction_Hexa (dim,z,lln,wdth_box,radius,BoundaryConf):
    poi = np.random.poisson(z*((2*wdth_box) ** dim),lln)
    pre_conf = (3 * wdth_box * np.random.rand(lln,max(poi),dim)) - wdth_box
    
    
    # we have lln configurations (some contains too much points)
    
    
    
   # D1 = np.full(lln,False)
    
    #for i in range(0,lln):
     #   j = 0
     #   while (D1[i] == False) & (j<np.size(BoundaryConf,axis=0)):
     #       D1[i] = True in (np.linalg.norm(conf[i,0:poi[i],:] - BoundaryConf[j,:],axis=1) <= radius)
     #       j = j+1
            
     #   j=0
    #    while (D1[i] == False) & (j<poi[i]):
    #        D = (np.linalg.norm( conf[i,j+1:poi[i],:] - conf[i,j,:],axis=1 ) ) <= radius
     #       D1[i] = True in D
    #        j = j+1
        
    #result = np.sum(1-D1)
    #return result;
    return pre_conf;

print(PartitionFunction_Hexa(2,1,2,1,1,np.array([])))
