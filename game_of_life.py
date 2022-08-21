import numpy as np
import matplotlib.pylab as plt
#from matplotlib.animation import FuncAnimation
from matplotlib import animation
import random
import os, sys


class GameOfLife:

    def __init__(self, nx, ny):


        # initialize figure for grid animation #
        self.figure, self.axes = plt.subplots()
        
        # grid dimension: nx (horizontal); ny (vertical) #
        self.nx = nx
        self.ny = ny

        # all zeros matrix to initialize the grid: first generation #
        self.first_generation = np.random.randint(0, 2, size=(nx,ny))

        # list of generations #
        self.generations_list = []
        self.generations_list.append(self.first_generation)

        self.im = plt.imshow(self.first_generation, cmap="gray", interpolation="none", vmin=0, vmax=1, origin="lower")

    def first_generation_init(self):
        
        self.im.set_data(self.first_generation)
        return [self.im]
        
    def make_animation(self):

        ani = animation.FuncAnimation(self.figure, self.generation_evolution, frames=100, interval=200, blit=True, repeat=False)
        plt.show()

    def generation_evolution(self,i):

        evolution = self.im.get_array()
        evolution = np.random.randint(0, 2, size=(nx,ny))
        self.im.set_array(evolution)
        
        return [self.im]
        
        
if __name__ == "__main__":


    nx = 40
    ny = 40
    
    GameOfLife = GameOfLife(nx, ny)


    GameOfLife.make_animation()
    
    
