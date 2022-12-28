# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")

label P2C1:
    show screen centeredbox("{size=+12}Part 2: Wishes from a Past Far Gone{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Chapter 7: The Degenerate Era{/size}")
    pause
    hide screen centeredbox

    # End the game here
    return
