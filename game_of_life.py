import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
from matplotlib import animation
import random
import os, sys
import copy

class GameOfLife:

    def __init__(self, nx_universe, ny_universe, nx, ny):


        # initialize figure for animation #
        self.figure, (self.ax1, self.ax2) = plt.subplots(2,1, gridspec_kw={'height_ratios': [1, 5]})
        
        self.total_population_line, = self.ax1.plot([], [], c="k", lw=2)

        self.ax1.set_ylabel("Population")
        self.ax1.set(xlim=(0,1), ylim=(0,100))
        
        self.ax1.grid()
        self.ax2.grid()

        #manager = plt.get_current_fig_manager()
        #manager.full_screen_toggle()

        plt.axis('off')

        cmap_personal = "Greys_r" #cm.get_cmap('Greys_r', 2)
        
        
        # grid dimensions #
        self.nx_universe = nx_universe
        self.ny_universe = ny_universe
        self.nx = nx
        self.ny = ny

        # universe initialization: nx_universe x ny_universe matrix #
        self.universe = np.zeros((nx_universe, ny_universe))
        
        # initial_automa: random matrix with dimnension nx < nx_universe; ny < ny_universe #
        self.initial_automa = np.random.randint(0, 2, size=(nx,ny))

        self.first_generation = self.matrix_padding(self.universe, self.initial_automa, int(self.nx_universe/2), int(self.ny_universe/2))
        self.im = plt.imshow(self.first_generation, cmap=cmap_personal, interpolation="none", vmin=0, vmax=1)


        self.counter_list = []
        self.total_population_list = []
        self.alive_cells_list = []
        self.dead_cells_list = []
        self.evolutions_list = []
        
    def matrix_padding(self, A, B, r, c):

        """
        ----------
        Parameters
        ----------

        A : np.array
        larger matrix 

        B: np.array
        smaller matrix to insert in the larger one

        r: int
        first index of the position of the left-hand corner of B in A

        c: int
        second index of the position of the left-hand corner of B in A
T        
        -------
        Returns
        -------

        np.array
        the matrix A "merged" with matrix B

        """
        
        A[r:r+B.shape[0], c:c+B.shape[1]] += B

        return A
        
    def first_generation_init(self):

        self.im.set_data(self.first_generation)

        return [self.im]
        

    
    def generation_evolution(self, generation):

        n_generation = int(len(self.evolutions_list))

        self.ax1.set(xlim=(0,len(self.evolutions_list)+10), ylim=(0,100))        

        self.ax1.set_title("Generation: {}".format(n_generation))
        
        evolution = self.im.get_array()
        self.ax1.set(xlim=(0,len(self.evolutions_list)+10), ylim=(0,np.sum(generation)+50))        

        # Previous evolution #
        evolution_prev = copy.copy(evolution)

        for i in range(self.nx_universe):
            for j in range(self.ny_universe):
                
                cell_coord = (i, j)
                cell_status = self.cell_evolution(i, j, evolution_prev)
        
                evolution[cell_coord] = cell_status
                
        print("Generation: "+str(generation+1))

        self.evolutions_list.append(evolution)
        if(np.sum(evolution) == 0):
            print("Life ended at generation "+str(generation+1)+"\n")
            quit()

        self.counter_list.append(generation+1)

        
        self.total_population_list.append(int(np.sum(evolution)))
        
        self.total_population_line.set_data(self.counter_list, self.total_population_list)        
        self.im.set_data(evolution)

        return [self.im], self.total_population_line

    def generative_evolution_graph(self, generation):
    
        pass
    
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


        return cell_status

    def eight_connected_neighbours(self, x, y):
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
                if(newx>=0 and newx<self.nx_universe and newy >=0 and newy<self.ny_universe):
                    results.append((newx, newy))
                

        return results
    
    
    def make_animation(self):

        ani = animation.FuncAnimation(self.figure, self.generation_evolution, init_func=self.first_generation_init, frames=100, interval=50, blit=False, repeat=False)

#        plt.title("Generation: "+str(n_generation))
        plt.show()

if __name__ == "__main__":


    nx_universe = 100
    ny_universe = 100
    nx = 10
    ny = 10

    
    GameOfLife = GameOfLife(nx_universe, ny_universe, nx, ny)
    GameOfLife.make_animation()
#    GameOfLife.make_graph()



    
