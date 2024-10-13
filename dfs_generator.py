import pygame
import random
from maze import Maze

def depth_first_search(maze, row, col, screen, draw):
    # Mark the current cell as visited
    maze.mark_visited(row, col)
    
    # Get the unvisited neighbors of the current cell
    neighbors = maze.get_neighbors(row, col)
    random.shuffle(neighbors)  # Shuffle to randomize path selection

    # Recursively visit each unvisited neighbor
    for direction, next_row, next_col in neighbors:
        if not maze.grid[next_row][next_col].visited:
            # Remove the wall between the current cell and the neighbor
            maze.remove_walls((row, col), (direction, next_row, next_col))

            # Draw the current state of the maze
            draw()

            # Recursively apply DFS to the neighbor
            depth_first_search(maze, next_row, next_col, screen, draw)

def generate_maze_with_dfs(maze, screen, draw):
    # Pick a random starting point for the maze generation
    start_row = random.randint(0, maze.rows - 1)
    start_col = random.randint(0, maze.cols - 1)

    # Start the DFS algorithm from the random starting point
    depth_first_search(maze, start_row, start_col, screen, draw)
