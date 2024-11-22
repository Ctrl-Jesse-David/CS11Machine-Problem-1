from utilities import display_grid, clear_screen
import time


'''
Main Algorithm Moving Algorithm:
    create a temporary grid
    store the updates on the grid in its temporary state
    run the temp grid in is_valid_grid
    change the final grid to the temporary gird's state if True
    loop til the is_valid_grid function returns False

'''

wall = '🧱'
egg = '🥚'
grass = '🟩'
empty_nest = '🪹'
full_nest = '🪺'
frying_pan = '🍳'


def is_valid_grid(grid): # Function that checks the validituy of the temporary grd
    for row in grid:
        if wall not in row:
            continue
    return True

def move_eggs(grid, direction):  # Main egg-moving logic
    score_change = 0

    movement_offsets = {
        'L': (0, -1),
        'R': (0, 1),
        'F': (-1, 0),
        'B': (1, 0)
    }

    row_offset, column_offset = movement_offsets[direction]

    while True:
        temp_grid = [row[:] for row in grid]  # Creates a copy of the grid
        movement_occurred = False
        egg_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == egg]

        for egg_row, egg_column in egg_positions:
            new_row = egg_row + row_offset
            new_column = egg_column + column_offset

            # Main conditionals
            if new_row < 0 or new_row >= len(grid) or new_column < 0 or new_column >= len(grid[0]):
                continue
            elif temp_grid[new_row][new_column] == wall or temp_grid[new_row][new_column] == full_nest:
                continue
            elif temp_grid[new_row][new_column] == empty_nest:
                temp_grid[new_row][new_column] = full_nest
                temp_grid[egg_row][egg_column] = grass
                score_change += 10
                movement_occurred = True
            elif temp_grid[new_row][new_column] == frying_pan:
                temp_grid[egg_row][egg_column] = grass
                score_change -= 5
                movement_occurred = True
            elif temp_grid[new_row][new_column] == grass:
                temp_grid[new_row][new_column] = egg
                temp_grid[egg_row][egg_column] = grass
                movement_occurred = True

        if is_valid_grid(temp_grid):
            grid[:] = temp_grid  # Update the og grid with the valid temporary grid
            clear_screen()
            display_grid(grid)
            time.sleep(0.1)
        else:
            break

        if not movement_occurred:
            break
    return score_change
