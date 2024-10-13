import pygame
import sys
from maze import Maze
from dfs_generator import generate_maze_with_dfs

# Initialize Pygame
pygame.init()

# Define some constants
WIDTH, HEIGHT = 600, 600  # Screen dimensions
ROWS, COLS = 20, 20  # Maze grid size
CELL_SIZE = WIDTH // COLS  # Size of each cell

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation with DFS")

# Define colors
GREEN = (20, 148, 20)
BLACK = (0, 0, 0)

# Create the Maze object
maze = Maze(ROWS, COLS, CELL_SIZE)

def draw_grid(maze):
    screen.fill(BLACK)  # Fill the background with white

    for row in range(maze.rows):
        for col in range(maze.cols):
            cell = maze.grid[row][col]

            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Draw the walls for each cell
            if cell.north:
                pygame.draw.line(screen, GREEN, (x, y), (x + CELL_SIZE, y), 2)  # Top wall
            if cell.south:
                pygame.draw.line(screen, GREEN, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)  # Bottom wall
            if cell.east:
                pygame.draw.line(screen, GREEN, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)  # Right wall
            if cell.west:
                pygame.draw.line(screen, GREEN, (x, y), (x, y + CELL_SIZE), 2)  # Left wall

    pygame.display.update()  # Update the display after drawing the grid


def main():
    clock = pygame.time.Clock()

    # Define the draw function that calls the draw_grid and updates the display
    def draw():
        draw_grid(maze)
        pygame.display.update()
        clock.tick(60)  # Control the frame rate (optional)

    # Generate the maze with DFS and visualization
    generate_maze_with_dfs(maze, screen, draw)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Keep displaying the maze even after it's fully generated
        draw()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

