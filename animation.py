from utilities import clear_screen
import time

# Function that display's the egg roll (indiviudally)
def egg_rolling_animation():
    egg = "🥚"
    frames = 53  # Number of frames to roll across the screen

    for position in range(frames):
        clear_screen()
        print("=======================================================")
        print("              🍳 Egg Roll Challenge 🍳")
        print("=======================================================\n")
        
        # Move the egg across the screen in each frame
        print(" " * position + egg)
        print(" " * (frames-position) + egg)
        print(" " * position + egg)
        print(" " * (frames-position) + egg)
        print(" " * position + egg)
        print(" " * (frames-position) + egg)

        print("\n-------------------------------------------------------")
        time.sleep(0.01)  # Control the animation speed

# Function that displays the loading animation
def loading_animation():
    egg = "🥚"
    frames = 50  # Number of frames to roll across the screen

    for position in range(frames):
        clear_screen()
        print("=======================================================")
        print("              🍳 Egg Roll Challenge 🍳")
        print("=======================================================\n")
        
        # Move the egg across the screen in each frame
        print(" " * position + egg)
        print(" " * position + egg)
        print(" " * position + egg)
        
        print("\nLoading Menu...")
        print("-------------------------------------------------------")
        time.sleep(0.01)  # Control the animation speed

# Function for game's introduction
def egg_rolling_animation_intro():
    egg_rolling_animation()
    egg_rolling_animation()