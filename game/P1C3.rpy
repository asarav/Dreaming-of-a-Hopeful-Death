# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")
image bg Current_Universe = "bg P1C3_our_current_universe.png"
image bg Current_Universe_2 = "bg P1C3_our_current_universe_2.png"

label P1C3:
    show screen centeredbox("{size=+10}Chapter 3: The Stelliferous Era{/size}")
    pause
    hide screen centeredbox
    scene bg Current_Universe
    show screen centeredbox("We are now witness to the Stelliferous Era which is the successor of the Primordial Era.")
    pause
    hide screen centeredbox
    show screen centeredbox("This era marks the period where stars were born in the expanding vacuum known as the universe.")
    pause
    hide screen centeredbox
    # This ends the game.
    return