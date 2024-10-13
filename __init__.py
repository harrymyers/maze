import pygame
import sys

# Initialize pygame
pygame.init()

# Define constants for the screen
SCREEN_WIDTH = 800  # Width of the window
SCREEN_HEIGHT = 600  # Height of the window
CELL_SIZE = 20  # Size of each cell in the maze
ROWS = SCREEN_HEIGHT // CELL_SIZE  # Number of rows
COLS = SCREEN_WIDTH // CELL_SIZE   # Number of columns


# Set up the display (create a window)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Maze Generation and Solving")

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Define colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (20, 148, 20)

def draw_grid():
    for row in range(ROWS):
        pygame.draw.line(screen, GREEN, (0, row * CELL_SIZE), (SCREEN_WIDTH, row * CELL_SIZE))
    for col in range(COLS):
        pygame.draw.line(screen, GREEN, (col * CELL_SIZE, 0), (col * CELL_SIZE, SCREEN_HEIGHT))

# Main loop
running = True
while running:
    # Handle events like closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 frames per second)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
