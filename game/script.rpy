# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("gay")


/home/candy/Documents/game/voenmeh/game/images
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



#image imagehover1: "images/button_hover.pgn" xysize(100, 100)
#image imageidle1: "images/button_idle.pgn" xysize(100, 100)
# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    default dr Drawable("images/gay.png",(500,500))

    $ renpy.show(a.path,[Position(xypos[0],xypos[1])])
    # Position gay.png at coordinates 1300, 800
    show gay at Position(xpos=1300, ypos=800)
    
    #call screen framebutton(0.8,0.2,"идти домой","home")
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "choose"

        "choice 1":
            e "go to home"
            jump home
        "choice 2":
            e "2"
        "choice 3":
            e "3"
        "choice 4":
            e "4"
        "choice 5":
            e "5"
        "choice 6":
            e "6"

    # This ends the game.

    return

label home:
    scene bg home
    "you went home"
    return