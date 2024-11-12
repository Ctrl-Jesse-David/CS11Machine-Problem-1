from utilities import clear_screen
from animation import loading_animation
from termcolor import cprint, colored
import os, time


# Make a user friendly interface
def display_levels():
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
        print(f"--> Level {level_number}")
    
    print("-------------------------------------------------------")

    # Let the user select the level by typing the level number
    level_choice = input(colored("Enter the level number to start: ", "green", attrs = ["bold"]))

    # Check if the input is valid
    try:
        level_choice = int(level_choice)
        if 1 <= level_choice <= len(levels):
            selected_level = levels[level_choice - 1]
            return selected_level
        else:
            print("Invalid level choice.")
            time.sleep(1)
            return None
    except ValueError:
        print("Please enter a valid number.")
        time.sleep(1)
        return None


# function that displays the game's leaderboard
def display_leaderboard():
    loading_animation()
    clear_screen()
    print("=======================================================")
    cprint("                  🏆 Leaderboard 🏆", "yellow", attrs = ["bold"])
    print("=======================================================")
    try:
        with open("leaderboard.txt", "r") as file:
            # Reads the scores in the leaderboard in descending order
            scores = [line.strip().split(": ")for line in file]
            sorted_scores = sorted(scores, key=lambda x:int(x[1]), reverse = True)[:10]

            if sorted_scores:
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

def game_level_selector():
    print("=======================================================")
    cprint("               📜 SELECT GAME LEVEL 📜", "light_red", attrs = ["bold"])
    print("=======================================================")
    # display game levels
    print("-------------------------------------------------------")
    print("        Please enter a choice and press Enter.")
    print("=======================================================")