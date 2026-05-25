# routes/route_absurd.rpy

label route_absurd_start:
    $ op_clear_sprites()
    play music "audio/music/absurd.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_day with fade
    $ op_clear_sprites()
    n "Китайская линия началась с нормальных требований и очень быстро перешла в корпоративную метафизику."

    $ op_set_emotion("manager", "smile")
    manager "Ребята, от китайских коллег пришел обновленный документ. Не пугайтесь, там всего двенадцать страниц."
    play sound "audio/sfx/notification.ogg"
    $ op_set_emotion("frontend_dev", "neutral")
    fe "Вчера было три."
    $ op_set_emotion("manager", "smile")
    manager "Они структурировали мысли."
    $ op_set_emotion("silent_senior", "comment")
    senior "Если мысль выросла в четыре раза за ночь, это не структура. Это опухоль."

    china "Button Reject must exist, but user should not reject. It should guide to positive refusal."
    $ op_set_emotion("manager", "smile")
    manager "Они хотят кнопку 'Отклонить', которая не отклоняет, а ведет к позитивному отказу."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Это как?"
    $ op_set_emotion("frontend_dev", "neutral")
    fe "Кнопка 'Я согласен, что не согласен'."
    $ op_set_emotion("devops", "tired")
    devops "Добавьте сразу кнопку 'Починить прод, но без изменений'."

    menu:
        "Как реагировать на абсурдные требования?"

        "Требовать нормальную аналитику и четкие формулировки":
            $ tech_quality += 2
            $ manager_rep -= 1
            $ absurdity -= 1
            $ op_set_emotion("gg", "neutral")
            p "Алена, без нормальных формулировок мы будем писать не систему, а гороскоп. Нужно уточнение по каждому пункту."
            $ op_set_emotion("manager", "smile")
            manager "Они могут воспринять это как нежелание сотрудничать."
            $ op_set_emotion("gg", "neutral")
            p "Лучше так, чем сотрудничать с туманом."
            $ op_set_emotion("qa_lead", "smirk")
            qalead "Редкий случай, когда я согласен с разработчиком."
            jump absurd_call

        "Сделать все настройками":
            $ absurdity += 3
            $ tech_debt += 2
            $ manager_rep += 2
            $ chinese_mode_enabled = True
            $ op_set_emotion("gg", "neutral")
            p "Сделаем конфигурацию: названия кнопок, статусы, видимость действий, отчеты. Пусть каждый офис настраивает свою реальность."
            $ op_set_emotion("frontend_dev", "neutral")
            fe "То есть мы делаем конструктор корпоративной правды."
            $ op_set_emotion("silent_senior", "neutral")
            senior "С архитектурной точки зрения — ужасно. С исторической — неизбежно."
            jump absurd_call

        "Предложить отдельный китайский режим":
            $ chinese_mode_enabled = True
            $ absurdity += 2
            $ tech_quality += 1
            $ op_set_emotion("gg", "neutral")
            p "Сделаем отдельный режим для китайского офиса, но сохраним общий внутренний тип данных."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Если в базе дефект остается дефектом — я переживу мягкий UI."
            $ op_set_emotion("manager", "smile")
            manager "Отлично. Я назову это 'regional adaptation'."
            $ op_set_emotion("devops", "tired")
            devops "Я назову это 'почему у нас два прода'."
            jump absurd_call

        "Без сопротивления принять все в текущий релиз":
            $ absurdity += 4
            $ tech_debt += 4
            $ burnout += 2
            $ op_set_emotion("gg", "neutral")
            p "Ладно. Берем в текущий релиз."
            $ op_set_emotion("devops", "angry")
            devops "Я пошел писать завещание для стенда."
            $ op_set_emotion("silent_senior", "neutral")
            senior "В PR меня не добавляй. Я не хочу быть свидетелем."
            jump absurd_call

label absurd_call:
    $ op_clear_sprites()
    play music "audio/music/absurd.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_call_screen with fade
    $ op_clear_sprites()
    play sound "audio/sfx/call.ogg"
    scene cg_chinese_call with fade
    $ op_clear_sprites()
    n "Созвон с китайскими коллегами назначили на семь утра. Костя пришел с кофе. Паша — с пустым взглядом. Алена — с улыбкой человека, который уже понял, что будет больно."
    play sound "audio/sfx/call.ogg"

    china "Red status is too aggressive. But green status is too successful. Need color of serious harmony."
    $ op_set_emotion("manager", "smile")
    manager "Им нужен цвет серьезной гармонии."
    $ op_set_emotion("frontend_dev", "annoyed")
    fe "Я увольняюсь в монастырь дизайна."
    $ op_set_emotion("gg", "neutral")
    p "Какого цвета серьезная гармония?"
    $ op_set_emotion("manager", "smile")
    manager "Они прислали пример."
    n "Алена показала скриншот. На нем был красный цвет."
    show ui_officepulse_chinese_mode at ui_panel_right
    $ op_set_emotion("frontend_dev", "annoyed")
    fe "Это красный."
    $ op_set_emotion("manager", "smile")
    manager "Но они пишут, что это не красный. Это responsible coral."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Ответственный коралл. Звучит как должность в QA."

    $ op_set_emotion("qa_lead", "neutral")
    qalead "Меня больше волнует не цвет. Если статус критичный, он должен быть критичным."
    $ op_set_emotion("manager", "smile")
    manager "Но они не хотят, чтобы пользователи чувствовали вину."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Пользователь должен чувствовать вину, если он сломал процесс. Это часть обучения."
    $ op_set_emotion("qa_halflead", "serious")
    qahalf "Виктор, не все обучение должно быть через вину."

    menu:
        "Что сделать с цветами и статусами?"

        "Добавить темы оформления для офисов":
            $ absurdity += 2
            $ tech_debt += 1
            $ op_set_emotion("gg", "neutral")
            p "Добавим темы оформления. Но семантика статуса останется единой."
            $ op_set_emotion("frontend_dev", "annoyed")
            fe "Я могу сделать. Но если появится цвет 'осторожно-радостный желтый', я уйду."
            $ op_set_emotion("manager", "guilty")
            manager "Не обещаю."

        "Отказаться менять семантику критичных статусов":
            $ tech_quality += 2
            $ qa_rep += 1
            $ op_set_emotion("gg", "serious")
            p "Цвет можно обсуждать. Но критичный статус должен оставаться критичным. Нельзя прятать риск в палитре."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Поддерживаю."
            $ op_set_emotion("manager", "guilty")
            manager "Я передам. Мягко. Очень мягко."

        "Сделать статус 'Критичное улучшение'":
            $ absurdity += 3
            $ manager_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Можно назвать это 'Критичное улучшение'."
            $ op_set_emotion("devops", "tired")
            devops "Прод упал. У нас критичное улучшение доступности."
            $ op_set_emotion("frontend_dev", "neutral")
            fe "Я нарисую иконку огня с улыбкой."
            $ op_set_emotion("qa_lead", "angry")
            qalead "Я вас всех ненавижу."

    jump absurd_demo_disaster

label absurd_demo_disaster:
    $ op_clear_sprites()
    play music "audio/music/release_crisis.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_day with fade
    $ op_clear_sprites()
    n "Финальное демо китайского режима началось плохо."
    n "Джун случайно залил старую версию справочника статусов. Паша перепутал тему оформления. Костя сообщил, что стенд поднят, но 'морально нестабилен'."

    $ op_set_emotion("junior_dev", "scared")
    junior "Я, кажется, задеплоил не ту ветку."
    $ op_set_emotion("devops", "tired")
    devops "Не ту — это какую?"
    $ op_set_emotion("junior_dev", "confused")
    junior "Которую не надо."
    $ op_set_emotion("devops", "focused")
    devops "Очень информативно. У тебя будущее в менеджменте инцидентов."

    $ op_set_emotion("manager", "panic")
    manager "Коллеги, китайская сторона уже подключилась. Давайте спокойно."
    china "We see Reject button. It rejects. Why?"
    $ op_set_emotion("manager", "panic")
    manager "Они видят кнопку 'Отклонить'. Она отклоняет. Они спрашивают, почему."
    $ op_set_emotion("frontend_dev", "neutral")
    fe "Потому что это кнопка 'Отклонить'."
    $ op_set_emotion("silent_senior", "neutral")
    senior "Слишком логично для этого проекта."

    menu:
        "Как спасать демо?"

        "Честно признать, что демо не готово":
            $ ethics += 2
            $ tech_quality += 1
            $ manager_rep -= 1
            $ op_set_emotion("gg", "neutral")
            p "Алена, лучше честно сказать: текущая версия не готова к показу. Иначе мы покажем хаос как функциональность."
            $ op_set_emotion("manager", "smile")
            manager "Это будет неприятно."
            $ op_set_emotion("gg", "neutral")
            p "Но не катастрофично. Катастрофично — продать им случайность."
            jump absurd_honest_finish

        "Провести демо на моках":
            $ ethics -= 1
            $ absurdity += 2
            $ manager_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Покажем моковые сценарии. Честно скажем, что это UX-preview, не live-стенд."
            $ op_set_emotion("manager", "smile")
            manager "Главное — не произноси слово 'мок' слишком громко."
            $ op_set_emotion("frontend_dev", "neutral")
            fe "Я сейчас включу самый красивый обман, который не совсем обман."
            jump absurd_mock_finish

        "Попросить DevOps сделать чудо":
            $ devops_rep += 1
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Кость, можно быстро откатить справочник и поднять правильную ветку?"
            $ op_set_emotion("devops", "focused")
            devops "Можно. Но после этого я официально становлюсь религиозным явлением."
            jump absurd_devops_save

        "Дать презентовать менеджеру как есть":
            $ absurdity += 3
            $ ethics -= 1
            $ op_set_emotion("gg", "neutral")
            p "Алена, презентуй. Будем отвечать по ходу."
            $ op_set_emotion("manager", "smile")
            manager "То есть импровизация?"
            $ op_set_emotion("dev_mentor", "neutral")
            dev1 "Нет. Корпоративный джаз."
            jump absurd_total_chaos

label absurd_honest_finish:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene bg_meeting_room_day with fade
    $ op_clear_sprites()
    n "Алена сказала китайской стороне, что демо переносится. Было неловко. Но впервые за долгое время никто не притворялся, что хаос — это план."
    china "We appreciate transparency. Please send updated plan."
    $ op_set_emotion("manager", "smile")
    manager "Они ценят прозрачность. И хотят обновленный план."
    $ op_set_emotion("devops", "tired")
    devops "План — это хорошо. План не падает в Kubernetes."
    $ tech_quality += 2
    jump finale_gate

label absurd_mock_finish:
    $ op_clear_sprites()
    play music "audio/music/absurd.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_chinese_call with fade
    $ op_clear_sprites()
    n "Паша включил моковые экраны. На них OfficePulse выглядел идеально: кнопки не ломали смысл, статусы сияли ответственной гармонией, отчеты показывали правду без дискомфорта."
    show ui_officepulse_chinese_mode at ui_panel_big
    china "Looks flexible. Very promising."
    $ op_set_emotion("manager", "smile")
    manager "Им нравится."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Конечно нравится. Там нет реальности."
    $ op_set_emotion("gg", "neutral")
    p "Зато есть направление."
    $ op_set_emotion("silent_senior", "comment")
    senior "Направление к аду тоже направление."
    $ absurdity += 2
    jump finale_gate

label absurd_devops_save:
    $ op_clear_sprites()
    play music "audio/music/release_crisis.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_devops_alerts with fade
    $ op_clear_sprites()
    n "Костя за десять минут сделал невозможное: откатил справочник, поднял правильную ветку, перезапустил стенд и никого не убил."
    $ op_set_emotion("devops", "angry")
    devops "Все. Работает. Но если кто-то скажет 'быстро же получилось', я уйду в лес."
    $ op_set_emotion("manager", "smile")
    manager "Костя, ты спас демо."
    $ op_set_emotion("devops", "tired")
    devops "Нет. Я отсрочил расплату. Это разные вещи."
    $ devops_module_enabled = True
    $ devops_rep += 2
    jump finale_gate

label absurd_total_chaos:
    $ op_clear_sprites()
    play music "audio/music/absurd.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_chinese_call with fade
    $ op_clear_sprites()
    n "Алена презентовала систему как есть. Кнопка 'Отклонить' отклоняла. Статус 'Критичное улучшение' мигал красным. Экспорт в Excel открылся кракозябрами."
    china "System is very flexible."
    n "В переговорке стало тихо."
    $ op_set_emotion("frontend_dev", "neutral")
    fe "Им нравится?"
    $ op_set_emotion("manager", "smile")
    manager "Кажется... да. Они говорят, что система гибкая."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Это не гибкость. Это перелом."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Но с точки зрения бизнеса — подвижность."
    $ absurdity += 3
    jump finale_gate

# =========================
# АРКА C. ЧЕЛОВЕЧЕСКАЯ: КАБИНЕТ 2
