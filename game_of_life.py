import numpy as np
import matplotlib.pylab as plt
from matplotlib import animation
import random
import os, sys
import copy

class GameOfLife:

    def __init__(self, nx_universe, ny_universe, nx, ny):


        # initialize figure for grid animation #
        self.figure, self.axes = plt.subplots()
        
        # grid dimensions #
        self.nx_universe = nx_universe
        self.ny_universe = ny_universe
        self.nx = nx
        self.ny = ny

        # universe initialization: nx x ny matrix #
        self.universe = np.zeros((nx_universe, ny_universe))
        
        # first generation: random matrix with dimnension nx < nx_universe; ny < ny_universe #
        self.first_generation = np.random.randint(0, 2, size=(nx,ny))

        self.im = plt.imshow(self.first_generation, cmap="gray_r", interpolation="none", vmin=0, vmax=1)

    def first_generation_init(self):
        
        self.im.set_data(self.first_generation)
        return [self.im]
        

    def generation_evolution(self, generation):

        evolution = self.im.get_array()

        # Previous evolution #
        evolution_prev = copy.copy(evolution)
        
        for i in range(self.nx):
            for j in range(self.ny):

                cell_coord = (i, j)
                cell_status = self.cell_evolution(i, j, evolution_prev)

                evolution[cell_coord] = cell_status
                
        print("Generation: "+str(generation+1))
        print(evolution)

        print("")
 
#        print(evolution, generation)
        self.im.set_array(evolution)
        
        return [self.im]
         
    def cell_evolution(self, i, j, evolution):

        """ Gives as result if a cell is alive or dead based on the Conway's rules 

        Parameters
        ----------

        i: int
        first cell coordinate

        j: int
        second cell coordinate
        
        cell: int
        value of the cell for that evolution

        Returns
        -------

        cell_status : int (0 or 1)
        The status of a cell 1 (for alive) 0 (for dead)

        """

        cell_coord = (i,j)
        neighbours_cells = self.eight_connected_neighbours(i, j)

        neighbours_cells_status = [evolution[coord] for coord in neighbours_cells]
        alive_cells = int(sum(map(lambda x : x==1, neighbours_cells_status)))
        
        if(evolution[cell_coord] == 1):
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation #
            if(alive_cells<2):
                cell_status = 0

            # Any live cell with two or three live neighbours lives on to the next generation #
            elif(alive_cells==2 or alive_cells==3):
                cell_status = 1

            # Any live cell with more than three live neighbours dies, as if by overpopulation #
            elif(alive_cells>3):
                cell_status = 0
                
        else:
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction #
            if(alive_cells==3):
                cell_status = 1
            # In all the other cases the dead cell remain dead #
            else:
                cell_status = 0
            
        print(cell_coord, alive_cells, cell_status)
        return cell_status

    def eight_connected_neighbours(self, x, y ):
        """The x- and y- components for a single cell in an eight connected grid
        
        Parameters
        ----------
        
        x : int
        The x- position of cell to find neighbours of
        
        y : int 
        The y- position of cell to find neighbours of
        
        Returns
        -------
        results : list of tuple
        A list of (x, y) indices for the neighbours    
        """

        results = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                newx = x+dx
                newy = y+dy
                if(dx == 0 and dy == 0):
                    continue
                if(newx>=0 and newx<self.nx and newy >=0 and newy<self.ny):
                    results.append((newx, newy))
                

        return results
    
    
    
    def make_animation(self):

        ani = animation.FuncAnimation(self.figure, self.generation_evolution, init_func=self.first_generation_init, frames=10, interval=400, blit=True, repeat=False)
        plt.show()
       
if __name__ == "__main__":


    nx_universe = 100
    ny_universe = 100
    nx = 4
    ny = 4

    
    GameOfLife = GameOfLife(nx, ny)
    GameOfLife.make_animation()



    
