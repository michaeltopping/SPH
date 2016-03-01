# this will be the class for the particle
from kernels import *
import numpy as np

class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.rho = 0
        self.h = 2


    # uses the SPH approximation to get the density at a particle
    def get_local_density(self, particles):
        # loop through all of the particles  
        rho = 0
        for p in particles:
            # check if its within the kernel range
            rho += p.mass*W(self.pos, p.pos, self.h)


        self.rho = rho
        return self.rho



    # this uses the equation of state to get the pressure at a particle
    def get_local_pressure(self):
        gamma = 5./3.
        return 1*self.rho**gamma
            



    # calculate the acceleration of the particle
    def calculate_acceleration(self, particles):

        # find the particles in the group within the kernel
        distances = np.array([np.sum( np.square(p.pos - self.pos) )**.5 for p in particles])
        groupIndices = np.where( ( distances < 2.*self.h ) )
        # remove the index for the self particle
        groupIndices = np.where( ( distances[groupIndices[0]] > 0))


        totalAccel = 0
        print("Group Indices:{}".format(groupIndices[0]))
        # loop through all of the particles in the group
        for p in particles[groupIndices[0]]:
            P = p.get_local_pressure()
            print("Pressure: {}".format(P))
            totalAccel += -(p.mass*(P/p.rho**2 + self.get_local_pressure()/self.rho**2)*gradW(self.pos, p.pos, self.h))

        print(totalAccel)
        totalAccel -= np.array([0,.01,0])
        return totalAccel




    # check the boundary conditions
    def check_boundaries(self, boxLength):
        # loop through the coordinates
        for ii in range(3):
            if self.pos[ii] > boxLength/2.:
                self.pos[ii] = boxLength/2.

            if self.pos[ii] < -boxLength/2.:
                self.pos[ii] = -boxLength/2.
