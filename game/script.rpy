# script.rpy
# Точка входа игры.

label start:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office_entrance with fade
    $ op_clear_sprites()
    n "Визуальная новелла: «Кабинет 2: OfficePulse»."
    n "История о маленьком IT-офисе, внутренней системе, офисной политике, баг-репортах, зарплатных пересмотрах и людях, которые пытаются не сгореть на работе."
    play sound "audio/sfx/notification.ogg"

    $ typed_name = renpy.input("Как зовут главного героя?", default="ГГ").strip()
    if typed_name:
        $ player_name = typed_name
    else:
        $ player_name = "ГГ"

    jump act1_first_day

# =========================
# АКТ 1. НОВИЧОК В КАБИНЕТЕ 2
# =========================
