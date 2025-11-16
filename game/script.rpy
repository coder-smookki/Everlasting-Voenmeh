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
    jump main_game

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
    
    show mathexam()
    return