# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")

label P1C4:
    show screen centeredbox("{size=+10}Chapter 4: A Way Out?{/size}")
    pause
    hide screen centeredbox
    # This ends the game.
    return