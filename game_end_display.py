from termcolor import cprint, colored
from utilities import display_grid

# The displays that will pop-up after finishing the game:

def display_victory(score): # If you were able to put all eggs inside the nest
    print("=======================================================")
    cprint("            🎉🎉 CONGRATULATIONS! 🎉🎉", "green", attrs=["bold"])
    print("=======================================================")
    cprint("   🏆🏅 All eggs safely rolled into their nests! 🏅🏆", attrs=["bold"])
    print("-------------------------------------------------------")
    print(colored("🏆 FINAL SCORE: ", "green", attrs=["bold"]) + f" {score} 🏆")
    print("-------------------------------------------------------\n")

def display_partial_victory(score): # If you weren't able to put ALL eggs inside the nests (but was able to put at least 1)
    print("=======================================================")
    cprint("                  💥😞 Nice Try! 💥😞", "red", attrs=["bold"])
    print("=======================================================")
    cprint("  You weren't able to put all eggs inside the nest!!", attrs=["bold"])
    print("-------------------------------------------------------")
    print(colored("🏆 FINAL SCORE: ", "red", attrs=["bold"]) + f" {score} 🏆")
    print("-------------------------------------------------------\n")

def display_loss(score): # If you weren't able to put EVERY egg inside the nests
    print("=======================================================")
    cprint("                  💥😞 You lost! 💥😞", "red", attrs=["bold"])
    print("=======================================================")
    cprint("                 Better luck next time!", attrs=["bold"])
    print("-------------------------------------------------------")
    print(colored("🏆 FINAL SCORE: ", "red", attrs=["bold"]) + f" {score} 🏆")
    print("-------------------------------------------------------\n")

def display_out_of_moves(score, grid): # If you ran out of moves
    print("=======================================================")
    cprint("             💥😞 You ran out of moves! 💥😞", "red", attrs=["bold"])
    print("=======================================================")
    cprint("                Better luck next time!", attrs=["bold"])
    print("-------------------------------------------------------")
    print(colored("🏆 FINAL SCORE: ", "red", attrs=["bold"]) + f" {score} 🏆")
    print("-------------------------------------------------------\n")
    display_grid(grid)
    print("-------------------------------------------------------")
