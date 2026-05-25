# screens.rpy
# Упрощенные экраны OfficePulse без зависимости от стандартного gui.rpy Ren'Py.

init offset = -1

default quick_menu = True

screen say(who, what):
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1920
        ysize 300
        background Frame("images/ui/textbox.png", 42, 42)

        if who is not None:
            frame:
                xpos 52
                ypos 14
                xminimum 280
                yminimum 58
                background Frame("images/ui/namebox.png", 24, 24)
                text who id "who":
                    xalign 0.5
                    yalign 0.5
                    size 34
                    color "#dceeff"

        text what id "what":
            xpos 68
            ypos 92
            xsize 1780
            size 31
            color "#ffffff"

screen input(prompt):
    modal True
    add Solid("#00000099")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1150
        ysize 260
        background Solid("#111111EE")
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 28
            text prompt xalign 0.5 size 32 color "#ffffff"
            input id "input" xalign 0.5 size 32 color "#66c1ff"

screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.66
        spacing 14
        for i in items:
            textbutton i.caption:
                action i.action
                xsize 1200
                background Frame("images/ui/choice_idle.png", 34, 18)
                hover_background Frame("images/ui/choice_hover.png", 34, 18)
                padding (24, 16)
                text_size 30
                text_color "#ffffff"
                text_hover_color "#66c1ff"
                text_xalign 0.5

screen main_menu():
    tag menu
    add Solid("#050505")
    vbox:
        xpos 90
        ypos 120
        spacing 24
        text "Кабинет 2: OfficePulse" size 64 color "#ffffff"
        null height 20
        textbutton "Начать" action Start() text_size 34 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Загрузить" action ShowMenu("load") text_size 34 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Настройки" action ShowMenu("preferences") text_size 34 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Об игре" action ShowMenu("about") text_size 34 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Выход" action Quit(confirm=True) text_size 34 text_color "#ffffff" text_hover_color "#ff8a8a"

screen navigation():
    vbox:
        xpos 60
        ypos 110
        spacing 14
        textbutton "Назад" action Return() text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "История" action ShowMenu("history") text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Сохранить" action ShowMenu("save") text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Загрузить" action ShowMenu("load") text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Настройки" action ShowMenu("preferences") text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
        textbutton "Главное меню" action MainMenu() text_size 28 text_color "#ffffff" text_hover_color "#ffcc66"

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 24
            text title size 46 color "#ffffff"
            transclude

screen save():
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 28
            text "Сохранение" size 46 color "#ffffff"
            grid 3 3:
                spacing 18
                for i in range(1, 10):
                    button:
                        action FileSave(i)
                        xsize 440
                        ysize 150
                        background Solid("#222222DD")
                        hover_background Solid("#333333EE")
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8
                            text "Слот [i]" xalign 0.5 size 28 color "#ffffff"
                            text FileTime(i, format="%d.%m.%Y %H:%M", empty="Пусто") xalign 0.5 size 22 color "#bbbbbb"

screen load():
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 28
            text "Загрузка" size 46 color "#ffffff"
            grid 3 3:
                spacing 18
                for i in range(1, 10):
                    button:
                        action FileLoad(i)
                        xsize 440
                        ysize 150
                        background Solid("#222222DD")
                        hover_background Solid("#333333EE")
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8
                            text "Слот [i]" xalign 0.5 size 28 color "#ffffff"
                            text FileTime(i, format="%d.%m.%Y %H:%M", empty="Пусто") xalign 0.5 size 22 color "#bbbbbb"

screen preferences():
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 28
            text "Настройки" size 46 color "#ffffff"
            hbox:
                spacing 20
                textbutton "Окно/Полный экран" action Preference("display", "toggle") text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
                textbutton "Пропуск: весь текст" action Preference("skip", "toggle") text_size 28 text_color "#ffffff" text_hover_color "#66c1ff"
            text "Музыка" size 28 color "#ffffff"
            bar value Preference("music volume") xsize 700
            text "Звуки" size 28 color "#ffffff"
            bar value Preference("sound volume") xsize 700
            text "Скорость текста" size 28 color "#ffffff"
            bar value Preference("text speed") xsize 700
            text "Автопереход" size 28 color "#ffffff"
            bar value Preference("auto-forward time") xsize 700

screen history():
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 20
            text "История" size 46 color "#ffffff"
            text "История диалогов в этой минимальной сборке не настроена. Это можно заменить стандартным history-screen позже." size 28 color "#cccccc" xsize 1350

screen about():
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 20
            text "Кабинет 2: OfficePulse" size 46 color "#ffffff"
            text "Черновая Ren'Py-сборка офисной визуальной новеллы. Все изображения сейчас являются плейсхолдерами и могут быть заменены без изменения сценария." size 28 color "#cccccc" xsize 1350

screen help():
    tag menu
    add Solid("#050505")
    use navigation
    frame:
        xpos 360
        ypos 70
        xsize 1500
        ysize 940
        background Solid("#111111EE")
        vbox:
            xpos 40
            ypos 40
            spacing 20
            text "Помощь" size 46 color "#ffffff"
            text "ЛКМ / Enter — продолжить. Esc — меню. Ctrl — пропуск текста." size 28 color "#cccccc"

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#000000AA")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 300
        background Solid("#111111F2")
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 28
            text message xalign 0.5 text_align 0.5 size 30 color "#ffffff" xsize 780
            hbox:
                xalign 0.5
                spacing 40
                textbutton "Да" action yes_action text_size 30 text_color "#ffffff" text_hover_color "#66c1ff"
                textbutton "Нет" action no_action text_size 30 text_color "#ffffff" text_hover_color "#ff8a8a"

screen notify(message):
    zorder 100
    frame:
        xalign 0.5
        yalign 0.08
        background Solid("#222222DD")
        padding (24, 14)
        text message size 24 color "#ffffff"
    timer 3.25 action Hide("notify")

screen skip_indicator():
    zorder 100
    frame:
        xalign 0.96
        yalign 0.04
        background Solid("#222222DD")
        padding (16, 10)
        text "Пропуск..." size 22 color "#ffffff"

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            xalign 0.5
            yalign 0.985
            spacing 18
            textbutton "Назад" action Rollback() text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"
            textbutton "История" action ShowMenu("history") text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"
            textbutton "Пропуск" action Skip() alternate Skip(fast=True, confirm=True) text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"
            textbutton "Авто" action Preference("auto-forward", "toggle") text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"
            textbutton "Сохр." action ShowMenu("save") text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"
            textbutton "Загр." action ShowMenu("load") text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"
            textbutton "Настр." action ShowMenu("preferences") text_size 18 text_color "#bbbbbb" text_hover_color "#ffffff"

# NVL в сценарии не используется, но экран оставлен для совместимости.
screen nvl(dialogue, items=None):
    window:
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 800
        background Solid("#000000CC")
        vbox:
            xpos 40
            ypos 40
            spacing 20
            for d in dialogue:
                if d.who:
                    text "[d.who]: [d.what]" size 28 color "#ffffff"
                else:
                    text d.what size 28 color "#ffffff"
            if items:
                for i in items:
                    textbutton i.caption action i.action text_size 28 text_color "#66c1ff"
