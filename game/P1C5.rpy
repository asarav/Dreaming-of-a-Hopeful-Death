# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")

label P1C5:
    show screen centeredbox("{size=+10}Chapter 5: Freakshow{/size}")
    pause
    hide screen centeredbox

    # This ends the game.
    return