
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

<<<<<<< HEAD
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


image notebook = "images/notebook.png"

screen math_exam():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "#ffffff"
        padding (20, 20)

        vbox:
            spacing 20
            text "Math Exam" size 40 color "#000000" xalign 0.5

            hbox:
                text "1. 2+2 = " color "#000000" size 30
                input id "q1" default "" length 10 color "#000000"

            hbox:
                text "2. lim x->inf (x + 1/x)^x = " color "#000000" size 30
                input id "q2" default "" length 20 color "#000000"


# The game starts here.
label start:

    $ renpy.movie_cutscene("images/1115.webm")

    jump mathexam


label mathexam:
    show notebook:
        xalign 0.5
        ypos 0
        zoom 2.0

    show text "{color=#000000}2+2=" as q1:
        xpos 900
        ypos 172


    show text "{color=#000000}lim x->inf (x + 1/x)^x =" as q2:
        xpos 900
        ypos 330
=======
# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy


    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"
>>>>>>> origin/master

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
    "hello"
    return
<<<<<<< HEAD

label failedmathexam:
    return
=======
>>>>>>> origin/master
