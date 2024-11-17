from main import clear_screen
from utilities import display_grid, load_level, update_leaderboard
from game_end_display import display_victory, display_partial_victory, display_loss, display_out_of_moves
from termcolor import cprint, colored
from egg_mover import move_eggs
from animation import loading_animation
import time


wall = '🧱'
egg = '🥚'
grass = '🟩'
empty_nest = '🪹'
full_nest = '🪺'
frying_pan = '🍳'


def copy_grid(grid): # Copies the grid for the undo feature
    return [row[:] for row in grid]

def start_game(filename): # Function for the Main "start" game_logic
    loading_animation()
    from main import main_menu
    grid, num_moves = load_level(filename)
    score = 0
    history = []
    moves = []
    movement_history = {
        'L': "←",
        'R': "→",
        'F': "↑",
        'B': "↓"
    }

    while num_moves > 0: # Loop that continues until there is avalable moves for the player
        clear_screen()
        print("=======================================================")
        cprint("              🍳 EGG ROLL CHALLENGE 🍳", "blue", attrs=["bold"])
        print("=======================================================\n")
        display_grid(grid)
        print("-------------------------------------------------------")
        print(colored("🔢 MOVES LEFT  ", "blue") + f" :  {num_moves}")
        print(colored("🌟 SCORE       ", "blue") + f" :  {score}")
        print(colored("🎯 PREV MOVE   ", "blue") + f" :  {" ".join(moves).strip()}")
        print("-------------------------------------------------------")
        move = input("Enter move " + colored("(L/R/F/B)", "blue", attrs=["bold"]) 
                     + ", " + colored("[U]", "blue", attrs=["bold"]) + "ndo, or " 
                     + colored("[E]", "blue", attrs=["bold"]) + "xit: ").upper()
        print("-------------------------------------------------------")

        if move == 'U' and history: # If the player decides to undo
            grid, num_moves, score, moves = history.pop()
            moves.pop()
            continue
        elif move == 'E': # If the player decides to exit the game
            while True:
                double_check = input("Are you sure you'd like to exit the game [Y/N]: ").upper()
                if double_check == "Y":
                    main_menu()
                    return
                elif double_check == "N":
                    break
                else:
                    cprint("Invalid response!", "red", attrs=["bold"])
                    time.sleep(1)
            continue
        elif move not in ['L', 'R', 'F', 'B']: # If the player doesn't input a valid option
            cprint("Invalid move! Try again.", "red", attrs = ["bold"])
            time.sleep(1)
            continue

        moves.append(movement_history[move])
        history.append((copy_grid(grid), num_moves, score, moves))
        add_score = move_eggs(grid, move)
        score += add_score
        num_moves -= 1

        clear_screen()

        # Check status of the grid as a basis for the end game display
        egg_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == egg]
        full_nest_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == full_nest]
        empty_nest_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == empty_nest]

    # Conditionals that handles which game display will pop-up
        if not egg_positions:
            if full_nest_positions and not empty_nest_positions:
                clear_screen()
                display_victory(score)
                break
            elif full_nest_positions and empty_nest_positions:
                clear_screen()
                display_partial_victory(score)
                break
            else:
                clear_screen()
                display_loss(score)
                break

    if num_moves == 0 and egg_positions: 
        clear_screen()
        display_out_of_moves(score, grid)

    display_grid(grid)
    print("-------------------------------------------------------")

    # To store name on leaderboard
    name = input("Enter your name: ")
    update_leaderboard(name, score)

    while True:  # Ask user for next action
        retry_option = input("Retry [R] or Main Menu [M]? ").upper()
        if retry_option == 'R':
            start_game(filename)
            break
        elif retry_option == 'M':
            main_menu()
            break
        else:
            cprint("Invalid response!", "red", attrs=["bold"])
            time.sleep(1)
