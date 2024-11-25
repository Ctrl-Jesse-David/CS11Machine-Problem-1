from utilities import display_grid, clear_screen
import time



''' This section contains all the game constants '''
wall = '🧱'
egg = '🥚'
grass = '🟩'
empty_nest = '🪹'
full_nest = '🪺'
frying_pan = '🍳'


def move_eggs(grid, direction):
    ''' Returns the score_change after a move from the player '''

    score_change = 0

    ''' Creates a dictionary of offsets which will be added to the original index '''
    movement_offsets = {
        'L': (0, -1),
        'R': (0, 1),
        'F': (-1, 0),
        'B': (1, 0)
    }

    row_offset, column_offset = movement_offsets[direction]

    ''' Creates an infinite loop for the grid's movement '''
    while True:
        egg_moved = False

        # Find all egg positions
        egg_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == egg]

        for egg_row, egg_column in egg_positions:
            new_row = egg_row + row_offset
            new_column = egg_column + column_offset

            # Check if the new position is out of bounds
            if new_row < 0 or new_row >= len(grid) or new_column < 0 or new_column >= len(grid[0]):
                continue

            # Handle movement based on cell type
            if grid[new_row][new_column] == wall or grid[new_row][new_column] == full_nest:
                continue
            elif grid[new_row][new_column] == empty_nest:
                grid[new_row][new_column] = full_nest
                grid[egg_row][egg_column] = grass
                score_change += 10
                egg_moved = True
            elif grid[new_row][new_column] == frying_pan:
                grid[egg_row][egg_column] = grass
                score_change -= 5
                egg_moved = True
            elif grid[new_row][new_column] == grass:
                grid[new_row][new_column] = egg
                grid[egg_row][egg_column] = grass
                egg_moved = True

        clear_screen()
        display_grid(grid)
        time.sleep(0.1)

        if not egg_moved:
            break

    return score_change
