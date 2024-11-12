import os
import subprocess

def clear_screen():
    clear_command = 'cls' if os.name == 'nt' else 'clear'  # Determine command based on OS
    subprocess.run([clear_command])  # Execute the command to clear the screen

# Function to load the game level from a file
def load_level(filename):
    with open(filename, 'r') as file:
        num_rows = int(file.readline().strip())  # Read the number of rows
        num_moves = int(file.readline().strip())  # Read the number of available moves
        grid = [list(file.readline().strip()) for _ in range(num_rows)]  # Read the grid layout
    return grid, num_moves  # Return the grid and the number of moves

# Function to display the game grid
def display_grid(grid):
    for row in grid:
        print(''.join(row))  # Print each row of the grid as a string
    print()

def update_leaderboard(name, score):
    with open("leaderboard.txt", 'a') as file:
        file.write(f"{name}: {score}\n")