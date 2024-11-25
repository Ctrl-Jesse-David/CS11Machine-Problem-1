from utilities import clear_screen
from animation import loading_animation
from termcolor import cprint, colored
import os, time

# INSTRUCTION FOR CREATING THE GAME LEVEL
'''
To create a game level file, follow this naming format: level_{number}.txt; eg. level_34.txt
    The first row should be the number of rows of the game_level
    The second row should be the total number of moves that is allowed for the game level
    The third row should be display the game level's grid
'''

''' This file handles displaying the options part of the game levvel '''

def display_header(title, color):
    ''' Display the commom header for the options '''
    loading_animation()
    clear_screen()
    print("=======================================================")
    cprint(title, color, attrs=["bold"])
    print("=======================================================")


def get_available_levels():
    """ Returns the available level files sorted by their level number """
    levels = [f for f in os.listdir() if f.endswith('.txt') and 'level_' in f]
    levels.sort(key=lambda x: int(x[6:-4]))
    return levels


def display_levels():
    """ Displays available levels and allows the user to select a level """
    while True:
        display_header(
            title="               🎮 AVAILABLE LEVELS 🎮", 
            color="green")
        
        levels = get_available_levels()
        for level in levels:
            level_number = level[6:-4]
            print(f"--> Level {colored(level_number, 'green', attrs=['bold'])}")

        print("-------------------------------------------------------")

        level_choice = input(colored("Enter the level number to start or [M] for Main Menu: ", "green", attrs=["bold"])).strip().upper()
        
        if level_choice == "M":
            return None
        elif level_choice.isdigit():
            level_choice = int(level_choice)
            if 1 <= level_choice <= len(levels):
                selected_level = levels[level_choice - 1]
                return selected_level
            else:
                cprint("Level does not exist. Please select a valid number.", "red", attrs=["bold"])
        else:
            cprint("Invalid input. Please enter a number or [M] to go back to Main Menu.", "red", attrs=["bold"])

        time.sleep(0.75)


def display_leaderboard():
    """ Displays the leaderboard with the top 10 highest scorers """
    display_header(
        title="                  🏆 Leaderboard 🏆", 
        color="yellow")
    try:
        with open("leaderboard.txt", "r") as file:
            scores = sorted((line.strip().split(": ") for line in file),
                key=lambda x: int(x[1]), reverse=True)[:10]
        if scores:
            for rank, (name, score) in enumerate(scores, start=1):
                print(f"   {rank}. {name:<15} - {score:>5}")
        else:
            print("No scores yet! Play to be the first on the leaderboard!")

    except FileNotFoundError:
        print("   No leaderboard found. Play the game to create one!")

    input(colored("Press Enter to return to the main menu.", "yellow", attrs=["bold"]))
    clear_screen()


def display_instructions():
    """ Displays the complete and detailed game instructions """
    display_header(
        title = "               📜 GAME INSTRUCTIONS 📜", 
        color = "light_red")
    
    cprint("🕹️  Controls:", "light_red", attrs=["bold"])
    print("  Use these commands to move the eggs:")
    print("    L - Roll Left")
    print("    R - Roll Right")
    print("    F - Roll Forward (Up)")
    print("    B - Roll Backward (Down)")
    print("-------------------------------------------------------")
    cprint("🚧 Obstacles:", "light_red", attrs=["bold"])
    print("  🧱 Walls - Eggs can't pass through them.")
    print("  🪺 Full Nests - Eggs can't pass through them.")
    print("  🍳 Frying Pans - Eggs will get fried so AVOID it!")
    print("-------------------------------------------------------")
    cprint("🏆 Objective:", "light_red", attrs=["bold"])
    print(" Roll all eggs into the empty nests 🪹 to win the game!")
    print("=======================================================")
    
    input(colored("Press Enter to return to the main menu.", "light_red", attrs=["bold"]))
    clear_screen()
