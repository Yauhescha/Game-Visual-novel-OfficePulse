# routes/route_career.rpy

label route_career_start:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_day with fade
    $ op_clear_sprites()
    n "После демо руководство заинтересовалось OfficePulse. Не потому, что система помогала людям. Потому что она могла считать людей."

    $ op_set_emotion("manager", "business")
    manager "Есть идея. Использовать OfficePulse для пересмотра зарплат и оценки эффективности."
    $ op_set_emotion("young_accountant", "worried")
    youngacc "Осторожно. Метрики без контекста могут быть опасны."
    $ op_set_emotion("qa_lead", "serious")
    qalead "Метрики хотя бы честнее личных симпатий."
    $ op_set_emotion("dev_lead", "angry")
    devlead "Если метрики не понимают суть работы, они хуже симпатий. Симпатии хотя бы не притворяются объективными."

    $ op_set_emotion("gg", "neutral")
    p "Какие показатели хотят видеть?"
    $ op_set_emotion("manager", "smile")
    manager "Количество закрытых задач, возвраты с QA, критичные баги, переработки, скорость реакции, участие в инцидентах, конфликтные комментарии."
    $ op_set_emotion("devops", "tired")
    devops "Конфликтные комментарии? А как система поймет, что комментарий конфликтный?"
    $ op_set_emotion("manager", "smile")
    manager "Можно по ключевым словам."
    $ op_set_emotion("silent_senior", "comment")
    senior "Поздравляю. Мы изобрели донос с регулярными выражениями."

    menu:
        "Как строить карьерный модуль?"

        "Только командные метрики и контекст":
            $ ethics += 2
            $ tech_quality += 1
            $ control -= 1
            $ op_set_emotion("gg", "neutral")
            p "Я не буду делать индивидуальную доску позора. Только командные метрики, контекст, история и право объяснения."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Слишком мягко."
            $ op_set_emotion("young_accountant", "smile")
            youngacc "Зато меньше шансов сломать людям карьеру одной цифрой."
            jump career_review_scene

        "Индивидуальные метрики, но с правом комментария":
            $ ethics += 1
            $ control += 1
            $ op_set_emotion("gg", "neutral")
            p "Индивидуальные метрики можно, но обязательно с правом комментария сотрудника и отметкой спорных случаев."
            $ op_set_emotion("dev_lead", "serious")
            devlead "Это компромисс. Не идеальный, но живой."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Если комментарии не превращаются в оправдания — допустимо."
            jump career_review_scene

        "Полный контроль: индивидуальные рейтинги, конфликты, опоздания":
            $ control += 4
            $ ethics -= 3
            $ op_set_emotion("gg", "neutral")
            p "Если делать, то честно: рейтинги, возвраты, опоздания, конфликты, срочные просьбы, все в одном дашборде."
            $ op_set_emotion("young_accountant", "neutral")
            youngacc "Это не честность. Это наблюдение."
            $ op_set_emotion("manager", "business")
            manager "Но руководству будет полезно."
            $ op_set_emotion("devops", "angry")
            devops "Руководству всегда полезно то, что потом будет больно всем остальным."
            jump career_review_scene

        "Отказаться делать модуль для пересмотров":
            $ ethics += 2
            $ manager_rep -= 2
            $ op_set_emotion("gg", "serious")
            p "OfficePulse не должен становиться автоматом для зарплатных решений. Я не хочу делать модуль пересмотра в таком виде."
            $ op_set_emotion("manager", "guilty")
            manager "Это может выглядеть как отказ от важной бизнес-задачи."
            $ op_set_emotion("gg", "serious")
            p "Пусть выглядит. Некоторые задачи опасны, если их сделать слишком хорошо."
            jump career_review_scene

label career_review_scene:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_salary_review with fade
    $ op_clear_sprites()
    n "День пересмотров зарплат пришел, как плохой релиз: все знали дату, но никто не был готов."

    $ op_set_emotion("old_accountant", "strict")
    oldacc "Премии считать будем по фактам или по ощущениям?"
    $ op_set_emotion("qa_lead", "neutral")
    qalead "По качеству."
    $ op_set_emotion("dev_lead", "serious")
    devlead "По вкладу."
    $ op_set_emotion("manager", "smile")
    manager "По показателям."
    $ op_set_emotion("devops", "tired")
    devops "По выжившим."
    $ op_set_emotion("young_accountant", "neutral")
    youngacc "По методике, которую все понимают. Желательно до того, как увидят результат."

    n "Виктор открыл список тестировщиков. Имя Кирилла было подсвечено красным: много возвратов багов на доработку, низкая точность описаний."
    show ui_officepulse_salary_report at ui_panel_right

    $ op_set_emotion("qa_intern", "scared")
    qaintern "Я правда старался."
    $ op_set_emotion("qa_lead", "angry")
    qalead "Стараться недостаточно. Нужно уметь."
    $ op_set_emotion("manual_qa", "neutral")
    manualqa "Он стажер."
    $ op_set_emotion("manual_qa", "tired")
    manualqa "Его надо учить, а не сравнивать с лидом."
    $ op_set_emotion("auto_qa", "neutral")
    autoqa "Если метрика не учитывает уровень человека, она бесполезна."
    $ op_set_emotion("auto_qa", "angry")
    autoqa "Иначе она просто измеряет возраст в профессии."

    menu:
        "Как использовать данные на пересмотре?"

        "Добавить уровень, контекст и наставничество":
            $ ethics += 2
            $ qa_rep += 1
            $ tech_quality += 1
            $ op_set_emotion("gg", "neutral")
            p "Метрика Кирилла должна сравниваться с ожиданиями стажера, а не лида. И рядом должны быть отметки наставничества."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Слишком мягко."
            $ op_set_emotion("qa_halflead", "smile")
            qahalf "Нет. Это наконец-то честно."
            $ op_set_emotion("qa_intern", "confused")
            qaintern "Спасибо."
            jump career_final_choice

        "Поддержать жесткую позицию QA-лида":
            $ qa_rep += 1
            $ control += 2
            $ ethics -= 1
            $ op_set_emotion("gg", "serious")
            p "Данные показывают проблему. Если человек заводит слабые баги, это влияет на команду."
            $ op_set_emotion("qa_intern", "scared")
            qaintern "Понял."
            n "Он сказал это тихо. Слишком тихо."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Холодно, но верно."
            jump career_final_choice

        "Защитить разработчиков от QA-метрик":
            $ dev_rep += 2
            $ qa_rep -= 1
            $ op_set_emotion("gg", "serious")
            p "По разработчикам нельзя считать только возвраты. Нужно отделять реальные дефекты от спорных требований."
            $ op_set_emotion("dev_lead", "neutral")
            devlead "Вот об этом я говорил."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "А я говорил, что разработчики всегда найдут способ назвать баг спорным требованием."
            jump career_final_choice

        "Показать скрытый дашборд контроля руководству":
            show ui_officepulse_dashboard at ui_panel_big
            $ control += 4
            $ ethics -= 4
            $ op_set_emotion("gg", "neutral")
            p "Есть еще расширенный дашборд. Он показывает конфликты, опоздания, срочные просьбы, правки истории и влияние на пересмотры."
            $ op_set_emotion("young_accountant", "neutral")
            youngacc "Ты сделал это без обсуждения?"
            $ op_set_emotion("gg", "neutral")
            p "Я сделал то, что покажет полную картину."
            $ op_set_emotion("devops", "tired")
            devops "Нет. Ты сделал камеру наблюдения и назвал ее картиной."
            jump career_final_choice

label career_final_choice:
    $ op_clear_sprites()
    play music "audio/music/night.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene bg_meeting_room_evening with fade
    $ op_clear_sprites()
    n "После пересмотра я остался один в переговорке. На экране был OfficePulse. Система больше не была просто кодом. Она стала решением о людях."
    show ui_officepulse_dashboard at ui_panel_big

    menu:
        "Какой принцип заложить в финальную версию?"

        "Система должна помогать людям исправлять процесс":
            $ ethics += 3
            $ tech_quality += 2
            $ audit_enabled = True
            $ op_set_emotion("gg", "neutral")
            p "OfficePulse не должен быть судьей. Он должен быть протоколом, картой и предупреждением. Решения должны принимать люди — с фактами и контекстом."
            jump finale_gate

        "Система должна показывать, кто слабое звено":
            $ control += 4
            $ ethics -= 3
            $ op_set_emotion("gg", "serious")
            p "Если данные показывают слабых — значит, их надо видеть. Офис не обязан быть комфортным для всех."
            jump finale_gate

        "Система должна быть удобной руководству":
            $ manager_rep += 2
            $ control += 2
            $ ethics -= 1
            $ op_set_emotion("gg", "neutral")
            p "Если руководству нужен инструмент управления, я сделаю его. Контекст добавим, но главное — понятность решений."
            jump finale_gate

        "Система должна быть минимальной, чтобы не разрушить офис":
            $ tech_quality -= 1
            $ ethics += 1
            $ op_set_emotion("gg", "serious")
            p "Лучше ограничить функциональность. Некоторые данные слишком опасны для маленького офиса."
            jump finale_gate

# =========================
# ФИНАЛЬНЫЕ РАЗВИЛКИ
