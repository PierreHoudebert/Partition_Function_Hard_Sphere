# Partition_Function_Hard_Sphere
Computation of the partition function of the (continuum) hard-sphere model

by Pierre Houdebert

This simple code compute the partition function of the continuum hard-sphere model. A formal definition of this model can be found for instance in 

Christoph Hofer-Temmel, Disagreement percolation for the hard-sphere model
https://arxiv.org/abs/1507.02521
https://projecteuclid.org/euclid.ejp/1568080871

the parameters are
-dim : the dimension
-z : the intensity of the underlying Poisson point process
-lln : number of iteration in the law of large number computation approximating the partition function
-wdth_box : size of the square box
- radius : radius of exclusion of the model, ie two points can't be closer than radius
