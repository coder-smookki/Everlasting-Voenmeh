# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("gay")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # Show random squares
    show square1 at Position(xpos=200, ypos=200)
    show square2 at Position(xpos=400, ypos=300)
    show square3 at Position(xpos=600, ypos=150)
    show square4 at Position(xpos=800, ypos=400)
    show square5 at Position(xpos=1000, ypos=250)

    # Position gay.png at coordinates 1300, 800
    show gay at Position(xpos=1300, ypos=800)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "choose"
        "choice 1":
            e "1"
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

    return