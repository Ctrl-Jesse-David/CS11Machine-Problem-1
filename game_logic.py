from main import clear_screen
from utilities import display_grid, load_level, update_leaderboard
from termcolor import cprint, colored
from egg_mover import move_eggs
import time


wall = '🧱'
egg = '🥚'
grass = '🟩'
empty_nest = '🪹'
full_nest = '🪺'
frying_pan = '🍳'


def copy_grid(grid): # Copies the grid for the undo
    return [row[:] for row in grid]

# Main game loop
def start_game(filename):
    from main import main_menu
    grid, num_moves = load_level(filename) # Unpack/Read level's file
    score = 0 # Score intializer
    history = [] # Moves history for [U]ndo
    moves = [] # For moves history
    movement_history = {
        'L': "←",
        'R': "→",
        'F': "↑",
        'B': "↓"
    }

    while num_moves > 0:
        clear_screen()
        print("=======================================================")
        cprint("              🍳 EGG ROLL CHALLENGE 🍳", "blue", attrs = ["bold"])
        print("=======================================================\n")
        display_grid(grid)
        print("-------------------------------------------------------")
        print(colored("🔢 MOVES LEFT  ", "blue") + f" :  {num_moves}")
        print(colored("🌟 SCORE       ", "blue") + f" :  {score}")
        print(colored("🎯 PREV MOVE   ", "blue") + f" :  {" ".join(moves).strip()}")
        print("-------------------------------------------------------")
        move = input("Enter move " + colored("(L/R/F/B)", "blue", attrs = ["bold"]) 
                     + ", " + colored("[U]", "blue", attrs = ["bold"]) + "ndo, or " 
                     + colored("[E]", "blue", attrs = ["bold"]) + "xit: ").upper()
        print("-------------------------------------------------------")

        if move == 'U' and history:
            grid, num_moves, score, moves = history.pop()
            moves.pop()
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

        moves.append(movement_history[move])
        history.append((copy_grid(grid), num_moves, score, moves))
        add_score = move_eggs(grid, move)
        score += add_score
        num_moves -= 1
    
        clear_screen()
    
        # Check whether you won or lost
        egg_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == egg]
        full_nest_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == full_nest]
        
        if not egg_positions:  # No more eggs in the frid
            if full_nest_positions: # If there is at least one full nest
                clear_screen()
                print("=======================================================")
                cprint("            🎉🎉 CONGRATULATIONS! 🎉🎉", "green", attrs = ["bold"])
                print("=======================================================")
                cprint("   🏆🏅 All eggs safely rolled into their nests! 🏅🏆", attrs = ["bold"])
                print("-------------------------------------------------------")
                print(colored("🏆 FINAL SCORE: ", "green", attrs = ["bold"]) + f" {score} 🏆")
                print("-------------------------------------------------------\n")
                break
            else: # No full nest and every egg went to the frying pan
                clear_screen()
                print("=======================================================")
                cprint("                  💥😞 You lost! 💥😞 ", "red", attrs = ["bold"])
                print("=======================================================")
                cprint("              better luck next time!", attrs = ["bold"])
                print("-------------------------------------------------------")
                print(colored("🏆 FINAL SCORE: ", "red", attrs = ["bold"]) + f" {score} 🏆")
                print("-------------------------------------------------------\n")
                break

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

        
