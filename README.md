# Conways Game of Life

The Game of Life, often referred to as Life, is a cellular automaton created by British mathematician John Horton Conway in 1970. This zero-player game evolves based on its initial state without any additional input. Users engage with the Game of Life by setting up an initial configuration and watching its progression. Notably, it is Turing complete, meaning it can simulate a universal constructor or any other Turing machine.

This is a two-dimensional Python version with grid of square cells, where each cell is either live or dead (populated or unpopulated). Each cell interacts with its eight neighbors, which are the cells directly adjacent horizontally, vertically, or diagonally. The transitions at each step in time are as follows:

    1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    2. Any live cell with two or three live neighbors survives to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial configuration is the seed of the system. The first generation is formed by simultaneously applying these rules to every cell in the seed, regardless of whether it is live or dead. Births and deaths happen simultaneously at each discrete moment, sometimes referred to as a tick. Each generation is derived solely from the previous one, with the rules being applied repeatedly to generate subsequent generations.
