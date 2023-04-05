from models.cell import Cell

class Board:
    def __init__(self, distribution):
        self.height = len(distribution)
        self.width  = len(distribution[0])
        
        self.load(distribution)
    
    def load(self, distribution):
        self.distribution = distribution

        cells = [[None for x in range(self.width)] for y in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                cells[y][x] = Cell(x, y, bool(distribution[y][x]))
        self.cells = cells
    
    def is_empty(self):
        for row in self.cells:
            for cell in row:
                if cell.is_alive:
                    return False
        
        return True

    def count_alive_neighbors(self, cell):
        count = 0

        for y in range(cell.y - 1, cell.y + 2):
            for x in range(cell.x - 1, cell.x + 2):
                try:
                    if x == cell.x and y == cell.y:
                        continue

                    count += self.distribution[y][x]
                except IndexError:
                    continue
        return count

    def __str__(self):
        return '\n'.join(
            ['  '.join([str(cell) for cell in row]) for row in self.cells]
        )