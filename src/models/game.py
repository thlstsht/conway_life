from functools import reduce
from copy import deepcopy
from time import sleep
from models.board import Board
from helpers.console import clear_console

class Game:
    def __init__(self, seed):
        self.board   = Board(seed)
        self.is_over = False

        print(f'\nStarted game with seed:\n{self.board}\n')
    
    def play(self):
        generation = 0

        while not self.is_over:
            sleep(1)

            self.tick()
            generation += 1

            clear_console()
            print(f'\rGeneration {generation}:\n{self.board}\n', flush=True)
        
        print('Game over')
        exit()
    
    def tick(self):
        new_distribution = [[None for x in range(self.board.width)] for y in range(self.board.height)]
        
        for y, row in enumerate(self.board.cells):
            for x, cell in enumerate(row):
                new_distribution[y][x] = int(self.cell_becomes_alive(cell, self.board))
        self.board.load(new_distribution)

        if self.board.is_empty():
            self.is_over = True
    
    def cell_becomes_alive(self, cell, board):
        """
        Any live cell with fewer than two live neighbours dies.
        Any live cell with two or three live neighbours lives.
        Any live cell with more than three live neighbours dies.
        Any dead cell with exactly three live neighbours becomes alive.
        """
        alive_neighbors = board.count_alive_neighbors(cell)

        return alive_neighbors == 3 \
           or (alive_neighbors == 2 and cell.is_alive)