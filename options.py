from utilities import clear_screen
from animation import loading_animation
from termcolor import cprint, colored
import os, time

'''
To create a game level file, follow this naming format: level_{number}.txt; eg. level_34.txt
    The first row should be the number of rows of the game_level
    The second row should be the total number of moves that is allowed for the game level
    The third row should be display the game level's grid
'''


def display_levels():
    while True:
        # Gets all the level files in the folder
        levels = [f for f in os.listdir() if f.endswith('.txt') and 'level_' in f]
        levels.sort(key=lambda x: int(x[6:-4]))

        # Display the sorted level files with their respective numbers
        clear_screen()
        print("=======================================================")
        cprint("               🎮 AVAILABLE LEVELS 🎮", "green", attrs = ["bold"])
        print("=======================================================")
        for level in levels:
            level_number = level[6:-4]  # Extract number from filename
            print(f"--> Level " + colored(f"{level_number}", "green", attrs = ["bold"]))
        
        print("-------------------------------------------------------")

        # Lets the user select the level by typing the level number or exit
        level_choice = input(colored("Enter the level number to start or [M] for Main Menu: ", "green", attrs = ["bold"])).strip().upper()
        if level_choice == "M":
            return None
        elif level_choice.isdigit():  # Check if input is a valid number
            level_choice = int(level_choice)
            if 1 <= level_choice <= len(levels): # Checks if the level exists
                selected_level = levels[level_choice - 1]
                return selected_level
            else:
                cprint("Level does not exist. Please select a valid number.", "red", attrs=["bold"])
        else:
            cprint("Invalid input. Please enter a number or [M] to go back to Main Menu.", "red", attrs=["bold"])
        
        time.sleep(1)

# function that displays the game's leaderboard
def display_leaderboard():
    loading_animation()
    clear_screen()
    print("=======================================================")
    cprint("                  🏆 Leaderboard 🏆", "yellow", attrs = ["bold"])
    print("=======================================================")
    try:
        with open("leaderboard.txt", "r") as file:
            # Reads the top 10 scores in the leaderboard in descending order
            scores = [line.strip().split(": ")for line in file]
            sorted_scores = sorted(scores, key=lambda x:int(x[1]), reverse = True)[:10]

            if sorted_scores: # Checks if there is already a leaderboard file then stores the name of the player if so
                for rank, (name, score) in enumerate(sorted_scores, start=1):
                    print(f"   {rank}. {name:<15} - {score:>5}")
            else:
                print("No scores yet! Play to be the first on the leaderboard!")

    except FileNotFoundError: # If there is no leaderboard file yet
        print("   No leaderboard found. Play the game to create one!")
    
    print("-------------------------------------------------------")
    input(colored("Press Enter to return to the main menu.", "yellow", attrs = ["bold"]))
    clear_screen()

# Function that displays the game's instructions
def display_instructions():
    loading_animation()
    clear_screen()
    print("=======================================================")
    cprint("               📜 GAME INSTRUCTIONS 📜", "light_red", attrs = ["bold"])
    print("=======================================================")
    cprint("🕹️  Controls:", "light_red", attrs = ["bold"])
    print("  Use these commands to move the eggs:")
    print("    L - Roll Left")
    print("    R - Roll Right")
    print("    F - Roll Forward (Up)")
    print("    B - Roll Backward (Down)")
    print("-------------------------------------------------------")
    cprint("🚧 Obstacles:", "light_red", attrs = ["bold"])
    print("  🧱 Walls - Eggs can't pass through them.")
    print("  🪺 Full Nests - Eggs can't pass through them.")
    print("  🍳 Frying Pans - Eggs will get fried so AVOID it!")
    print("-------------------------------------------------------")
    cprint("🏆 Objective:", "light_red", attrs = ["bold"])
    print(" Roll all eggs into the empty nests 🪹 to win the game!")
    print("=======================================================")
    
    input(colored("Press Enter to return to the main menu.", "light_red", attrs = ["bold"]))
    clear_screen()