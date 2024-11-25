import sys, time
from termcolor import cprint, colored
from animation import egg_rolling_animation_intro
from utilities import clear_screen
from options import display_leaderboard, display_instructions, display_levels

''' This file handles the main menu interface of the player '''

def main_menu():
    '''
    This function gives the player the option by entering the highlighted letter.
    The input will either:
    
    - Start the game (will proceed to the available game levels)
    - Display the leaderboard for those who played the game
    - Show the game's instructions
    - Exit the game
    '''

    from game_logic import start_game

    egg_rolling_animation_intro()
    clear_screen()

    while True:
        print("=======================================================")
        cprint("          🥚 Welcome to EGG ROLL CHALLENGE 🥚          ", 'light_blue', attrs = ["bold"])
        print("=======================================================")
        print("            Can you guide the eggs safely?")
        print("           Let the rolling adventure begin!") 
        print("-------------------------------------------------------")
        print("                🍳 " + colored("[S]", "light_blue", attrs = ["bold"]) + " Start Game   🍳")
        print("                📜 " + colored("[I]", "light_blue", attrs = ["bold"]) + " Instructions 📜")
        print("                🏆 " + colored("[L]", "light_blue", attrs = ["bold"]) + " Leaderboards 🏆")
        print("                🍳 " + colored("[E]", "light_blue", attrs = ["bold"]) + " Exit Game    🚪")
        print("-------------------------------------------------------")
        print("        Please enter a choice and press Enter.")
        print("=======================================================")

        choice = input(colored("Select an option: ", "light_blue", attrs = ["bold"])).strip().upper()

        if choice == "S": 
            selected_level = display_levels()
            if selected_level:
                start_game(selected_level)
            else:
                clear_screen()

        elif choice == "I":
            display_instructions()

        elif choice == "L":
            display_leaderboard()

        elif choice == "E":
            cprint("Exiting... Thanks for playing!", 'red', attrs = ["bold"])
            sys.exit()

        else:
            print("Invalid Choice. Please try again!")
            time.sleep(0.1)
            clear_screen()

if __name__ == '__main__':
    main_menu()
