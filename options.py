from utilities import clear_screen
from animation import loading_animation
from termcolor import cprint, colored


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