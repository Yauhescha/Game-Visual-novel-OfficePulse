# routes/route_human.rpy

label route_human_start:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_kitchen_day with fade
    $ op_clear_sprites()
    n "В какой-то момент я понял: OfficePulse — не только про задачи. Каждая строка в системе связана с человеком, который устал, ошибся, испугался или просто пытался дожить до пятницы."

    n "На кухне Лера стояла у кофемашины. Было десять утра. То есть по ее личному часовому поясу — начало рабочего дня."

    $ op_set_emotion("gg", "neutral")
    p "Ты правда каждое утро опаздываешь?"
    $ op_set_emotion("late_tester", "neutral")
    lateqa "Формально — да. Фактически я часто закрываю ночные проверки. Но в табеле красивее выглядит опоздание, чем переработка без задачи."
    $ op_set_emotion("gg", "neutral")
    p "Почему не оформить?"
    $ op_set_emotion("late_tester", "neutral")
    lateqa "Потому что для ночной паники редко создают задачу. Обычно пишут: 'Лер, глянь быстро'."

    menu:
        "Что ответить Лере?"

        "Предложить фиксировать ночные проверки в OfficePulse":
            $ ethics += 2
            $ qa_rep += 1
            $ tech_quality += 1
            $ op_set_emotion("gg", "neutral")
            p "Давай добавим тип активности: ночная проверка, инцидент, срочная перепроверка. Чтобы это было видно."
            $ op_set_emotion("late_tester", "serious")
            lateqa "Ты хочешь превратить мои оправдания в данные?"
            $ op_set_emotion("gg", "neutral")
            p "Я хочу, чтобы тебе не приходилось оправдываться."
            $ op_set_emotion("late_tester", "soft")
            lateqa "Опасная фраза. Почти человеческая."

        "Сказать, что опоздания все равно выглядят плохо":
            $ qa_rep -= 1
            $ op_set_emotion("gg", "neutral")
            p "Понимаю, но со стороны это все равно выглядит плохо."
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Со стороны многое выглядит просто. Особенно чужая усталость."

        "Промолчать и принести кофе":
            $ qa_rep += 1
            $ human_route_open = True
            $ op_set_emotion("gg", "neutral")
            p "Какой кофе пьешь?"
            $ op_set_emotion("late_tester", "sleepy")
            lateqa "Сегодня? Любой, который докажет, что я еще в системе."
            n "Иногда поддержка начинается не с умных слов."

    jump human_junior_scene

label human_junior_scene:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_day with fade
    $ op_clear_sprites()
    n "Даня сидел над задачей уже третий час. На экране был код справочника статусов, который выглядел так, будто его писал человек, одновременно боящийся базы данных и TypeScript."

    $ op_set_emotion("junior_dev", "confused")
    junior "Я опять все усложнил?"
    $ op_set_emotion("gg", "neutral")
    p "Немного."
    $ op_set_emotion("junior_dev", "confused")
    junior "Это плохое немного?"
    $ op_set_emotion("gg", "neutral")
    p "Это обычное немного."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Не пугайся. Все через это проходят. Кроме Славы. Слава родился с комментариями к PR."
    $ op_set_emotion("silent_senior", "neutral")
    senior "Неправда. Сначала были замечания к акушеру."

    menu:
        "Как помочь Дане?"

        "Разобрать задачу вместе и объяснить архитектуру":
            $ junior_helped = True
            $ junior_rep += 2
            $ dev_rep += 1
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Давай разложим. Есть сущность статуса, есть отображаемое имя, есть офисная конфигурация. Не смешивай это в одну кашу."
            $ op_set_emotion("junior_dev", "confused")
            junior "То есть китайское название не должно менять внутренний тип?"
            $ op_set_emotion("gg", "neutral")
            p "Да. Вот теперь ты мыслишь не кнопкой, а системой."
            $ op_set_emotion("junior_dev", "happy")
            junior "Это больно, но приятно."

        "Быстро переписать за него":
            $ junior_rep -= 1
            $ tech_quality += 1
            $ op_set_emotion("gg", "neutral")
            p "Дай сюда. Я перепишу, а ты посмотришь."
            $ op_set_emotion("junior_dev", "happy")
            junior "Спасибо."
            n "Код стал лучше. Даня — не очень."

        "Оставить его разбираться самому":
            $ junior_rep -= 1
            $ ethics -= 1
            $ op_set_emotion("gg", "neutral")
            p "Попробуй сам еще час. Потом посмотрим."
            $ op_set_emotion("junior_dev", "confused")
            junior "Хорошо."
            n "Иногда самостоятельность — это рост. Иногда — одиночество с компилятором. Я пока не понял, что выбрал."

    jump human_newqa_scene

label human_newqa_scene:
    $ op_clear_sprites()
    play music "audio/music/office_evening.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office1_evening with fade
    $ op_clear_sprites()
    n "Настя задержалась после работы. На ее экране был список багов по OfficePulse. Они были оформлены идеально: шаги, результат, ожидание, серьезность, риск."

    $ op_set_emotion("gg", "neutral")
    p "Ты всегда так подробно пишешь?"
    $ op_set_emotion("new_tester", "soft")
    newqa "Стараюсь. Иначе Виктор перепишет за меня."
    $ op_set_emotion("gg", "neutral")
    p "Боишься его?"
    $ op_set_emotion("new_tester", "soft")
    newqa "Не боюсь. Но рядом с ним легко начать проверять не продукт, а собственную ценность."

    $ op_set_emotion("gg", "tired")
    p "Ты тестируешь почти все мои задачи. Не устала от меня?"
    $ op_set_emotion("new_tester", "disappointed")
    newqa "От тебя — нет. От того, что меня используют как фильтр между тобой и релизом — иногда."

    menu:
        "Как построить отношения с Настей?"

        "Предложить работать как dev+QA пара":
            $ newqa_rep += 2
            $ qa_rep += 1
            $ tech_quality += 2
            $ op_set_emotion("gg", "neutral")
            p "Давай работать не как 'я сделал — ты сломала', а как пара. Я показываю спорные места до тестирования, ты говоришь риски до багов."
            $ op_set_emotion("new_tester", "disappointed")
            newqa "Это звучит почти как нормальный процесс. Подозрительно."
            $ op_set_emotion("gg", "neutral")
            p "Можем попробовать и испортить статистику токсичности."
            $ op_set_emotion("new_tester", "soft")
            newqa "Договорились."

        "Попросить ее быть мягче в баг-репортах":
            $ newqa_rep -= 1
            $ op_set_emotion("gg", "neutral")
            p "Можешь писать баги чуть мягче? Иногда ощущение, что меня судят."
            $ op_set_emotion("new_tester", "neutral")
            newqa "Я пишу не тебе. Я пишу системе. Если ты видишь там суд, может, проблема не в формулировке."

        "Держать дистанцию":
            $ ethics += 0
            $ op_set_emotion("gg", "neutral")
            p "Понятно. Тогда будем просто работать по процессу."
            $ op_set_emotion("new_tester", "disappointed")
            newqa "Процесс — это тоже отношения. Просто с меньшим количеством честности."

    jump human_devops_scene

label human_devops_scene:
    $ op_clear_sprites()
    play music "audio/music/night.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene bg_server_room with fade
    $ op_clear_sprites()
    n "Костя сидел перед тремя мониторами. На одном были логи, на втором графики, на третьем чат, где кто-то написал: 'Кость, а можешь быстро?'"

    $ op_set_emotion("devops", "angry")
    devops "Я ненавижу слово быстро. Быстро — это когда человек не хочет создавать задачу."
    $ op_set_emotion("gg", "neutral")
    p "Я хочу добавить в OfficePulse модуль DevOps-заявок. Приоритеты, окружения, история, кто попросил, зачем."
    $ op_set_emotion("devops", "tired")
    devops "Ты хочешь легализовать мое страдание."
    $ op_set_emotion("gg", "neutral")
    p "Я хочу сделать его видимым."
    $ op_set_emotion("devops", "tired")
    devops "Звучит почти полезно. Подозрительно для разработки."

    menu:
        "Что добавить для DevOps?"

        "Полноценный модуль заявок":
            $ devops_module_enabled = True
            $ devops_rep += 3
            $ tech_quality += 1
            $ op_set_emotion("gg", "neutral")
            p "Сделаем полноценный модуль: заявка, приоритет, дедлайн, окружение, ответственный, история."
            $ op_set_emotion("devops", "focused")
            devops "Если это заработает, я перестану отвечать на половину личных сообщений."
            $ op_set_emotion("gg", "neutral")
            p "И это хорошо?"
            $ op_set_emotion("devops", "grateful")
            devops "Это будет мой отпуск."

        "Только быстрый список просьб":
            $ devops_rep += 1
            $ tech_debt += 1
            $ op_set_emotion("gg", "neutral")
            p "Начнем с простого списка просьб. Потом расширим."
            $ op_set_emotion("devops", "tired")
            devops "Потом — это кладбище нормальных идей. Но ладно. Хоть так."

        "Отложить DevOps до следующего релиза":
            $ devops_rep -= 1
            $ op_set_emotion("gg", "tired")
            p "Боюсь, сейчас не влезет. Надо отложить до следующего релиза."
            $ op_set_emotion("devops", "tired")
            devops "Конечно. Моя усталость тоже в бэклоге."

    jump human_release_night

label human_release_night:
    $ op_clear_sprites()
    play music "audio/music/release_crisis.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene cg_release_crisis with fade
    $ op_clear_sprites()
    n "Ночь перед релизом. В офисе остались я, Настя, Лера, Даня и Костя. Такое ощущение, что кабинет 2 стал временным убежищем для людей, которые не успели сдаться."

    system "Ошибка: изменение истории задачи через старый API не отображается в UI."
    play sound "audio/sfx/alert.ogg"
    show ui_officepulse_error at ui_panel_right

    $ op_set_emotion("junior_dev", "confused")
    junior "Это критично?"
    $ op_set_emotion("new_tester", "neutral")
    newqa "Да. Если историю можно изменить в обход интерфейса, всем отчетам нельзя доверять."
    $ op_set_emotion("devops", "focused")
    devops "Старый API торчит наружу?"
    show ui_officepulse_logs at ui_panel_left
    $ op_set_emotion("gg", "neutral")
    p "Не наружу. Но доступ есть у внутренних сервисов."
    $ op_set_emotion("late_tester", "neutral")
    lateqa "А внутренние сервисы — это всегда 'не наружу', пока кто-то не сделает наружу через костыль."

    menu:
        "Что сделать перед релизом?"

        "Остановить релиз и честно объяснить":
            $ ethics += 3
            $ tech_quality += 2
            $ qa_rep += 1
            $ op_set_emotion("gg", "serious")
            p "Останавливаем релиз. История — основа системы. Если она дырявая, релизить нельзя."
            $ op_set_emotion("junior_dev", "scared")
            junior "Нас убьют?"
            $ op_set_emotion("devops", "tired")
            devops "Не сегодня. Сегодня нас просто не поймут."
            $ op_set_emotion("new_tester", "soft")
            newqa "Я поддержу. Это правильное решение."
            jump finale_gate

        "Закрыть доступ через DevOps и выпустить с риском":
            $ devops_rep += 2
            $ tech_debt += 1
            $ devops_module_enabled = True
            $ op_set_emotion("gg", "neutral")
            p "Кость, можно ограничить старый API на уровне доступа до фикса?"
            $ op_set_emotion("devops", "focused")
            devops "Можно. Это костыль, но хотя бы честный костыль с табличкой 'опасно'."
            $ op_set_emotion("new_tester", "neutral")
            newqa "В release notes обязательно указать риск."
            $ op_set_emotion("gg", "neutral")
            p "Укажем."
            jump finale_gate

        "Скрыть баг до следующего спринта":
            $ critical_bug_hidden = True
            $ ethics -= 3
            $ tech_debt += 3
            $ op_set_emotion("gg", "neutral")
            p "Если сейчас остановим релиз, нас разорвут. Спрячем до следующего спринта."
            $ op_set_emotion("new_tester", "angry")
            newqa "Ты серьезно?"
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Вот так люди и становятся процессом, который ненавидели."
            jump finale_gate

# =========================
# АРКА D. КАРЬЕРА: ПЕРЕСМОТР
