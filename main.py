import sys, time
from termcolor import cprint, colored
from animation import egg_rolling_animation_intro
from utilities import clear_screen
from options import display_leaderboard, display_instructions, display_levels

def main_menu():
    from game_logic import start_game

    egg_rolling_animation_intro()
    clear_screen()

    while True: # Main Menu of the User's Interface
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

        # Gets the player's choice
        choice = input(colored("Select an option: ", "light_blue", attrs = ["bold"])).strip().upper()

        if choice == "S":  # To start the game
            selected_level = display_levels()  # Function that gets the selected level
            if selected_level:
                start_game(selected_level)
            else:
                clear_screen()

        elif choice == "I":  # To display the instructions
            display_instructions()

        elif choice == "L":  # To display the leaderboard
            display_leaderboard()

        elif choice == "E":  # To exit the game
            cprint("Exiting... Thanks for playing!", 'red', attrs = ["bold"])
            sys.exit()

        else:  # If the player's choice isn't in the menu
            print("Invalid Choice. Please try again!")
            time.sleep(0.5)
            clear_screen()

if __name__ == '__main__':
    main_menu()