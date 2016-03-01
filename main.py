from box import *
from particle import *
from kernels import *


# create a box
dt = 1
box = Box(10, 100, dt)
# create the initial conditions
box.initial_conditions()
box.print_positions()
tFinal = 100
nSteps = int(tFinal/dt)
# main time loop
for ii in range(nSteps):
    box.update_particles()
    box.plot_particles()
    
box.print_positions()

