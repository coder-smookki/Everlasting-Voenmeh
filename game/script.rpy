# Фон — фотография
image bg classroom = "images/bg/classroom.png"

# Спрайты
image gg normal = At("images/characters/gg/gg_day1_nuetral.png", Transform(zoom=1.3))
image friend normal = At("images/characters/nerd/nerd_neutral.png", Transform(zoom=1.3))

# Позиции
define left_pos = Position(xalign=-0.1, ypos=1.4)
define right_pos = Position(xalign=1.1, ypos=1.4)

# Стиль для текста диалога
style say_dialogue:
    color "#FFFFFF"
    size 50
    text_align 0  # Выравнивание по центру
    xalign 0      # По центру по горизонтали
    xpos 0.19
    yalign 0.5

# Стиль для имени персонажа
style say_label:
    color "#FFFFFF"
    size 50
    bold True

# Персонажи для диалогов с разными позициями окон
define g = Character("Гланый Герой", color="#ff0000", what_style="say_dialogue", who_style="say_label")
define f = Character("Ботаник", color="#ffbf00", what_style="say_dialogue", who_style="say_label")
label start:
    # Проигрываем видео 47 секунд
    play movie "images/video/intro.webm"
    # $ renpy.pause(47.0, hard=False)
    stop movie fadeout 1.0
    jump mathexam

label main_game:
    scene bg classroom
    
    # Друг говорит - показываем только его справа
    show friend normal at right_pos
    f "Я же говорил, об этом месте слабают легенды"
    
    # ГГ отвечает - показываем только его слева
    show gg normal at right_pos
    hide friend  # скрываем предыдущего говорящего
    g "Да, это место действительно впечатляет!"
    
    # Друг снова говорит - показываем только его
    show friend normal at right_pos
    hide gg  # скрываем ГГ
    f "Я читал, что здесь происходили странные вещи..."

    return

image notebook = "images/objects/notebook.png" 

style booktext:
    size 50
    color"#000000"

style limittext:
    size 25
    color"#000000"


default strq1 = "2+2 * 2 = "
default strq2 = "4! + 1 = "
default strq3 = "lim sin(x)/x = "
default strq4 = "lim (3x+1)/x = "
default strq5 = "lim x/ln(x) = "

default int_answer1 = 6
default int_answer2 = 25
default int_answer3 = 1
default int_answer4 = 3
default int_answer5 = 0

image question1 = Text("2+2 * 2 = ", style="booktext")
image question2 = Text("4! + 1 = ", style="booktext")
image question3 = Text("lim sin(x)/x = ", style="booktext")
image question4 = Text("lim (3x+1)/x = ", style="booktext")
image question5 = Text("lim x/ln(x) = ", style="booktext")

image xapproachinginf = Text("x->inf",style="limittext")
image xapproaching0 = Text("x->0",style="limittext")

default correct_answers_list = []
label mathexam:
    $ yposnotebook = -56
    $ sizebetween = 80
    $ yunderlimit = 45
    $ xunderlimit = 10
    $ yshift = 85
    $ yfirst = 230

    show notebook:
        zoom 2.0
        xalign 0.5
        ypos yposnotebook
    
    show question1 as q1:
        xpos 700
        ypos yfirst
    

    show question2 as q2:
        xpos 700
        ypos yfirst + yshift

    show question3 as q3:
        xpos 700
        ypos yfirst + 2*yshift 
    
    show xapproaching0:
        xpos 700 + xunderlimit
        ypos yfirst + 2*yshift  + yunderlimit

    show question4 as q4:
        xpos 700
        ypos yfirst + 3*yshift 
    
    show xapproachinginf:
        xpos 700 + xunderlimit
        ypos yfirst + 3*yshift  + yunderlimit

    show question5 as q5:
        xpos 700
        ypos yfirst + 4*yshift 

    show xapproaching0:
        xpos 700 + xunderlimit
        ypos yfirst + 4*yshift + yunderlimit

    $ user_answer1 = renpy.input("Введите ваш результат:",allow="-01234567890",length = 4)
    $ answer_on_question = strq1 + user_answer1
    show image Text("[answer_on_question]",style="booktext") as q1:
        xpos 700
        ypos yfirst
    
    $ correct_answers_list.append(user_answer1.isnumeric() and int(user_answer1) == int_answer1)

    $ user_answer2 = renpy.input("Введите ваш результат:",allow="-01234567890",length = 4)
    $ answer_on_question  = strq2 + user_answer2
    show image Text("[answer_on_question]",style="booktext") as q2:
        xpos 700
        ypos yfirst + yshift 

    $ correct_answers_list.append(user_answer2.isnumeric() and (int(user_answer2) == int_answer2))

    $ user_answer3 = renpy.input("Введите ваш результат:",allow="-01234567890",length = 4)
    $ answer_on_question  = strq3 + user_answer3
    show image Text("[answer_on_question]",style="booktext") as q3:
        xpos 700
        ypos yfirst + 2*yshift 
        
    $ correct_answers_list.append(user_answer3.isnumeric() and (int(user_answer3) == int_answer3))


    $ user_answer4 = renpy.input("Введите ваш результат:",allow="-01234567890",length = 4)
    $ answer_on_question  = strq4 + user_answer4
    show image Text("[answer_on_question]",style="booktext") as q4:
        xpos 700
        ypos yfirst + 3*yshift 
        
    $ correct_answers_list.append(user_answer4.isnumeric() and (int(user_answer4) == int_answer4))

    $ user_answer5 = renpy.input("Введите ваш результат:",allow="-01234567890",length = 4)
    $ answer_on_question  = strq5 + user_answer5
    show image Text("[answer_on_question]",style="booktext") as q5:
        xpos 700
        ypos yfirst + 4*yshift 
        
    $ correct_answers_list.append(user_answer5.isnumeric() and (int(user_answer5) == int_answer5))

    $ correct_answers_count = sum(correct_answers_list)  
    "кхм-кхм дайте посмотреть"

    $ true_answer1 = "".join([strq1 ,"{b}",("{color=#22792B}" if correct_answers_list[0] else "{color=#FF0000}"),user_answer1,"" if correct_answers_list[0] else "{/color}","{/b}"])
    $ true_answer2 = "".join([strq2 ,"{b}",("{color=#22792B}" if correct_answers_list[1] else "{color=#FF0000}"),user_answer2,"" if correct_answers_list[1] else "{/color}","{/b}"])
    $ true_answer3 = "".join([strq3 ,"{b}",("{color=#22792B}" if correct_answers_list[2] else "{color=#FF0000}"),user_answer3,"" if correct_answers_list[2] else "{/color}","{/b}"])
    $ true_answer4 = "".join([strq4 ,"{b}",("{color=#22792B}" if correct_answers_list[3] else "{color=#FF0000}"),user_answer4,"" if correct_answers_list[3] else "{/color}","{/b}"])
    $ true_answer5 = "".join([strq5 ,"{b}",("{color=#22792B}" if correct_answers_list[4] else "{color=#FF0000}"),user_answer5,"" if correct_answers_list[4] else "{/color}","{/b}"])

    show image Text("[true_answer1]",style="booktext") as q1:
        xpos 700
        ypos yfirst 
    show image Text("[true_answer2]",style="booktext") as q2:
        xpos 700
        ypos yfirst + yshift
    show image Text("[true_answer3]",style="booktext") as q3:
        xpos 700
        ypos yfirst + 2*yshift  
    show image Text("[true_answer4]",style="booktext") as q4:
        xpos 700
        ypos yfirst + 3*yshift  
    show image Text("[true_answer5]",style="booktext") as q5:
        xpos 700
        ypos yfirst + 4*yshift  
        
    "количество правильных ответов: [correct_answers_count]"
    "end"
    "end"
    return