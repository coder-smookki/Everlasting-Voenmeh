# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("gay")


screen framebutton(_xalign,_yalign,_text,_jump):
    frame:
        xpadding 30
        ypadding 10
        xalign _xalign
        yalign _yalign
        textbutton _text action [ToggleScreen("framebutton"),Jump(_jump)]


screen image_button(_idle,_hover,_xalign,_yalign,_action):
    imagebutton:
        xalign _xalign
        yalign _yalign

        idle _idle
        hover _hover
        action [ToggleScreen("image_button"),_action]


# Play the intro video
#DOES NOT SUPPORT mp4

# The game starts here.
label start:


    $ renpy.movie_cutscene("images/1115.webm")

    return

