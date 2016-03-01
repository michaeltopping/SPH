# the class that will hold the box for the simulation
from particle import *
from random import random
from kernels import *
import matplotlib.pyplot as plt

class Box:
    def __init__(self, length, nParticles, dt):
        self.length = length
        self.nParticles = nParticles
        self.particles = np.array([])
        self.dt = dt



    def initial_conditions(self):
        for ii in range(self.nParticles):
            pos = [(self.length*random())-.5*self.length for jj in range(3)]
            vel = [random()-.5 for jj in range(3)]
            self.particles = np.append(self.particles, Particle(1, pos, vel))
            

        # loop through each of the particles and find the densities
        for p in self.particles:
            rho = p.get_local_density(self.particles)


    def update_particles(self):
        # this is the the updated list of particles
        nextParticles = []

        # loop through all of the particles
        for p in self.particles:
            # update the position of the particle on the half step
            p.pos = p.pos + self.dt/2.*p.vel


            # find the acceleration
            accel = p.calculate_acceleration(self.particles)
            # update the velocity on the half step, so that we can calculate 
            #  the acceleration on the half step 
            velHalf = p.vel+self.dt/2.*accel

            # find the acceleration on the half step
            accelHalf = p.calculate_acceleration(self.particles)
            # update the velocity for the full step, using the half step 
            #  acceleration
            # we will need the old velocity to calculate the updated
            #  position
            oldvel = p.vel
            p.vel = p.vel + self.dt*accelHalf
            

            # now update the positions on the full step
            p.pos = p.pos+self.dt/2.*(oldvel+p.vel)



            # check the boundaries of the box
            p.check_boundaries(self.length)     


    

    # print the positions of all the particles
    def print_positions(self):
        for p in self.particles:
            print(p.pos)

    

    # plot the particle positions
    def plot_particles(self):
        plt.clf()
        for p in self.particles:
            plt.scatter(p.pos[0], p.pos[1])
        plt.xlim([-20,20])
        plt.ylim([-20,20])
        plt.show()
