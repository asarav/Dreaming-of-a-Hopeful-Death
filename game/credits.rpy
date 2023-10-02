# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")

image bg credits_title = "P1C1/bg P1C1 - Screaming while floating in the midst of space with stars and galaxies in the background.png"


label credits:
    play music "audio/Dreaming of a Hopeful Death Intro Theme.mp3" fadeout 2.0 fadein 1.0

    scene bg P1C1_title

    show screen centeredbox("{size=+16}Dreaming of a Hopeful Death{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}by A. S. Mori{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Based on the novel of the same name{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+12}Music:{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Dreaming of a Hopeful Death Title - A. S. Mori{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Songs Without Words: No.12 in F Sharp Minor, Op.30, Felix Mendelssohn, European Archive{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Pavane For a Dead Princess - Maurice Ravel, Markus Staab{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Preludes Op. 28 No. 4 Suffocation - Chopin, Ivan Ilic{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Peer Gynt Suite no. 1, Op. 46 II Aase's Death - Edvard Grieg, Musopen Symphony{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Etude Op. 25 no. 7 in C sharp minor- 'Cello' - Chopin, Edward Neeman{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}All images were generated within Dall-E 2 and prompted by A. S. Mori.{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}To support A. S. Mori, please consider purchasing the novel Dreaming of a Hopeful Death which is available in multiple formats on Amazon.{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Made with Ren'Py{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Thank you for playing till the end.{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("Dreaming of a Hopeful Death © 2023 by A. S. Mori is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/")
    pause
    hide screen centeredbox

    # End the game here
    return