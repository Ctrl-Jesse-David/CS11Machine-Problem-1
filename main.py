import sys, time
from termcolor import cprint, colored
from animation import egg_rolling_animation_intro
from utilities import clear_screen
from options import display_leaderboard, display_instructions

def main_menu():
    from game_logic import start_game

    egg_rolling_animation_intro() # Animation for Game Intro
    clear_screen()

    while True:
        # Main Menu of the User's Interface
        print("=======================================================")
        cprint("          🥚 Welcome to EGG ROLL CHALLENGE 🥚          ", 'light_blue', attrs = ["bold"])
        print("=======================================================")
        print("            Can you guide the eggs safely?")
        print("           Let the rolling adventure begin!")
        print("-------------------------------------------------------")
        print("                🍳 ", end = "")
        cprint("[S]", "light_blue", attrs = ["bold"], end = "")
        print(" Start Game   🍳")
        print("                📜 ", end = "")
        cprint("[I]", "light_blue", attrs = ["bold"], end = "")
        print(" Instructions 📜")
        print("                🏆 ", end = "")
        cprint("[L]", "light_blue", attrs = ["bold"], end = "")
        print(" Leaderboards 🏆")
        print("                🚪 ", end = "")
        cprint("[E]", "light_blue", attrs = ["bold"], end = "")
        print(" Exit Game    🚪")
        print("-------------------------------------------------------")
        print("        Please enter a choice and press Enter.")
        print("=======================================================")

        # Gets the player's choice
        choice = input(colored("Select an option: ", "light_blue", attrs = ["bold"])).strip().upper()  

        if choice == "S": # To start the game
            if len(sys.argv) > 1: # If game_level.txt is provided
                file = sys.argv[1]
            else: # If game_level.txt isn't provided
                file = input("Enter the level file name to start: ").strip()
            try: # If the file exists
                start_game(file)
            except FileNotFoundError: # If the file doesn't exist
                print(f"File: {file}", end="")
                cprint(" does not exist!", "red", attrs = ["bold"])
                time.sleep(1.3)
                clear_screen()

        elif choice == "I": # To display the instructions
            display_instructions()

        elif choice == "L": # To display the leaderboard
            display_leaderboard()

        elif choice == "E": # To exit the game
            cprint("Exiting... Thanks for playing!", 'red', attrs = ["bold"])
            sys.exit()

        else: # If the player's choice isn't in the menu
            print("Invalid Choice. Please try again!")
            time.sleep(0.5)
            clear_screen()

if __name__ == '__main__':
    main_menu()


'''Bugs to fix:
                Egg Roll: Make it roll at the same time
                count egg, and response is according to the number of eggs (plural/singular)
                Put the history of moves!
                when egg goes into the nest in level1.txt, it should say you lost
                multiple stages / stage selctor (how)
'''
