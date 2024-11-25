from termcolor import cprint, colored
from utilities import display_grid

def display_header(title, title_color="green"):
    """ Displays the header with a changeable title """
    print("=======================================================")
    cprint(f"            {title}", title_color, attrs=["bold"])
    print("=======================================================")

def display_footer(score, color="green"):
    """ Displays the footer with the final score of the player """
    print("-------------------------------------------------------")
    print(colored("🏆 FINAL SCORE: ", color, attrs=["bold"]) + f"{score} 🏆")
    print("-------------------------------------------------------\n")

def display_message(score, title, main_message, title_color="green", score_color="green"):
    """ Displays the victory/partial victory/loss/out of moves message """
    display_header(title, title_color)
    cprint(main_message, attrs=["bold"])
    display_footer(score, score_color)

def display_victory(score):
    """ Displays the victory message """
    display_message(
        score,
        title="🎉🎉 CONGRATULATIONS! 🎉🎉",
        main_message="   🏆🏅 All eggs safely rolled into their nests! 🏅🏆",
        title_color="green",
        score_color="green"
    )

def display_partial_victory(score):
    """ Displays the partial victory message """
    display_message(
        score,
        title="💥😞 Nice Try! 💥😞",
        main_message="  You weren't able to put all eggs inside the nest!!",
        title_color="red",
        score_color="red"
    )

def display_loss(score):
    """ Displays the loss message """
    display_message(
        score,
        title="💥😞 You lost! 💥😞",
        main_message="                 Better luck next time!",
        title_color="red",
        score_color="red"
    )

def display_out_of_moves(score, grid):
    """ Displays the out of moves message """
    display_message(
        score,
        title="💥😞 You ran out of moves! 💥😞",
        main_message="                Better luck next time!",
        title_color="red",
        score_color="red"
    )
