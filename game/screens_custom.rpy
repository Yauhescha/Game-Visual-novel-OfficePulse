# screens_custom.rpy
# Необязательный экран параметров. Можно вызвать: call screen officepulse_stats

screen officepulse_stats():
    tag menu
    add Solid("#111111")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        has vbox
        spacing 16
        text "Параметры OfficePulse" size 44
        text "Репутация у разработки: [dev_rep]"
        text "Репутация у QA: [qa_rep]"
        text "Репутация у менеджера: [manager_rep]"
        text "Репутация у бухгалтерии: [accountant_rep]"
        text "Репутация у DevOps: [devops_rep]"
        text "Качество системы: [tech_quality]"
        text "Технический долг: [tech_debt]"
        text "Этика: [ethics]"
        text "Выгорание: [burnout]"
        text "Абсурд: [absurdity]"
        textbutton "Назад" action Return()
