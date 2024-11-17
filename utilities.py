import os
import subprocess

def clear_screen():
    clear_command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run([clear_command])

def load_level(filename): # Function that loads the game level from a file
    with open(filename, 'r') as file:
        num_rows = int(file.readline().strip())  # Read the number of rows
        num_moves = int(file.readline().strip())  # Read the number of available moves
        grid = [list(file.readline().strip()) for _ in range(num_rows)]  # Read the grid layout
    return grid, num_moves  # Return the grid and the number of moves

def display_grid(grid): # Function that displays the game grid
    for row in grid:
        print(''.join(row))
    print()

def update_leaderboard(name, score): # Function that updates the leaderboard.txt file
    with open("leaderboard.txt", 'a') as file:
        file.write(f"{name}: {score}\n")