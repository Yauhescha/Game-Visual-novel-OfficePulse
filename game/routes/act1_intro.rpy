# routes/act1_intro.rpy

label act1_first_day:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office_entrance with fade
    $ op_clear_sprites()
    n "Первый рабочий день начался не с торжественного приветствия, а с турникета, который отказался признавать новый пропуск."
    play sound "audio/sfx/steps.ogg"
    play sound "audio/sfx/error.ogg"
    n "Охранник посмотрел на меня так, будто я уже успел сломать прод."

    $ op_set_emotion("gg", "neutral")
    p "Я сегодня первый день. Мне сказали, кабинет два."

    n "Охранник лениво набрал кому-то в офис. Через минуту в коридоре появился мужчина с кружкой кофе и выражением лица человека, который видел слишком много онбордингов."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Ты новенький мидл?"
    $ op_set_emotion("gg", "neutral")
    p "Да."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Тогда пошли. Я Артем. Формально я провожу тебе онбординг. Неформально — объясню, куда здесь лучше не наступать."

    scene bg_corridor_day with fade
    $ op_clear_sprites()
    n "Коридор был узкий, офис — небольшой, но ощущение было такое, будто в этих стенах помещается вся история корпоративных конфликтов человечества."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Слева кабинет один. Там бухгалтерия, почти-лид разработки, новая тестировщица и наш DevOps. Если дверь закрыта — не открывай без причины."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Справа кабинет три. QA. Если оттуда тихо — значит, там кто-то пишет длинный комментарий к багу."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "А вот это кабинет два. Твое новое место."

    scene bg_office2_day with fade
    $ op_clear_sprites()
    n "Кабинет 2 оказался самым обычным: столы, мониторы, провода, кружки, стикеры, запах кофе и легкая усталость в воздухе."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Вот твой стол. Локальное окружение поднимем. Документация есть, но она больше как легенда."
    $ op_set_emotion("gg", "neutral")
    p "В каком смысле?"
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "В том смысле, что все о ней слышали, но мало кто видел живой."

    n "Я сел за стол и включил ноутбук. На соседнем месте стояла пустая чашка с надписью: 'QA sees you'."

    $ op_set_emotion("gg", "neutral")
    p "Чье это место?"
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Леры. Тестировщица. Она каждый день опаздывает минимум на полчаса."
    $ op_set_emotion("gg", "neutral")
    p "И это нормально?"
    $ op_set_emotion("dev_mentor", "serious")
    dev1 "В этом офисе слово 'нормально' лучше использовать осторожно."

    n "Через сорок минут дверь открылась. В кабинет вошла девушка с рюкзаком, стаканом кофе и лицом человека, который не собирается оправдываться перед временем."
    play sound "audio/sfx/door.ogg"
    play sound "audio/sfx/coffee.ogg"

    $ op_set_emotion("late_tester", "neutral")
    lateqa "О, новый разработчик. Привет."
    $ op_set_emotion("gg", "neutral")
    p "Привет."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Это Лера. Лера, это [player_name]."
    $ op_set_emotion("late_tester", "sarcastic")
    lateqa "Соболезную."
    $ op_set_emotion("gg", "neutral")
    p "Из-за работы?"
    $ op_set_emotion("late_tester", "neutral")
    lateqa "Из-за кабинета два. Он сначала кажется обычным. Потом ты начинаешь понимать шутки."

    menu:
        "Как отреагировать на ее опоздание?"

        "Спросить: 'У нас так можно?'":
            $ qa_rep -= 1
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "У нас так можно?"
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Можно что?"
            $ op_set_emotion("gg", "neutral")
            p "Опаздывать почти на час."
            n "Артем тихо поставил кружку на стол. По его лицу было видно: он только что увидел первый офисный микроконфликт сезона."
            $ op_set_emotion("late_tester", "sleepy")
            lateqa "Если ночью стенд падает, а ты в три утра пишешь в чат, что 'просто проверил одну штуку', тогда утром можно многое."
            $ op_set_emotion("gg", "neutral")
            p "Понял."
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Пока нет. Но поймешь."

        "Промолчать":
            $ ethics += 1
            $ op_set_emotion("gg", "neutral")
            p "Привет."
            n "Я решил не начинать первый день с морализаторства. Артем одобрительно кивнул, будто я прошел невидимый тест."
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Молчаливый. Это хорошо. Значит, пока не написал ни одного спорного комментария в задаче."

        "Пошутить":
            $ qa_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Я так понимаю, в офисе есть гибкий график, но он знает об этом только QA?"
            $ op_set_emotion("late_tester", "sarcastic")
            lateqa "Не только QA. Просто QA чаще всех вынужден доказывать, что время относительно."
            $ op_set_emotion("dev_mentor", "serious")
            dev1 "Осторожно. Она умеет находить баги не только в задачах, но и в людях."

        "Спросить позже, все ли нормально":
            $ qa_rep += 2
            $ human_route_open = True
            $ op_set_emotion("gg", "neutral")
            p "Привет. Потом покажешь, где тут кофе?"
            $ op_set_emotion("late_tester", "soft")
            lateqa "Если переживешь настройку окружения — покажу."
            n "Я решил не делать выводы. В офисе, где все выглядят уставшими, причины могут быть сложнее расписания."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Ладно, знакомство прошло почти без крови. Теперь онбординг."
    jump act1_onboarding

label act1_onboarding:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_day with fade
    $ op_clear_sprites()
    n "Артем открыл проект. На экране появились модули, сервисы, старые миграции, новые костыли и README, которое заканчивалось фразой 'дальше спросить у Игоря'."
    play sound "audio/sfx/keyboard.ogg"

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Основная система старая. Есть легаси, есть новый модуль, есть то, что нельзя трогать, потому что никто не помнит почему."
    $ op_set_emotion("gg", "neutral")
    p "А кто помнит?"
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Игорь. Но он объясняет так, что после объяснения вопросов становится больше."

    $ op_set_emotion("backend_dev", "serious")
    legacy "Я слышал свое имя."
    n "У двери появился мужчина с блокнотом и выражением лица человека, который однажды написал временное решение, а оно пережило три архитектуры."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Игорь, это [player_name]. Новый мидл."
    $ op_set_emotion("backend_dev", "serious")
    legacy "Сочувствую."
    $ op_set_emotion("gg", "neutral")
    p "Вы уже второй, кто это говорит."
    $ op_set_emotion("backend_dev", "neutral")
    legacy "Значит, коллектив честный."

    n "За дальним столом сидел еще один разработчик. Он не сказал ни слова. Только поднял взгляд от монитора и снова вернулся к коду."

    $ op_set_emotion("gg", "neutral")
    p "А это?"
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Слава. Senior. Говорит редко. Если оставил комментарий в ревью — считай, что получил письмо из будущего."
    $ op_set_emotion("silent_senior", "comment")
    senior "Если код не требует комментариев, это не значит, что он хороший. Это значит, что я еще не открыл PR."

    n "Я улыбнулся. Кажется, я начал понимать кабинет 2."

    jump act1_first_bug

label act1_first_bug:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_day with fade
    $ op_clear_sprites()
    n "Через два дня мне дали первую небольшую задачу: добавить поле в карточку заявки и сохранить его в базе."
    n "Артем сказал, что задача простая. Игорь сказал, что простых задач не бывает. Слава ничего не сказал, что было страшнее всего."

    $ op_set_emotion("gg", "neutral")
    p "Готово. Отправляю на тестирование."

    n "Через час пришел баг. Его завела новая тестировщица из кабинета 1 — Настя."
    play sound "audio/sfx/message.ogg"
    show ui_officepulse_task_card at ui_panel_right

    scene bg_office1_day with fade
    $ op_clear_sprites()
    $ op_set_emotion("new_tester", "formal")
    newqa "Привет. По задаче есть дефект. Поле сохраняется, но при повторном открытии карточки значение не отображается для роли бухгалтера."
    $ op_set_emotion("gg", "neutral")
    p "Странно. Я проверял."
    $ op_set_emotion("new_tester", "formal")
    newqa "Ты проверял под ролью разработчика. В acceptance criteria указана роль бухгалтера."
    $ op_set_emotion("gg", "neutral")
    p "Точно. Пропустил."
    $ op_set_emotion("new_tester", "formal")
    newqa "Я приложила шаги, скрин и expected result."

    menu:
        "Как ответить Насте?"

        "Спокойно поблагодарить и исправить":
            $ qa_rep += 1
            $ newqa_rep += 1
            $ tech_quality += 1
            $ op_set_emotion("gg", "neutral")
            p "Спасибо. Да, моя ошибка. Исправлю и добавлю проверку на роль."
            $ op_set_emotion("new_tester", "neutral")
            newqa "Хорошо. Тогда после фикса я быстро перепроверю."
            n "Формально. Сухо. Но справедливо."

        "Начать спорить":
            $ qa_rep -= 2
            $ newqa_rep -= 2
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Но поле же сохраняется. Это скорее недочет отображения, не критичный дефект."
            $ op_set_emotion("new_tester", "angry")
            newqa "Если пользователь не видит сохраненное значение, для него оно не сохранено."
            $ op_set_emotion("gg", "neutral")
            p "Можно было оформить мягче."
            $ op_set_emotion("new_tester", "angry")
            newqa "Можно было проверить роль из требований."
            n "Разговор закончился. Баг остался."

        "Попросить Артема помочь":
            $ dev_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Артем, можешь глянуть? Я, кажется, пропустил роль бухгалтера."
            $ op_set_emotion("dev_mentor", "neutral")
            dev1 "Конечно. И запомни: если задача кажется простой, значит, где-то есть роль бухгалтера."
            $ op_set_emotion("new_tester", "neutral")
            newqa "Я буду на месте. Когда поправишь — переотправь."

        "Пойти напрямую к QA-лиду":
            $ qa_rep -= 2
            $ burnout += 2
            jump act1_qalead_first_conflict

    jump act1_accounting_day

label act1_qalead_first_conflict:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office3_day with fade
    $ op_clear_sprites()
    n "Я решил, что лучше сразу выяснить стандарты тестирования. Кабинет 3 встретил меня тишиной и звуком клавиатуры."

    $ op_set_emotion("qa_lead", "neutral")
    qalead "Ты по какому вопросу?"
    $ op_set_emotion("gg", "neutral")
    p "По багу от Насти. Хотел уточнить, насколько это критично."
    $ op_set_emotion("qa_lead", "angry")
    qalead "Если ты пришел спорить с первым багом в первый рабочий день, то у нас проблема не с критичностью, а с самооценкой."
    $ op_set_emotion("gg", "neutral")
    p "Я хотел разобраться."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Мидл — это не тот, кто умеет писать код. Это тот, чьи баги не надо объяснять тестировщику три раза."

    $ op_set_emotion("qa_halflead", "serious")
    qahalf "Виктор, может, без прессинга? Человек новый."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Новый — не значит безответственный."

    n "Я вышел из кабинета 3 с исправленным пониманием: QA-лид не кричит. Он просто говорит так, что хочется самому завести на себя баг."

    jump act1_accounting_day

label act1_accounting_day:
    $ op_clear_sprites()
    play music "audio/music/office_day.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office1_day with fade
    $ op_clear_sprites()
    n "В конце недели в офис приехала старая бухгалтер — Раиса Петровна. Ее появление изменило атмосферу сильнее, чем падение прода."
    n "Даже Виктор из QA говорил тише. Даже Артем убрал кружку с надписью 'релиз без тестов'."

    $ op_set_emotion("old_accountant", "strict")
    oldacc "Где новый разработчик?"
    $ op_set_emotion("gg", "neutral")
    p "Я здесь."
    $ op_set_emotion("old_accountant", "neutral")
    oldacc "Ты тот, который поле для бухгалтеров сломал?"
    $ op_set_emotion("gg", "neutral")
    p "Уже исправил."
    $ op_set_emotion("old_accountant", "strict")
    oldacc "Хорошо. Исправлять надо быстрее, чем ломать. Это касается не только программ."

    $ op_set_emotion("young_accountant", "worried")
    youngacc "Раиса Петровна, я подготовила отчет по переработкам. Но там опять расхождение между задачами и ручными отметками."
    $ op_set_emotion("old_accountant", "neutral")
    oldacc "Потому что задачи — это то, что люди пишут. А деньги — это то, что люди потом спрашивают."

    n "На столе лежал Excel-файл. По ощущениям, он был старше половины сотрудников."
    show ui_officepulse_salary_report at ui_panel_right

    $ op_set_emotion("gg", "neutral")
    p "У вас все расчеты в Excel?"
    $ op_set_emotion("young_accountant", "neutral")
    youngacc "Часть в Excel, часть в почте, часть в чатах, часть в голове Раисы Петровны."
    $ op_set_emotion("old_accountant", "neutral")
    oldacc "В голове надежнее. Ее хотя бы случайно не обновит DevOps."

    $ op_set_emotion("devops", "tired")
    devops "Я услышал свое имя и сразу устал."

    menu:
        "Как повести себя с бухгалтерией?"

        "Предложить автоматизировать часть отчетности":
            $ accountant_rep += 2
            $ salary_module_enabled = True
            $ op_set_emotion("gg", "neutral")
            p "Возможно, часть отчетности можно будет автоматизировать. Хотя бы связать задачи, переработки и финальные суммы."
            $ op_set_emotion("young_accountant", "neutral")
            youngacc "Вот. Вот это я и говорю уже полгода."
            $ op_set_emotion("old_accountant", "neutral")
            oldacc "Автоматизация — это когда программа быстро делает ошибку, которую человек делал медленно."
            $ op_set_emotion("gg", "neutral")
            p "Тогда можно начать с проверки, а не замены."
            $ op_set_emotion("old_accountant", "smile")
            oldacc "Хм. Не самый глупый ответ."

        "Не лезть":
            $ ethics += 1
            $ op_set_emotion("gg", "neutral")
            p "Понял. Лучше пока не буду вмешиваться."
            $ op_set_emotion("young_accountant", "neutral")
            youngacc "Мудро. Но грустно."
            $ op_set_emotion("old_accountant", "strict")
            oldacc "Молодой человек с инстинктом самосохранения. Редкость."

        "Подшутить над древним Excel":
            $ accountant_rep -= 2
            $ absurdity += 1
            $ op_set_emotion("gg", "neutral")
            p "Этот Excel, похоже, видел больше релизов, чем весь кабинет два."
            $ op_set_emotion("old_accountant", "strict")
            oldacc "Молодой человек, этот Excel видел людей, которые шутили так же. Их уже нет. А он есть."
            $ op_set_emotion("devops", "tired")
            devops "Я бы на твоем месте сделал бэкап своего будущего."

        "Помочь молодой бухгалтерше после работы":
            $ accountant_rep += 2
            $ ethics += 1
            $ human_route_open = True
            $ op_set_emotion("gg", "neutral")
            p "Мила, если хочешь, могу после работы глянуть структуру отчета. Не обещаю решение, но хотя бы пойму боль."
            $ op_set_emotion("young_accountant", "smile")
            youngacc "Спасибо. Честно, мне уже важно, что кто-то готов смотреть не только на код."
            $ op_set_emotion("old_accountant", "suspicious")
            oldacc "Смотрите. Только ничего не сохраняйте поверх."

    jump act2_project_assignment

# =========================
# АКТ 2. OFFICEPULSE
# =========================
