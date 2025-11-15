

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

define e = Character("gay")


screen framebutton(_xalign,_yalign,_text,_jump):
    #todo use xbox
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


image notebook = "images/notebook.png"


# The game starts here.
label start:

    $ renpy.movie_cutscene("images/1115.webm")

    jump mathexam


# Игра начинается здесь:
label mathexam:

    scene bg room

    show eileen happy

    show notebook:
        xalign 0.5
        ypos 0
        zoom 2.0

    $ answer1 = renpy.input("{color=#FFFFFF}2+2=")
    if answer1.strip() == "4":
        show text "{color=#000000}2+2=4" as q1:
            xpos 900
            ypos 172
    else:
        jump failedmathexam

    #russian e
    $ answer1 = renpy.input("{color=#FFFFFF}lim x->inf (x + 1/x)^x = ")
    if answer1.strip() == "e" or answer1.strip() == "е":
        show text "{color=#000000}lim x->inf (x + 1/x)^x = e" as q2:
            xpos 900
            ypos 330
    else:
        jump failedmathexam
    " "
    return


label failedmathexam:
    return
