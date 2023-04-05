class Cell:
    def __init__(self, x, y, is_alive):
        self.x        = x
        self.y        = y
        self.is_alive = is_alive
    
    def __str__(self):
        return '1' if self.is_alive else '0'