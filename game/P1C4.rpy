# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Humanity")
define p = Character("Politician")
define one_of_billions = Character("One of Billions within Humanity")
define a_child_among_billions = Character("A Child Among Billions")
define a_believer = Character("A Believer Among Billions")
define a_preacher = Character("A Preacher Among Billions")

label P1C4:
    show screen centeredbox("{size=+10}Chapter 4: A Way Out?{/size}")
    pause
    hide screen centeredbox

    p "Do you know what year it is, or how long it has been since we have been trapped in this form?"
    one_of_billions "I lost count after about twelve"
    one_of_billions "I don’t think we age anymore."
    one_of_billions "Does it still matter?"
    h "Perhaps, I did still age."
    h "Perhaps I did not."
    h "There was no mirror."
    h "I could not raise my hands to my eyes or scream in the darkness."
    h "All I had were the orbits of the planets to tell me of the passage of time."
    h "We stayed fixed in one place, never moving, never interacting with anything within the solar system."
    h "We did not revolve around a large body, and only rotated approximately a degree every five minutes or so."
    h "Each year, we were given a close glimpse of the planet we once called home as it crossed our field of vision and then left."
    h "The first day, all the lights could still be seen on the earth."
    h "Afterwards, it was complete darkness."
    h "If I knew the predicament I was in rather than simply denying it, perhaps we would have savored the sight I saw on that first day even more."
    h "Rather than wallow in disorientation, we could have lived in the moment, assuming that I am still living."
    a_child_among_billions "Is this hell?"
    a_believer "It must be"
    a_believer "Even though we were forgiven for our sins, that didn't absolve us of our responsibilities as God's creations."
    a_believer "We have sinned and this is our punishment."
    a_preacher "Then who among us is most guilty?"
    h "A preacher's voice boomed across the emptiness of space from within me."
    a_preacher "Who is the one who has doomed us to this fate?"
    h "An interesting question."
    h "Was it the soldiers that fought the wars?"
    h "No."
    h "They were the greatest patriots."
    h "Was it the serial killers and mass murderers?"
    h "Perhaps, but they were a misguided product of their society."
    # This ends the game.
    return