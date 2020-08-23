# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Josh = Character("Josh Ong", color = "#44DDDD")
define Brigette = Character("Brigette Simper", color = "#44DDDD")
define Shouko = Character("Shouko Oogushi", color = "#44DDDD")
define Nine = Character("Nine-One Divoc", color = "#44DDDD")
define Alistair = Character("Alistair Moffat", color = "#44DDDD")
define Jessica = Character("Jessica Kim", color = "#44DDDD")
define professor = Character("Professor X", color = "#44DDDD")

# Brigette pics
image Brigette_1 = Image("Brigette_1.jpg")
image Brigette_1b = Image("Brigette_1b.jpg")
image Brigette_2 = Image("Brigette_2.jpg")
image Brigette_2b = Image("Brigette_2b.jpg")
image Brigette_3 = Image("Brigette_3.jpg")
image Brigette_3b = Image("Brigette_3b.jpg")

# Josh pics
image Josh_1 = Image("josh_1.jpg")
image Josh_2 = Image("josh_2.jpg")
image Josh_room = Image("josh_room.png")

# Nine pics
image Nine_1 = Image("nine_1.jpg")

# Shouko pics

# Jessica pics

# Alistair pics


# Image positions
transform top_left_screen:
    xalign 0.1
    yalign 0.1

transform top_right_screen:
    xalign 0.9
    yalign 0.1

transform bottom_screen:
    xalign 0.5
    yalign 0.8

transform middle:
    xalign 0.5
    yalign 0.5


# Backgrounds
image bedroom = Image("bedroom.jpg")
image main_room = Image("home_space.png")
image breakout_transition = Image("transition.jpg")
image blue_screen = Image("blue_screen.jpg")
image blank = Solid("#000000")


#-----
# the main program
label start:

    $ num_team_members = 0

    $ Josh_angry = False
    $ Brigette_angry = False
    $ Shouko_angry = False
    $ Nine_angry = False
    $ Alistair_angry = False
    $ Jessica_angry = False

    $ Josh_joined_team = False
    $ Brigette_joined_team = False
    $ Shouko_joined_team = False
    $ Nine_joined_team = False
    $ Alistair_joined_team = False
    $ Jessica_joined_team = False

    call disclaimer_scene
    call intro
    call online_class_scene
    call player_instructions

    # breakout room 1
    scene breakout_transition
    centered "You are being moved to outbreak group 1"
    menu:
        "Would you like to join the conversation or skip this group?"

        "Join the conversation":
            call breakout_room_1
            pass
        "Quiet watch the other students like a {i}creepy{/i} ninja (skip)":
            call skip_breakout_1
            pass

    if num_team_members >= 2:
        player "I've got my teammates secured, looks like I can go back to sleep. Stuff the rest of the class."
        call end_game
        return

    # breakout room 2
    scene breakout_transition
    centered "You are being moved to outbreak group 2"
    menu:
        "Would you like to join the conversation or skip this group?"

        "Join the conversation":
            call breakout_room_2
            pass
        "Quietly observe in order to not disturb the natural habitat of awkward university students (skip)":
            call skip_breakout_2
            pass

    if num_team_members >= 2:
        player "I've got my teammates secured, looks like I can go back to sleep. Stuff the rest of the class."
        call end_game
        return

    # breakout room 3
    scene breakout_transition
    centered "You are being moved to outbreak group 3"
    centered "Guess you're going to join the conversation this time... instead of being a mannequin."
    call breakout_room_3
    call end_game

    # finish
    return



#---
# disclaimer for the product
label disclaimer_scene:
    scene blank
    centered "Disclaimer: This work is purely fictional."
    centered "Disclaimer Jr. : Obscene language is mostly censored, but is present in the storyline."
    return


#---
# wake up scene
label intro:
    scene bedroom
    "{i}It's a nice summer day in quarantine."
    "{i}You've just woken up, feeling really tired from last night's League grind."
    "{i}In fact, you're so tired, you don't remember your own name."
    "{i}Wait no for real... what is your name?"
    $ player_name = renpy.input("{i}{b}What is your name?", "Enter name", length=20)

    define player = Character("Me", color = "#666600")

    player "* Ah of course, of course, my name is [player_name]... what a dumbass I am. *"
    "{i}As you start to remind yourself of your own name. You also
    realise that you have to make a very important decision."
    player "* Hmmm my Design of Algorithms tutorial starts in 1 minute. I \
    should get the computer... OR, I could go back to sleep. *"

    menu:
        "Go back to sleep":
            player "* Arggh, but I can't ditch 3 classes in a row. Damn it! *"

            pass
        "Get the computer":
            pass

    player "* Welp, it's gonna be a long day. *"

    "{i}You open the computer and log in to your online class."
    return


#---
# first scene when joining online class
label online_class_scene:
    scene main_room
    player "* Ah... everyone's here already. *"
    professor "Of course! It's the one and only [player_name] who makes us wait again."
    professor "Tell me, [player_name], do you find pleasure in holding us up every single CLASS?"
    menu:
        "Well... kinda":
            professor "I see. We're going to have a very friendly chat after class."
        "No sir, I'm very sorry. It won't happen again.":
            professor "Yeah yeah, same old trick, I've heard enough from you"

    professor "Alright everyone, let's finally start. Today's class is {b}very important{/b}. As you already know, we have already released the project for this semester."
    professor "If you need a quick recap, we're going to make a very basic computer program. You need to implement a polymorphic hash table."
    professor "We may give you numbers as input, we may give you strings as input, heck we may even give you hash tables as input."
    professor "Your task is to make sure that when provided with a valid hash function, your program will work for any given type of input."
    professor "The goal of the project is not only for you to become godlike programmers, but also to allow some of you find some friends... since that's a rare occurrence in the computing world."
    professor "Alright, enough talking, I'm going to put you guys into different outbreak rooms, you will be sent to 3 different breakout rooms, you should talk to one another to find out who you would like to team up with."
    professor "You need exactly 2 teammates for the project. Remember, if you pick the right people, they'll help you get a better mark for the subject. If you pick the wrong people... well, just don't pick the wrong people."
    "{i}Feels like the professor was looking at you when he said that last part... but hey, the camera's turned off, he couldn't have been."
    professor "Okay off you go."
    return


#---
# Instruction screen
label player_instructions:
    scene blank
    centered "{b}{size=40}Instructions{/size}{/b} \n
    \n\n
    1. You will be put into 3 different outbreak rooms, one at a time, each with 2 other students. \n
    2. You are to talk to your peers to learn more about them. \n
    3. At the end of the outbreak room, you may ask them to join your team. \n
    4. You need to invite 2 people into your team, choose wisely... or risk receiving a 50 WAM. \n
    \n\n
    Side note: You can save progress in the menu, if you would like to jump to different sections. \n
    It is recommended that you save progress right here, so you can go back to this starting point without having to redo the intro. \n
    \n\n
    {b}Enjoy!"
    return


#---
# Breakout 1 skip scene
label skip_breakout_1:
    scene blank
    show Josh_1 at top_left_screen
    show Brigette_1b at top_right_screen
    "... ... ... ..."
    Josh "... hehe, check out this cool guitar ...."
    Brigette "... yeah it's so cool... almost as cool as... you ..."
    "... ... ... ... ... ... ... ..."
    return

#---
# Breakout 2 skip scene
label skip_breakout_2:
    scene blank
    show Nine_1 at top_left_screen
    show Shouko_1 at top_right_screen
    "... ... ... ..."
    Nine "... yeah I'm cool like that ...."
    Shouko "...    ..."
    "... ... ... ... ... .... ... ..."
    return

#---
# outro
label outro:
    scene bedroom
    player "Welp... that was an eventful semester. I guess I could do it again."
    return
