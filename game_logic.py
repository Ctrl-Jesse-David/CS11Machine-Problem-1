from main import clear_screen
from utilities import display_grid, load_level, update_leaderboard
from termcolor import cprint, colored
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

            if grid[new_row][new_column] == wall or grid[new_row][new_column] == full_nest:
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


def copy_grid(grid): # Copies the grid for the undo
    return [row[:] for row in grid]


# Main game loop
def start_game(filename):
    from main import main_menu
    grid, num_moves = load_level(filename) # Unpack/Read level's file
    score = 0 # Score intializer
    all_eggs_in_nests = False # Egg's location tracker
    history = [] # Moves history for [U]ndo
    moves = [] # For moves history

    while num_moves > 0 and not all_eggs_in_nests:
        # Length of header and footer should be dependent on the size of the column of the gird
        clear_screen()
        print("=======================================================")
        cprint("              🍳 Egg Roll Challenge 🍳", "blue", attrs = ["bold"])
        print("=======================================================\n")
        display_grid(grid)
        print("-------------------------------------------------------")
        print(colored("🔢 MOVES LEFT  ", "blue") + f" : {num_moves}")
        print(colored("🌟 SCORE       ", "blue") + f" :  {score}")
        print(colored("🎯 PREV MOVE   ", "blue") + f" :  {moves}")
        print("-------------------------------------------------------")
        move = input("Enter move " + colored("(L/R/F/B)", "blue", attrs = ["bold"]) 
                     + ", " + colored("[U]", "blue", attrs = ["bold"]) + "ndo, or " 
                     + colored("[E]", "blue", attrs = ["bold"]) + "xit: ").upper()
        print("-------------------------------------------------------")

        if move == 'U' and history:
            grid, num_moves, score = history.pop()
            continue
        elif move == 'E':  # Handle exit here
            while True:
                double_check = input("Are you sure you'd like to exit the game [Y/N]: ").upper()
                if double_check == "Y":
                    main_menu()  # Go to main menu if they confirm exit
                    return
                elif double_check == "N":
                    break  # Exits the confirmation loop and continue the game
                else:
                    cprint("Invalid response!", "red", attrs=["bold"])
                    time.sleep(1)
            continue  # Skip calling move_eggs for exit move
        elif move not in ['L', 'R', 'F', 'B']:
            print("Invalid move! Try again.")
            time.sleep(1)
            continue

        history.append((copy_grid(grid), num_moves, score))
        add_score, all_eggs_in_nests = move_eggs(grid, move)
        score += add_score
        num_moves -= 1
    
    clear_screen()
    if all_eggs_in_nests:
        score += num_moves # Add remaining moves after the game
        print("=======================================================")
        cprint("            🎉🎉 CONGRATULATIONS! 🎉🎉", "green", attrs = ["bold"])
        print("=======================================================")
        cprint("   🏆🏅 All eggs safely rolled into their nests! 🏅🏆", attrs = ["bold"])
        print("-------------------------------------------------------")
        print(colored("🏆 FINAL SCORE: ", "green", attrs = ["bold"]) + f" {score} 🏆")
        print("-------------------------------------------------------\n")
    else:
        print("=======================================================")
        cprint("              💥😞 You lost! 💥😞 ", "red", attrs = ["bold"])
        print("=======================================================\n")
        cprint("              better luck next time!", attrs = ["bold"])
        print("-------------------------------------------------------")
        print(colored("🏆 FINAL SCORE: ", "red", attrs = ["bold"]) + f" {score} 🏆")
        print("-------------------------------------------------------\n")

    display_grid(grid)
    print("-------------------------------------------------------")

    # To store name on Leaderboard
    name = input("Enter your name: ")
    update_leaderboard(name, score)

    while True: # Asking user after the game
        retry_option = input("Retry [R] or Main Menu [M]? ").upper()
        if retry_option == 'R':
            start_game(filename)
            break
        elif retry_option == 'M':
            main_menu()
            break
        else:
            cprint("Invalid response!", "red", attrs = ["bold"])
            time.sleep(1)
            continue

        
