# routes/act2_officepulse.rpy

label act2_project_assignment:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office1_day with fade
    $ op_clear_sprites()
    n "На следующей неделе Сергей, почти-лид разработки, позвал меня в кабинет 1. Он говорил спокойно, но слишком аккуратно — так говорят люди, которые сейчас дадут задачу без нормального конца."

    $ op_set_emotion("dev_lead", "neutral")
    devlead "[player_name], у нас есть отдельная инициатива. Внутренняя система OfficePulse."
    $ op_set_emotion("gg", "neutral")
    p "Что она должна делать?"
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Учитывать задачи, баги, возвраты, причины отказов, пересмотры, отчеты, загрузку DevOps. В идеале — дать прозрачность."
    $ op_set_emotion("gg", "neutral")
    p "Звучит как несколько систем."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Так и есть. Но называется одной, чтобы бюджет выглядел спокойнее."

    $ op_set_emotion("gg", "neutral")
    p "Почему это отдаете мне?"
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Ты новый. У тебя еще нет старых обид."
    $ op_set_emotion("gg", "neutral")
    p "Это плюс?"
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Пока да."

    n "В кабинет вошел Виктор. Похоже, он знал о разговоре раньше меня."

    $ op_set_emotion("qa_lead", "serious")
    qalead "OfficePulse должен быть не игрушкой для оправдания разработчиков, а инструментом качества."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Он должен показывать факты."
    $ op_set_emotion("qa_lead", "serious")
    qalead "Факты без контекста — это оружие для тех, кто не умеет читать."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Контекст без фактов — это способ вечно валить задачи на настроение QA."

    n "Я впервые увидел их спор вживую. Это было похоже на code review, которое перешло в философию."

    $ op_set_emotion("gg", "neutral")
    p "А кто будет тестировать систему?"
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Настя. Ее взяли как раз под большую часть твоих задач."

    $ op_set_emotion("new_tester", "formal")
    newqa "Я уже посмотрела черновые требования. Там есть риски."
    $ op_set_emotion("gg", "neutral")
    p "Я еще не начал писать."
    $ op_set_emotion("new_tester", "neutral")
    newqa "Тем более. Пока дешевле исправлять."

    jump act2_manager_arrives

label act2_manager_arrives:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_day with fade
    $ op_clear_sprites()
    n "Через два дня появилась Алена — менеджер OfficePulse. Она пришла с ноутбуком, улыбкой и документом на сорок семь пунктов."
    play sound "audio/sfx/notification.ogg"

    $ op_set_emotion("manager", "business")
    manager "Ребята, хорошие новости. Система интересна не только нам. Китайская команда тоже хочет использовать OfficePulse у себя."
    $ op_set_emotion("dev_mentor", "tired")
    dev1 "Она еще не существует."
    $ op_set_emotion("manager", "smile")
    manager "Вот именно. Поэтому сейчас лучшее время заложить масштабируемость."
    $ op_set_emotion("devops", "tired")
    devops "Я уже слышу, как где-то плачет один сервер."

    $ op_set_emotion("manager", "smile")
    manager "Там от китайцев маленькое уточнение. Им нужна локализация, отдельные роли, другой календарь, экспорт в Excel по их шаблону, и желательно возможность скрывать конфликтные комментарии от локального руководителя."

    n "В комнате стало тихо. Даже Слава поднял глаза от ноутбука."

    $ op_set_emotion("silent_senior", "neutral")
    senior "Возможность скрывать конфликтные комментарии — это не требование. Это признание вины."
    $ op_set_emotion("frontend_dev", "neutral")
    fe "А что значит 'другой календарь'?"
    $ op_set_emotion("manager", "smile")
    manager "Праздники, часовые пояса, рабочие субботы, и еще у них статусы задач немного отличаются."
    $ op_set_emotion("backend_dev", "serious")
    legacy "Немного — это сколько?"
    $ op_set_emotion("manager", "smile")
    manager "В два раза."

    menu:
        "Как ответить на первые китайские требования?"

        "Сказать, что это отдельный эпик":
            $ tech_quality += 2
            $ manager_rep -= 1
            $ ethics += 1
            $ op_set_emotion("gg", "neutral")
            p "Это не маленькое уточнение. Это отдельный эпик: мультиофисность, локализация, роли, календарь, экспорт. Надо выделять отдельно."
            $ op_set_emotion("manager", "business")
            manager "Я понимаю, но бизнесу нужно быстрее."
            $ op_set_emotion("gg", "neutral")
            p "Быстрее можно. Нормально — отдельно."
            $ op_set_emotion("dev_lead", "neutral")
            devlead "Хорошо сказано."
            $ op_set_emotion("qa_lead", "smirk")
            qalead "Редкий случай, когда разработчик не пытается закопать проблему в код."

        "Взять все в текущий релиз":
            $ manager_rep += 2
            $ tech_debt += 3
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Попробуем заложить это сразу в текущий релиз."
            $ op_set_emotion("devops", "tired")
            devops "Я запомню этот момент. Потом буду показывать его людям как начало катастрофы."
            $ op_set_emotion("silent_senior", "neutral")
            senior "Смело. Не значит разумно."
            $ op_set_emotion("manager", "smile")
            manager "Отлично. Я знала, что мы найдем общий язык."

        "Сделать временный костыль":
            $ tech_debt += 2
            $ absurdity += 1
            $ op_set_emotion("gg", "neutral")
            p "Можно сделать временный режим для китайского офиса, а потом нормально переделать."
            $ op_set_emotion("backend_dev", "serious")
            legacy "Временное решение — это постоянное решение, которое еще не призналось."
            $ op_set_emotion("frontend_dev", "neutral")
            fe "Я уже вижу checkbox 'Китай'."
            $ op_set_emotion("manager", "smile")
            manager "Главное, чтобы работало на демо."

        "Предложить конфигурационный режим":
            $ tech_quality += 1
            $ chinese_mode_enabled = True
            $ manager_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Можно сделать конфигурационный режим: офисы, роли, статусы, календари. Не быстро, но это переживет следующие требования."
            $ op_set_emotion("silent_senior", "neutral")
            senior "Это похоже на мысль. Продолжай."
            $ op_set_emotion("qa_lead", "angry")
            qalead "Если будет аудит изменений конфигурации — я не против."
            $ op_set_emotion("manager", "smile")
            manager "А если без аудита?"
            $ op_set_emotion("qa_lead", "angry")
            qalead "Тогда я против в два раза сильнее."

    jump act2_first_design

label act2_first_design:
    $ op_clear_sprites()
    play music "audio/music/office_evening.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_evening with fade
    $ op_clear_sprites()
    n "Следующие дни OfficePulse существовал в виде схем, споров и растущего списка 'маленьких уточнений'."
    n "Паша рисовал интерфейс. Игорь предупреждал о легаси. Слава молча оставлял комментарии. Настя читала требования как детектив."

    $ op_set_emotion("frontend_dev", "neutral")
    fe "У меня вопрос. Если баг нельзя называть багом в китайской версии, как его называть?"
    $ op_set_emotion("manager", "smile")
    manager "Они предложили вариант 'область улучшения'."
    $ op_set_emotion("late_tester", "neutral")
    lateqa "А если прод упал?"
    $ op_set_emotion("manager", "smile")
    manager "Критическая область улучшения."
    $ op_set_emotion("devops", "tired")
    devops "Мне нравится. Сегодня ночью у нас была критическая область улучшения базы данных."

    $ op_set_emotion("new_tester", "formal")
    newqa "Серьезно. Если в системе можно будет переименовать дефект в улучшение, метрики станут бесполезными."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Вот. Настя понимает."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "А если мы дадим разные отображаемые названия, но единый внутренний тип?"
    $ op_set_emotion("gg", "neutral")
    p "То есть в базе defect, в UI локализованное название?"
    $ op_set_emotion("silent_senior", "comment")
    senior "Наконец-то кто-то сказал 'в базе', а не 'на кнопке'."

    n "Я записал первое важное правило OfficePulse: правда должна храниться глубже интерфейса."
    show ui_officepulse_logs at ui_panel_left

    menu:
        "Какую архитектурную основу выбрать?"

        "Жесткий аудит всех изменений":
            $ audit_enabled = True
            $ ethics += 2
            $ tech_quality += 2
            $ qa_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Добавляем неизменяемый аудит: кто, когда и что изменил. Даже если UI показывает мягкие формулировки."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Правильно. Иначе это будет генератор красивой лжи."
            $ op_set_emotion("manager", "smile")
            manager "Главное, чтобы отчеты не выглядели слишком конфликтно."
            $ op_set_emotion("dev_lead", "neutral")
            devlead "Отчеты пусть выглядят честно. Конфликтно выглядят процессы."

        "Мягкая версия без опасных полей":
            $ manager_rep += 1
            $ tech_debt += 1
            $ op_set_emotion("gg", "neutral")
            p "На первом этапе уберем самые конфликтные поля. Сделаем задачи, статусы, базовые отчеты."
            $ op_set_emotion("new_tester", "neutral")
            newqa "Тогда система не ответит на главный вопрос: почему задача возвращалась."
            $ op_set_emotion("gg", "neutral")
            p "Зато выйдет быстрее."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Быстрое бесполезное — тоже бесполезное. Только быстро."

        "Дать лидам расширенные права редактирования":
            $ control += 1
            $ ethics -= 1
            $ tech_debt += 1
            $ op_set_emotion("gg", "neutral")
            p "Можно дать лидам права править причины, если ошибка в формулировке."
            $ op_set_emotion("qa_lead", "serious")
            qalead "Править — да. С историей изменений."
            $ op_set_emotion("dev_lead", "neutral")
            devlead "Без истории это будет не система учета, а стиральная машина."
            $ op_set_emotion("manager", "business")
            manager "Но иногда бизнесу нужна гибкость."
            $ op_set_emotion("silent_senior", "comment")
            senior "Гибкость без следов называется подлог."

        "Скрыть аудит до второго релиза":
            $ critical_bug_hidden = False
            $ tech_debt += 3
            $ manager_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Аудит нужен, но можно перенести во второй релиз."
            $ op_set_emotion("new_tester", "neutral")
            newqa "Тогда первый релиз уже начнет собирать данные, которым нельзя доверять."
            $ op_set_emotion("gg", "neutral")
            p "Зато мы не утонем в объеме."
            n "Я сам услышал, как это прозвучало. Не убедительно."

    jump act2_junior_arrives

label act2_junior_arrives:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_day with fade
    $ op_clear_sprites()
    n "Через месяц после меня в кабинет 2 пришел джун — Даня. Он держал ноутбук двумя руками, будто это был хрупкий артефакт."

    $ op_set_emotion("junior_dev", "confused")
    junior "Привет. Мне сказали, здесь разработчики."
    $ op_set_emotion("dev_mentor", "smile")
    dev1 "Иногда. В плохие дни мы еще и психологи, и саппорт, и археологи легаси."
    $ op_set_emotion("gg", "neutral")
    p "Я [player_name]. Если что — спрашивай."
    $ op_set_emotion("junior_dev", "confused")
    junior "А можно сразу? У меня проект не собирается."
    $ op_set_emotion("backend_dev", "neutral")
    legacy "Добро пожаловать. Это нормальное состояние проекта."

    n "Даня сел за соседний стол. Через двадцать минут он спросил, почему Git требует от него принять решение по конфликту, хотя он никому не угрожал."

    menu:
        "Как вести себя с джуном?"

        "Терпеливо помогать":
            $ junior_helped = True
            $ junior_rep += 2
            $ dev_rep += 1
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Давай по шагам. Сначала посмотрим, что именно конфликтует. Git не ругается, он просто показывает, что два человека трогали одно место."
            $ op_set_emotion("junior_dev", "confused")
            junior "То есть это не я все сломал?"
            $ op_set_emotion("gg", "neutral")
            p "Пока нет. Но потенциал есть."
            $ op_set_emotion("junior_dev", "happy")
            junior "Спасибо. Это почему-то успокаивает."

        "Скинуть на Артема":
            $ junior_rep -= 1
            $ dev_rep -= 1
            $ op_set_emotion("gg", "neutral")
            p "Дань, лучше к Артему. Он тут онбордингом занимается."
            $ op_set_emotion("dev_mentor", "serious")
            dev1 "Официально — да. Но ты уже месяц как не новый. Поздравляю с повышением до человека, который тоже отвечает на вопросы."
            $ op_set_emotion("junior_dev", "confident")
            junior "Понял. Извините."
            n "Он улыбнулся, но закрыл ноутбук чуть тише."

        "Раздраженно ответить":
            $ junior_rep -= 2
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Даня, это базовый Git. Погугли сначала."
            $ op_set_emotion("junior_dev", "confused")
            junior "Да, хорошо. Извини."
            $ op_set_emotion("late_tester", "sarcastic")
            lateqa "О, классика. Через месяц после онбординга человек уже говорит как старожил."
            n "Мне стало неприятно, но я сделал вид, что не услышал."

        "Использовать его как помощника для OfficePulse":
            $ junior_rep += 1
            $ tech_quality += 1
            $ tech_debt += 1
            $ op_set_emotion("gg", "neutral")
            p "Давай так: я помогу тебе с окружением, а ты возьмешь простую часть OfficePulse — справочник статусов."
            $ op_set_emotion("junior_dev", "confident")
            junior "Я справлюсь?"
            $ op_set_emotion("gg", "neutral")
            p "С моей помощью — да. Без моей помощи — будет обучающий пожар."
            $ op_set_emotion("devops", "tired")
            devops "Пожары только через заявку."

    jump act2_first_demo

label act2_first_demo:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_first_demo with fade
    $ op_clear_sprites()
    n "Первое демо OfficePulse назначили на пятницу. Это уже было плохим знаком."
    show ui_officepulse_dashboard at ui_panel_big
    play sound "audio/sfx/mouse_click.ogg"
    n "В переговорке собрались почти все: разработчики, QA, бухгалтерия, DevOps, Алена и даже Раиса Петровна, которая сказала, что пришла посмотреть на 'электронную ответственность'."

    $ op_set_emotion("manager", "smile")
    manager "Коллеги, сегодня покажем первую версию OfficePulse. Список задач, баги, история изменений, базовые отчеты и задел под китайский офис."

    $ op_set_emotion("gg", "neutral")
    p "Начнем с карточки задачи. Здесь видно статус, ответственного, связанные дефекты и историю."
    $ op_set_emotion("new_tester", "neutral")
    newqa "Покажи историю изменения причины возврата."
    $ op_set_emotion("gg", "neutral")
    p "Вот."

    if audit_enabled:
        $ op_set_emotion("qa_lead", "neutral")
        qalead "Вижу автора изменения, время и старое значение. Хорошо."
        $ op_set_emotion("dev_lead", "neutral")
        devlead "И комментарий тоже виден. Значит, нельзя просто переписать историю."
    else:
        $ op_set_emotion("qa_lead", "neutral")
        qalead "А где автор изменения?"
        $ op_set_emotion("gg", "neutral")
        p "Пока не выводим."
        $ op_set_emotion("qa_lead", "neutral")
        qalead "Пока — это когда уже поздно."

    $ op_set_emotion("young_accountant", "tired")
    youngacc "А отчет по переработкам здесь будет?"
    if salary_module_enabled:
        $ op_set_emotion("gg", "neutral")
        p "Да. Я заложил отдельный модуль. Пока черновик, но можно связать задачи, переработки и премии."
        $ op_set_emotion("young_accountant", "smile")
        youngacc "Спасибо. Это уже больше, чем 'потом посмотрим'."
    else:
        $ op_set_emotion("gg", "neutral")
        p "Пока нет. В следующих релизах."
        $ op_set_emotion("old_accountant", "neutral")
        oldacc "То есть деньги опять после всего. Как обычно."

    $ op_set_emotion("devops", "tired")
    devops "А заявки на стенды?"
    $ op_set_emotion("gg", "neutral")
    p "Пока только в планах."
    $ op_set_emotion("devops", "tired")
    devops "Стабильно. Все в планах, кроме моей усталости."

    china "Can system show process honesty, but without discomfort from honesty?"
    n "Алена посмотрела в чат созвона и слегка побледнела."
    play sound "audio/sfx/call.ogg"
    $ op_set_emotion("manager", "smile")
    manager "Китайские коллеги спрашивают, можно ли показывать прозрачность процесса так, чтобы она не создавала дискомфорт прозрачностью."

    $ op_set_emotion("frontend_dev", "neutral")
    fe "Это новый уровень требований."
    $ op_set_emotion("silent_senior", "neutral")
    senior "Нет. Это старый уровень политики. Просто переведенный."

    n "После демо стало понятно: OfficePulse больше не маленькая внутренняя система. Это зеркало, в которое никто не хочет смотреть первым."

    jump route_choice

# =========================
# ВЫБОР ОСНОВНОЙ АРКИ
# =========================

label route_choice:
    $ op_clear_sprites()
    play music "audio/music/office_evening.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_day with fade
    $ op_clear_sprites()
    n "После первого демо у меня было несколько направлений. Каждое решало одну проблему, но усиливало другую."

    menu:
        "На чем сфокусироваться дальше?"

        "Расследовать странные изменения в логах":
            $ route_name = "drama"
            jump route_drama_start

        "Разрулить китайские требования":
            $ route_name = "absurd"
            jump route_absurd_start

        "Поддержать людей вокруг":
            $ route_name = "human"
            jump route_human_start

        "Сделать OfficePulse инструментом управленческих решений":
            $ route_name = "career"
            jump route_career_start

# =========================
# АРКА A. ДРАМА: ЛОГИ НЕ ВРУТ
