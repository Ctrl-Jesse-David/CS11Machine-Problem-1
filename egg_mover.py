from utilities import display_grid, clear_screen
import time

wall = '🧱'
egg = '🥚'
grass = '🟩'
empty_nest = '🪹'
full_nest = '🪺'
frying_pan = '🍳'


def move_eggs(grid, direction): # Egg main moving logic
    score_change = 0
    movement_occurred = True

    movement_offsets = {
        'L': (0, -1),
        'R': (0, 1),
        'F': (-1, 0),
        'B': (1, 0)
    }
    row_offset, column_offset = movement_offsets[direction]

    while movement_occurred:
        movement_occurred = False
        new_positions = {}

        egg_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == egg]

        for egg_row, egg_column in egg_positions:
            new_row = egg_row + row_offset
            new_column = egg_column + column_offset

            if new_row < 0 or new_row >= len(grid) or new_column < 0 or new_column >= len(grid[0]):
                continue

            elif grid[new_row][new_column] == wall or grid[new_row][new_column] == full_nest:
                new_positions[(egg_row, egg_column)] = (egg_row, egg_column)
            elif grid[new_row][new_column] == empty_nest:
                grid[new_row][new_column] = full_nest
                grid[egg_row][egg_column] = grass
                score_change += 10
                movement_occurred = True
            elif grid[new_row][new_column] == frying_pan:
                grid[egg_row][egg_column] = grass
                score_change -= 5
                movement_occurred = True
            elif grid[new_row][new_column] == grass:
                new_positions[(egg_row, egg_column)] = (new_row, new_column)
                movement_occurred = True

        for (old_row, old_column), (new_row, new_column) in new_positions.items():
            if (old_row, old_column) != (new_row, new_column):
                grid[old_row][old_column] = grass
                grid[new_row][new_column] = egg

        clear_screen()
        display_grid(grid)
        time.sleep(0.1)

        if all(grid[r][c] == full_nest for r, c in egg_positions):
            return score_change, True

    return score_change, False