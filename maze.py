# maze.py

class Cell:
    def __init__(self):
        # Each cell starts with all walls intact
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.visited = False  # Initially, the cell is unvisited

    def __repr__(self):
        return f"Cell(N: {self.north}, S: {self.south}, E: {self.east}, W: {self.west}, Visited: {self.visited})"

class Maze:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]  # Create a grid of cells

    def get_neighbors(self, row, col):
        neighbors = []
        
        # Check north neighbor
        if row > 0 and not self.grid[row - 1][col].visited:
            neighbors.append(('north', row - 1, col))
        
        # Check south neighbor
        if row < self.rows - 1 and not self.grid[row + 1][col].visited:
            neighbors.append(('south', row + 1, col))
        
        # Check east neighbor
        if col < self.cols - 1 and not self.grid[row][col + 1].visited:
            neighbors.append(('east', row, col + 1))
        
        # Check west neighbor
        if col > 0 and not self.grid[row][col - 1].visited:
            neighbors.append(('west', row, col - 1))

        return neighbors

    def remove_walls(self, current_cell, next_cell):
        # Remove walls between two adjacent cells
        direction, row, col = next_cell

        if direction == 'north':
            self.grid[current_cell[0]][current_cell[1]].north = False
            self.grid[row][col].south = False

        elif direction == 'south':
            self.grid[current_cell[0]][current_cell[1]].south = False
            self.grid[row][col].north = False

        elif direction == 'east':
            self.grid[current_cell[0]][current_cell[1]].east = False
            self.grid[row][col].west = False

        elif direction == 'west':
            self.grid[current_cell[0]][current_cell[1]].west = False
            self.grid[row][col].east = False

    def mark_visited(self, row, col):
        # Mark the cell as visited
        self.grid[row][col].visited = True

