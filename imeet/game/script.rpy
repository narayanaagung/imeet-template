# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Donkey")
define r = Character("Rabbit")
define n = Character("Dragon")
define bb = Character("Brown Bear")
define c = Character("Black Cat")
define unk = Character("???")

define transisi = Dissolve(.5)
define lambat = Dissolve(1)

# The game starts here.

label start:
    scene bg hutan
    with Dissolve(.5)
    "Long time ago and far away from here, there's live an Donkey."
    "This Donkey like any usual Donkey, have a pairs of big ear.But this Donkey have a dream,"
    "She want to live as rabbit."
    show donkey:
        xalign 0.0
        yalign 1.0
    with transisi
    d"I want to be a Rabbit ! Eat carrots, live on dig, have a small body."
    "One day, the Donkey meet her friend,an brown bear.Then she ask her about her problem."
    show bear:
        xalign 1.0
        yalign 1.0
    with transisi
    d"Hey brown bear ! I need your help"
    bb"What i can do for you Donkey ?"
    d"I want turn to be Rabbit, what should i do ?"
    bb"(Hmm...what should i tell to her?)"
    menu:
        "Tell Donkey to stop pursue her dream to be Rabbit":
            $ route="a1"
            jump route_a1
        "Tell Donkey to find the Dragon":
            $ route="b1"
            jump route_b1

label route_a1:
    bb"Buddy, i know its hard for you.But its imposible an living form turn to another living form.We should gratitude for what we have."
    d"Uh...what a pity.Well then I'll pursue it my self"
    bb"I'm sorry,this only I can do for you"
    d"Its okay,I know you do your best"
    "Then Donkey continue her journey"
    jump route_a2

label route_b1:
    bb"Hey I can help you,there's a legend said in the peak of Pompeii Mountain live an Dragon who can grant wish for someone who have good manner and virtue."
    bb"But I dont know if the legend are true, why you dont seek it your self ?"
    d"Thats so far from here,but I'll do it to pursue my dream, thank you Brown Bear !"
    bb"You're welcome, have a nice journey and take care for yourself !"
    d"Yeah ! You too !"
    "Then Donkey continue her journey"
    jump route_b2

label route_a2:
    "In her way to find solution of her problem, Donkey encountered many obstacles.But she did it successfully."
    unk"HELP ! PLEASE SOMEBODY HELP ME !!!"
    d"I hear something, I should go there."
    "Then Donkey went to where the voice come from."
    "Then she found the Rabbit who trapped in rope"
    r "Help me ! They will use me as meat for meal !"
    d "Rabbit ! Hang on I will free you from this rope."
    d "I will try use my teeth, Hopefully it can be useful"
    "She bite the rope, and Its broke !"
    "The Rabbit set free."
    r "My thanks for you Donkey, what i can do to pay my debt for someone who save my life ?"
    d "Uhh...I want to live as Rabbit like you ?"
    r "Like me eh ? Well you should meet the Dragon. She can help you."
    d "Where should I find her ?"
    r "My grandpa said She live on peak of mountain of fire."
    r "Pompeii Mountain"
    d " Well then, thank you very much Rabbit."
    jump story2

label route_b2:
    "Donkey continue her journey, in way to Pompeii Mountain she met an black cat"
    d" Hello black cat !"
    c"hwaaaaaa its you Donkey, what I can do for you my friends ?"
    d"I will go to Pompeii Mountain"
    c"Oh well, may i help you ? You see, I have wagon.I'll tell Horse to escort you there"
    d"Thanks for your offer,but sorry I'll go there alone"
    c"Ah, how about I give you provision for your journey ? You must be hungry right ?"
    d"Uh...I'll take it, my thanks"
    c"Nevermind, you've help me on the past"
    jump story2
    
label story2:
    "Then Donkey continue her journey to Pompeii Mountain"
    "Finally Donkey arrive on Peak of Pompeii Mountain. "
    unk"I've been waiting for you"
    d"Who's there !?"
    unk"It is I the guardian of this Mountain."
    "Suddenly a blue dragon with 2 horn appear from the volcano"
    n"Donkey, welcome to peak of Pompeii Mountain. It is I the Dragon"
    n" I will grant your wishes.But..."
    d"But ?"
    n"Lets see your examination first"

    if route == "a1":
        n "Hmm, Brown Bear told you to stop your dream to become rabbit and you still continue your journey"
        n "And you help the Rabbit and She tell you the secret of this mountain."
        n "A path you choose indeed a way of virtue, but you keep going to pursue your dream."
        n "Indeed thats a way of Rabbit life who never give up and helping the others"
        n "Very well..."
        n "I will turn you into Rabbit as your wish, but you must promise you keep the good habit that you get on your journey"
        jump ending

    if route == "b1":
     n"Brown bear told you the secret of this mountain,eh ?"
     n"And on your way to come here you met the Black Cat"
     n"She offer you a transportation to come here, but instead you take offer of provision so you wouldnt be hungry"
     n"A path you choose indeed a way of virtue,but you still care with your health."
     n"Indeed thats a way of Rabbit who pursue their dream and still care with your health"
     n"But you must remember this, you should know a hard life. You must not life with enough stomach, you must work harder to fill your stomach"
     n"I hope you will learn this Donkey, in your life as Rabbit"
     jump ending

label ending:
    "And then Donkey transformed to Rabbit."
    r "Thank you oh the wise dragon"
    n "You're welcome, now I will return you to your own home"
    "THE END"
    return


