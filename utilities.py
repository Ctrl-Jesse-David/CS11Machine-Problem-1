import os
import subprocess

def clear_screen():
    """ Clears the terminal screen """
    clear_command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run([clear_command])

def load_level(filename):
    ''' Loads the game level data from a file wcich reads the number of rows, available moves, and the grid layout '''
    with open(filename, 'r') as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves 

def display_grid(grid):
    """ Displays a 2d representation of the game layout grid in the terminal """
    for row in grid:
        print(''.join(row))
    print()

def update_leaderboard(name, score):
    """ Updates the leaderboard file with the player's name and score """
    with open("leaderboard.txt", 'a') as file:
        file.write(f"{name}: {score}\n")

def process_moves(input_str):
    """ Validates the player's input moves """
    valid_moves = [c for c in input_str.upper() if c in 'LRFBEU']
    if not valid_moves:
        return "No valid moves found"
    return valid_moves
