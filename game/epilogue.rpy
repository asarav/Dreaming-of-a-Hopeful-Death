# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")
# The game starts here.
image bg aged_princess = "epilogue/A princess who was turned to stone reaching out towards the sky. The princess is surrounded by forest. Time has passed, and now the princess who is a .png"
image bg aged_princess2 = "epilogue/A princess who was turned to stone reaching out towards the sky. The princess is surrounded by forest. Time has passed, and now the princess who is a 2.png"
image bg cracked_princess = "epilogue/A princess who was turned to stone reaching out towards the sky with wide and visible cracks forming in her stone form. Plants are beginning to take r.png"
image bg cracked_princess2 = "epilogue/A princess who was turned to stone reaching out towards the sky with wide and visible cracks forming in her stone form. Plants are beginning to take r 2.png"
image bg broken_statue = "epilogue/The weathered remains of a female statue on the forest floor with a tree growing from the area where the statue fell..png"
image bg broken_statue2 = "epilogue/The weathered remains of a female statue on the forest floor with a tree growing from the area where the statue fell 2.png"
image bg dying_tree = "epilogue/A large tree within the forest that is withered and dying..png"
image bg dying_tree2 = "epilogue/A large tree within the forest that is withered and dying 2.png"
image bg large_desert = "epilogue/A large desert with no end where a forest once stood.png"
image bg large_desert2 = "epilogue/A large desert with no end where a forest once stood 2.png"
image bg large_desert3 = "epilogue/A large desert with no end where a forest once stood 3.png"

label epilogue:
    scene bg aged_princess

    # Epilogue
    show screen centeredbox("{size=+12}{outlinecolor=#000000}Epilogue{/outlinecolor}{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("In a field of statues deep within the forests on the edge of civilization, the one that remained was a fractured shell of its former self.")
    pause
    hide screen centeredbox
    show screen centeredbox("The princess, to the end, never was given a chance to escape from her plight, forever confined to live as rock till the winds and the rains turned her to dust.")
    pause
    hide screen centeredbox
    show screen centeredbox("She never regained her identity as a princess, a human, a living being, or an individual.")
    pause
    hide screen centeredbox
    show screen centeredbox("She lived long, surviving the witch who petrified her, and survived long enough to see the beginnings and ends of many kingdoms and civilizations that encroached on the border of her prison.")
    pause
    hide screen centeredbox
    show screen centeredbox("Like peering through the bars, she would glean information with what little changes could be observe from her perspective.")
    pause
    hide screen centeredbox
    show screen centeredbox("People came and people went, but in the end, no one turned her back.")
    pause
    hide screen centeredbox
    show screen centeredbox("She became a passing curiosity rather than an individual with wants and needs.")
    pause
    hide screen centeredbox

    scene bg aged_princess2

    show screen centeredbox("She was no longer a living, breathing being, but an art piece.")
    pause
    hide screen centeredbox
    show screen centeredbox("Albeit an art piece fully capable of human thought.")
    pause
    hide screen centeredbox
    show screen centeredbox("If those who saw her knew, would they have treated her differently?")
    pause
    hide screen centeredbox
    show screen centeredbox("The callousness of other people was all too familiar to her.")
    pause
    hide screen centeredbox
    show screen centeredbox("The possibility of any breakthroughs was unlikely.")
    pause
    hide screen centeredbox
    show screen centeredbox("The seasons passed, and her companions who stood by her side eroded away piece by piece.")
    pause
    hide screen centeredbox

    scene bg cracked_princess2

    show screen centeredbox("She too was beginning to lose pieces of herself as the years passed.")
    pause
    hide screen centeredbox
    show screen centeredbox("At first, it was surface level.")
    pause
    hide screen centeredbox
    show screen centeredbox("Like the wrinkles of old age, cracks and miniscule fissures formed.")
    pause
    hide screen centeredbox
    show screen centeredbox("Small chunks were carried away with the changing winds and rains.")
    pause
    hide screen centeredbox
    show screen centeredbox("The fragments fell by her side and were either washed away or disintegrated due to the elements.")
    pause
    hide screen centeredbox

    scene bg cracked_princess

    show screen centeredbox("These things that were once part of her were gone, and they were not coming back.")
    pause
    hide screen centeredbox
    show screen centeredbox("With time, the cracks and flaws grew larger.")
    pause
    hide screen centeredbox
    show screen centeredbox("It was as though the dam broke and with the first damages the forces of time accelerated her degradation.")
    pause
    hide screen centeredbox
    show screen centeredbox("What was once skin deep later became fingers, a nose, and eventually entire limbs.")
    pause
    hide screen centeredbox

    scene bg broken_statue2

    show screen centeredbox("The first arm that was to go was the one that was outstretched and reaching out in desperation.")
    pause
    hide screen centeredbox
    show screen centeredbox("It fell off with a crack, but landed softly in the overgrown grasses that surrounded her.")
    pause
    hide screen centeredbox
    show screen centeredbox("It too would disintegrate.")
    pause
    hide screen centeredbox
    show screen centeredbox("If she could look in a mirror, she could see that all the finer features of her appearance were now faded.")
    pause
    hide screen centeredbox
    show screen centeredbox("Lines were dulled into rounded edges, what once was a face now had bumps to indicate what was once there, and her hair was melted into one smooth stone surface.")
    pause
    hide screen centeredbox
    show screen centeredbox("Plants made a home out of her with vines taking root in her body where the cracks were.")
    pause
    hide screen centeredbox
    show screen centeredbox("These were a force to topple her over to meet the same end as her fingers and outstretched arm.")
    pause
    hide screen centeredbox

    scene bg broken_statue

    show screen centeredbox("With her arm no longer there to balance her, she fell backwards with her eyes directed towards the sky and the ceiling formed by the forest canopy overhead.")
    pause
    hide screen centeredbox
    show screen centeredbox("Her last days of conscious thought were spent looking at the blue sky and the starry nights.")
    pause
    hide screen centeredbox
    show screen centeredbox("Despite her body withering, she felt no pain.")
    pause
    hide screen centeredbox
    show screen centeredbox("She watched on, intrigued, regretful, and surprisingly calm.")
    pause
    hide screen centeredbox
    show screen centeredbox("It was a slow process where she lost parts of herself.")
    pause
    hide screen centeredbox
    show screen centeredbox("Eventually, she began to forget what was a part of her and what was not.")
    pause
    hide screen centeredbox
    show screen centeredbox("As she became dust, she joined the soil and was then washed away in the rain.")
    pause
    hide screen centeredbox
    show screen centeredbox("Nothing came as a surprise, and she was thankful for the opportunity, no matter how limited.")
    pause
    hide screen centeredbox
    show screen centeredbox("In the days that followed, a sprout emerged from where she once stood.")
    pause
    hide screen centeredbox
    show screen centeredbox("It grew into a strong tree that lasted many centuries only to follow her in its eventual demise where its corpse formed a withered husk.")
    pause
    hide screen centeredbox

    scene bg dying_tree

    show screen centeredbox("In the millennia that followed, the rains grew fewer and fewer.")
    pause
    hide screen centeredbox

    scene bg dying_tree2

    show screen centeredbox("The forest starved and lost its luster.")
    pause
    hide screen centeredbox

    scene bg large_desert

    show screen centeredbox("The forest and all its creatures vanished after fighting a long battle and its place was sprawling desert that was home to its own class of inhabitants.")
    pause
    hide screen centeredbox

    scene bg large_desert2

    show screen centeredbox("Throughout all of this, the planet on which the princess once stood continued to spin.")
    pause
    hide screen centeredbox

    scene bg large_desert3

    show screen centeredbox("It continued to revolve around its sun, and the cosmos remained unaffected as all the heavenly bodies traveled their predetermined paths.")
    pause
    hide screen centeredbox

    # End the game here
    return