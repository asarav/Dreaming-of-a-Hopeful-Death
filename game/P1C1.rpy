# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg P1C1_title = "P1C1/bg P1C1 - Screaming while floating in the midst of space with stars and galaxies in the background.png"
image bg P1C1_empty_metropolis = "P1C1/bg P1C1 - A large modern metropolis devoid of any humans.png"
image bg P1C1_empty_metropolis2 = "P1C1/bg P1C1 - 2 A large modern metropolis devoid of any humans.png"
image bg P1C1_empty_metropolis3 = "P1C1/bg P1C1 - New York city after all humans have disappeared to leave it unmaintained.png"
image bg P1C1_empty_metropolis4 = "P1C1/bg P1C1 - 2 New York city after all humans have disappeared to leave it unmaintained.png"


label P1C1:
    play music "audio/Dreaming of a Hopeful Death Intro Theme.mp3" fadeout 2.0 fadein 1.0

    scene bg P1C1_title

    show screen centeredbox("{size=+16}Dreaming of a Hopeful Death{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+16}by A. S. Mori{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+12}Part 1: Wishes from a Past Far Gone{/size}")
    pause
    hide screen centeredbox
    show screen centeredbox("{size=+10}Chapter 1: The Curse{/size}")
    pause
    hide screen centeredbox

    scene bg P1C1_empty_metropolis

    show screen centeredbox("It is not always evolutionarily advantageous to be able to comprehend the fragility of one’s life and one’s race.")
    pause
    hide screen centeredbox
    show screen centeredbox("In the past, whether a meteor was about to impact the earth, or a galaxy could collide with the Milky Way was of no concern to the common man.")
    pause
    hide screen centeredbox
    show screen centeredbox("We do not perceive everything, and our senses are fundamentally flawed when considering what lies beyond our senses and our intellectual abilities to comprehend what is not.")
    pause
    hide screen centeredbox
    show screen centeredbox("To supplement our shortcomings, we use tools such as eyeglasses, telescopes, microscopes, as well as sensors that convert from other spectra and streams into a format we understand.")
    pause
    hide screen centeredbox
    show screen centeredbox("These too have a limitation in that they are the creations of humans. These humans are subject to human error, to misconceptions, and to a simple limitation of intellect and body.")
    pause
    hide screen centeredbox
    show screen centeredbox("Furthermore, reality holds an abundance of information that must be parsed to be made sense of.")
    pause
    hide screen centeredbox
    show screen centeredbox("Not all information is useful, and as a result, living organisms typically take advantage of that which is beneficial to the prolonging of its life and species and what it is even capable of processing.")
    pause
    hide screen centeredbox
    show screen centeredbox("Humanity is no exception.")
    pause
    hide screen centeredbox

    scene bg P1C1_empty_metropolis2

    show screen centeredbox("From the smallest building block of reality to the entirety of the unobservable universe, although there is much to learn of within a single lifetime, there is infinitely more that will never be known even when given the lifetime of the universe to explore it.")
    pause
    hide screen centeredbox
    show screen centeredbox("Despite this, human civilization has advanced its desire for knowledge in its eternal mission to minimize its pain, maximize its pleasure, and master its manipulation of the reality in which it is confined in.")
    pause
    hide screen centeredbox
    show screen centeredbox("In doing so, it advanced, while inflicting itself with artificial sufferings, to its pinnacle.")
    pause
    hide screen centeredbox
    show screen centeredbox("With a neo-liberalist global economy that valued continuous growth above all else, it advanced, day by day, quarter by quarter.")
    pause
    hide screen centeredbox
    show screen centeredbox("The system was effective due to its iterative nature, but ill-suited for thinking beyond the short term which meant that it was suboptimal.")
    pause
    hide screen centeredbox
    show screen centeredbox("It was very rarely that cosmic timescales were considered or even long term timescales that were relevant within a lifetime.")
    pause
    hide screen centeredbox
    show screen centeredbox("This is partially what led to the downfall of the modern human race, but even if human civilization managed to recognize its lack of knowledge as a severe existential threat, with its level of technology and confinement to the third dimension, it would have still been powerless to escape its fate.")
    pause
    hide screen centeredbox
    show screen centeredbox("Ignorant of the large-scale phenomena that occur in other dimensions, humanity was unaware of the occurrences and beings that resided within higher dimensions and was naturally unprepared for the fate they would be cursed to for the remainder of all time.")
    pause
    hide screen centeredbox

    scene bg P1C1_empty_metropolis3

    show screen centeredbox("Like stepping on an ant is to a human, an eldritch being operating beyond the third dimension mutated all living humans into a single entity within an instant.")
    pause
    hide screen centeredbox
    show screen centeredbox("In one moment, humanity was composed of multiple individuals going about their daily lives.")
    pause
    hide screen centeredbox
    show screen centeredbox("In the next, humanity was one entity with the memories of all living humans at the time, leaving the earth to all other species to fill the void.")
    pause
    hide screen centeredbox

    scene bg P1C1_empty_metropolis4

    show screen centeredbox("Society and civilization became one sentient being and in doing so, the nature of human existence was forever changed.")
    pause
    hide screen centeredbox
    show screen centeredbox("In other parallel realities, perhaps humanity was spared.")
    pause
    hide screen centeredbox
    show screen centeredbox("However, in this one, this specific one, humanity was forced into singularity and eternal life.")
    pause
    hide screen centeredbox
    show screen centeredbox("Its existence was now that of a singular entity unable to die or physically interact with the physical world until the universe reaches heat death.")
    pause
    hide screen centeredbox
    show screen centeredbox("Its role in the universe was no longer that of an active player, but rather an observer unable to act upon reality or conversely be acted upon.")
    pause
    hide screen centeredbox
    show screen centeredbox("Its future was now one that was sentenced to wander the universe like a sorrowful ghost that haunted the empty spaces between solar systems and planets— a Sisyphus of the cosmos.")
    pause
    hide screen centeredbox
    
    jump P1C2