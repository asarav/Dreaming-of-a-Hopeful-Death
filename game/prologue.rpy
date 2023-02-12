# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")
image bg Prologue_witch_cabin = "prologue/bg Prologue_witch_cabin.png"
image bg Prologue_kingdom = "prologue/bg Prologue_fantasy_kingdom.png"
image bg Prologue_kingdom_2 = "prologue/bg Prologue_2_fantasy_kingdom.png"

screen centeredbox(said):
    style_prefix "centered"
    hbox: 
        xalign 0.5 
        yalign 0.5    
        frame: 
            background Image("gui/textbox.png", xalign=0.5, yalign=0.5)
            vbox: 
                box_wrap True 
                xalign 0.5 
                yalign 0.5 
                text said

style centered_text:
    text_align 0.5
    layout "subtitle"

# The game starts here.

label prologue:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg Prologue_witch_cabin

    play music "audio/Songs Without Words - No.12 in F Sharp Minor, Op.30.mp3" fadeout 1.0 fadein 1.0
    # Prologue
    show screen centeredbox("{size=+12}{outlinecolor=#000000}Prologue{/outlinecolor}{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("Once upon a time, there was a witch who lived within a forest deep within the territory of a burgeoning kingdom that was in the midst of turmoil.")
    pause
    hide screen centeredbox
    show screen centeredbox("This witch was a master of magic, potions, and alchemy whose practice has continued since the day she resolved herself to gain the highest of proficiencies in the occult arts during an era of history long forgotten.")
    pause
    hide screen centeredbox
    show screen centeredbox("Her livelihood was typically one of a relaxed solitude and hermitage.")
    pause
    hide screen centeredbox
    show screen centeredbox("The domain of man seldom reached her doorstep until now as a result of the fierce beasts that prowled the forest floors and the vegetation that spanned the savage reaches of nature’s dominion...")
    pause
    hide screen centeredbox
    show screen centeredbox("resulting in a labyrinth of hostile paths that were punctuated by oases of abundance and bucolic bliss.")
    pause
    hide screen centeredbox
    show screen centeredbox("Occasionally, a traveler wandered into her oasis; sometimes by accident, sometimes intentionally.")
    pause
    hide screen centeredbox
    show screen centeredbox("Initially, the witch acted cordially, healing the wounds of travelers and teaching them of the ways of the forest.")
    pause
    hide screen centeredbox

    scene bg Prologue_kingdom

    show screen centeredbox("With time, as those from the civilized world began to grow less fearful of the forest, the lost traveler was replaced by the prospecting adventurer who wished for profit within the impenetrable woods.")
    pause
    hide screen centeredbox
    show screen centeredbox("This led to unpleasant encounters where strangers intruded into her home in search of elixirs of immortality, gold, and knowledge.")
    pause
    hide screen centeredbox
    show screen centeredbox("A decision needed to be made on the proper course of action and this decision resulted in a large-scale circle of transmutation which surrounded the witch’s territory.")
    pause
    hide screen centeredbox
    show screen centeredbox("All who failed to heed the warnings placed on the edges of the circle were cursed to rapidly turn to stone when they trespassed into the domain of the witch.")
    pause
    hide screen centeredbox
    show screen centeredbox("Despite the cruel nature of the punishment, it was a stunning sight to see armies of people from all walks of life originating from the nearby kingdom collected in one place.")
    pause
    hide screen centeredbox
    show screen centeredbox("Eventually, these excursions into the forest by these invaders declined as the kingdom reached the end of its tenure.")
    pause
    hide screen centeredbox

    scene bg Prologue_kingdom_2

    show screen centeredbox("The statues withered to dust, and the kingdom which encroached upon the edge of the forest retreated as an extended civil war split the kingdom into two factions.")
    pause
    hide screen centeredbox
    show screen centeredbox("The royal family was being hunted and escaped by foot into the forest.")
    pause
    hide screen centeredbox
    show screen centeredbox("The king, queen, princess, and their retainers wandered the labyrinth of vines and pines only to become more and more entwined in its disorienting layout.")
    pause
    hide screen centeredbox
    show screen centeredbox("The king fell ill, and the queen starved, both passing together in the night.")
    pause
    hide screen centeredbox
    show screen centeredbox("The malnourished retainers who were left were eaten by wolves leaving the princess to wander aimlessly in the woods and fend for herself against the treacherous surroundings.")
    pause
    hide screen centeredbox
    show screen centeredbox("Crawling through the thickets, her hands bled as she blindly scrambled in the dark in search of shelter.")
    pause
    hide screen centeredbox
    show screen centeredbox("After hours of searching, her hopes were met in the form of a clearing partially illuminated by the moonlight.")
    pause
    hide screen centeredbox
    show screen centeredbox("Upon approaching the shadows, it became clear they held a humanoid form.")
    pause
    hide screen centeredbox
    show screen centeredbox("She reached out with a hand, as though to ask for help, and it was in that position she stayed as stone crawled upon her arm to leave her as a landmark.")
    pause
    hide screen centeredbox
    show screen centeredbox("Unable to speak, unable to move, unable to ask for help.")
    pause
    hide screen centeredbox
    show screen centeredbox("Doomed to live, but deprived of life.")
    pause
    hide screen centeredbox
    show screen centeredbox("She wished that someone could save her.")
    pause
    hide screen centeredbox
    show screen centeredbox("Unfortunately, the witch no longer resided in the forest.")
    pause
    hide screen centeredbox
    show screen centeredbox("The only thing she left behind were the statues that she effortlessly made without much thought anymore.")
    pause
    hide screen centeredbox
    show screen centeredbox("Whether she would return was unknown.")
    pause
    hide screen centeredbox

    jump P1C1