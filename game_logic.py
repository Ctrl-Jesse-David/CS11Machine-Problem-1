from main import clear_screen
from utilities import display_grid, load_level, update_leaderboard, process_moves
from game_end_display import display_victory, display_partial_victory, display_loss, display_out_of_moves
from termcolor import cprint, colored
from egg_mover import move_eggs
from animation import loading_animation
import time


''' This section contains all the game constants '''
wall = '🧱'
egg = '🥚'
grass = '🟩'
empty_nest = '🪹'
full_nest = '🪺'
frying_pan = '🍳'


def copy_grid(grid):
    '''Copies the grid for the undo feature '''
    return [row[:] for row in grid]


def get_grid_states(grid):
    """ Calculate the positions of eggs, full nests, and empty nests """
    egg_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == egg]
    full_nest_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == full_nest]
    empty_nest_positions = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == empty_nest]
    return egg_positions, full_nest_positions, empty_nest_positions


def start_game(filename):
    ''' Starts the main game logic '''
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

    while True:
        ''' Creates an infinite loop which breaks if the necessary conditions are followed '''
        
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

        '''
        Check first the grid's state whether it has no more eggs inside the grid then verify if:
        - There are eggs in at least one nest and there is no empty_nest
        - There are eggs in at least one nest and there is at least one empty_nest
        - There are no full_nest positions (else-block)
        - You lost all of your avaialble moves
        '''

        egg_positions, full_nest_positions, empty_nest_positions = get_grid_states(grid)

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

        if num_moves == 0:
            clear_screen()
            display_out_of_moves(score, grid)
            break

        move_raw = input("Enter move " + colored("(L/R/F/B)", "blue", attrs=["bold"]) 
                        + ", " + colored("[U]", "blue", attrs=["bold"]) + "ndo, or " 
                        + colored("[E]", "blue", attrs=["bold"]) + "xit: ").upper()
        print("-------------------------------------------------------")


        ''' The function "process_moves" filters out the valid moves for the game to process.
        This will then undergo a for-loop to process every move ("LLL" will be 3 "L" for-loops) '''
        
        move = process_moves(move_raw)

        for player_move in move:
            if player_move == "no valid moves":
                cprint("No valid moves found! Try again.", "red", attrs=["bold"])
                time.sleep(1)
                continue

            elif player_move == 'U':
                if history:
                    grid, num_moves, score, moves = history.pop()
                    if moves:
                        moves.pop()
                    continue
                else:
                    cprint("Nothing to undo!", "red", attrs=["bold"])
                    time.sleep(1)
                    continue

            elif player_move == 'E':
                while True:
                    double_check = input("Are you sure you'd like to exit the game " 
                                         + colored("[Y/N]", "red", attrs=["bold"]) + ": ").upper()
                    if double_check == "Y":
                        main_menu()
                        return
                    elif double_check == "N":
                        break
                    else:
                        cprint("Invalid response!", "red", attrs=["bold"])
                        time.sleep(1)
                continue

            elif player_move not in movement_history:
                cprint("Invalid player_move! Try again.", "red", attrs=["bold"])
                time.sleep(1)
                continue
            
            ''' This section appends the moves to display the previous moves, the data that 
            will be stored in history to do the "undo" feature, and adds the score based from
            the move '''
            
            moves.append(movement_history[player_move])
            history.append((copy_grid(grid), num_moves, score, moves[:]))
            add_score = move_eggs(grid, player_move)
            score += add_score
            num_moves -= 1

    display_grid(grid)
    print("-------------------------------------------------------")

    ''' this section updates the leaderboard, then gives an option for the user
    to retry or go back to the main menu interface '''

    name = input("Enter your name: ")
    update_leaderboard(name, score)

    while True:
        retry_option = input("Retry " + colored("[R]", "red", attrs=["bold"]) + "or Main Menu " 
                             + colored("[M]", "red", attrs=["bold"]) + "?: ").upper()
        if retry_option == 'R':
            start_game(filename)
            break
        elif retry_option == 'M':
            main_menu()
            break
        else:
            cprint("Invalid response!", "red", attrs=["bold"])
            time.sleep(1)
