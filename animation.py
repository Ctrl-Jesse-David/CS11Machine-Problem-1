from utilities import clear_screen
import time

def egg_rolling_animation(): # Function that display's the egg roll (indiviudally)
    egg = "🥚"
    frames = 53

    for position in range(frames):
        clear_screen()
        print("=======================================================")
        print("                🍳 Egg Roll Challenge 🍳")
        print("=======================================================\n")
        
        print(" " * position + egg)
        print(" " * (frames-position) + egg)
        print(" " * position + egg)
        print(" " * (frames-position) + egg)
        print(" " * position + egg)
        print(" " * (frames-position) + egg)

        print("\n-------------------------------------------------------")
        print("Loading...\n")
        time.sleep(0.01)

def loading_animation(): # Function that displays the loading animation
    egg = "🥚"
    frames = 50

    for position in range(frames):
        clear_screen()
        print("=======================================================")
        print("              🍳 Egg Roll Challenge 🍳")
        print("=======================================================\n")

        print(" " * position + egg)
        print(" " * position + egg)
        print(" " * position + egg)
        
        print("\nLoading Menu...")
        print("-------------------------------------------------------")
        time.sleep(0.01)

def egg_rolling_animation_intro(): # Function for game's introduction animation
    egg_rolling_animation()
    egg_rolling_animation()