# routes/route_drama.rpy

label route_drama_start:
    $ op_clear_sprites()
    play music "audio/music/drama.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_evening with fade
    $ op_clear_sprites()
    n "Вечером офис менялся. Днем он шумел задачами, созвонами и шутками. Ночью оставались только мониторы, гул кондиционера и правда, которую днем не успевали замечать."
    play sound "audio/sfx/call.ogg"

    n "Лера задержалась после работы. На ее экране была открыта карточка задачи."
    $ op_set_emotion("late_tester", "neutral")
    lateqa "[player_name], подойди."
    $ op_set_emotion("gg", "neutral")
    p "Что случилось?"
    $ op_set_emotion("late_tester", "sleepy")
    lateqa "Я утром видела одну причину возврата. Сейчас она другая."
    $ op_set_emotion("gg", "neutral")
    p "Может, кто-то исправил формулировку?"
    $ op_set_emotion("late_tester", "neutral")
    lateqa "Может. Но исправил так, что разработчик стал выглядеть хуже, а QA — правее."

    n "Я открыл историю. Если аудит был включен, следы были явными. Если нет — оставались только косвенные признаки: время изменения, старый кеш, фрагмент в уведомлении."

    if audit_enabled:
        system "Изменение: причина возврата. Автор: Виктор. Старое значение: 'неясное требование'. Новое значение: 'реализация не соответствует требованиям'."
        $ op_set_emotion("gg", "neutral")
        p "Автор — Виктор."
        $ op_set_emotion("late_tester", "neutral")
        lateqa "И это не первая задача."
    else:
        $ op_set_emotion("gg", "neutral")
        p "Прямой истории нет. Но уведомление в чате осталось со старой формулировкой."
        $ op_set_emotion("late_tester", "neutral")
        lateqa "То есть система еще не умеет доказывать, но уже умеет подозревать."

    menu:
        "Что сделать с подозрительными изменениями?"

        "Проверить логи самому":
            $ tech_quality += 1
            $ ethics += 1
            $ op_set_emotion("gg", "neutral")
            p "Сначала проверю сам. Без обвинений."
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Хорошо. Но не затягивай. Если это всплывет на пересмотре, будет поздно."
            jump drama_logs_self

        "Позвать DevOps":
            $ devops_rep += 1
            $ ethics += 1
            $ op_set_emotion("gg", "neutral")
            p "Нужны системные логи. Пойду к Косте."
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Он тебя проклянет. Но поможет."
            jump drama_logs_devops

        "Сразу сообщить почти-лиду разработки":
            $ dev_rep += 2
            $ qa_rep -= 1
            $ op_set_emotion("gg", "neutral")
            p "Это касается разработчиков. Сергей должен знать."
            $ op_set_emotion("late_tester", "neutral")
            lateqa "Только осторожно. Если это превратится в войну, факты утонут первыми."
            jump drama_devlead_confront

        "Промолчать до утра":
            $ ethics -= 2
            $ burnout += 1
            $ op_set_emotion("gg", "neutral")
            p "Сейчас поздно. Утром разберемся."
            $ op_set_emotion("late_tester", "sleepy")
            lateqa "Утром это уже может быть чьим-то аргументом на пересмотре."
            n "Она закрыла ноутбук. Разговор закончился, но неприятное чувство осталось."
            jump drama_salary_review


label drama_salary_review:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_salary_review with fade
    $ op_clear_sprites()
    n "Утром оказалось, что подозрительные изменения уже попали в материалы для зарплатного пересмотра."
    n "То, что вчера было странностью в логах, сегодня стало аргументом против конкретных людей."

    $ op_set_emotion("qa_lead", "neutral")
    qalead "По этой задаче разработка не выполнила требования. Причина возврата зафиксирована."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Зафиксирована когда? После обсуждения или до?"
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Сергей, если хочешь спорить, спорь с фактами."

    n "Лера посмотрела на меня. Настя тоже. Они обе знали, что факты уже не совсем факты."

    menu:
        "Вмешаться прямо на пересмотре?"

        "Остановить обсуждение и сказать о правках истории":
            $ ethics += 2
            $ qa_rep += 1
            $ op_set_emotion("gg", "neutral")
            p "Стоп. Перед тем как использовать эту причину в пересмотре, нужно проверить историю изменений. Формулировка менялась."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "У тебя есть доказательства?"
            $ op_set_emotion("gg", "neutral")
            p "Пока не все. Но достаточно, чтобы не принимать решение сейчас."
            jump drama_qahalf_confession

        "Промолчать, чтобы не устроить скандал":
            $ ethics -= 2
            $ critical_bug_hidden = True
            n "Я промолчал. Решение приняли быстро. Слишком быстро для решения, которое могло повлиять на чью-то зарплату."
            jump finale_gate

        "Поддержать сторону разработки без полной проверки":
            $ dev_rep += 2
            $ qa_rep -= 1
            $ ethics -= 1
            $ op_set_emotion("gg", "serious")
            p "Эту причину нельзя использовать. Она выглядит как попытка усилить вину разработки задним числом."
            $ op_set_emotion("qa_lead", "neutral")
            qalead "Выглядит? Хорошее слово для человека без полной картины."
            jump drama_devlead_confront

label drama_logs_self:
    $ op_clear_sprites()
    play music "audio/music/night.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene bg_night_office with fade
    $ op_clear_sprites()
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene cg_night_logs with fade
    $ op_clear_sprites()
    n "Я остался в офисе и начал сравнивать карточки задач, уведомления, старые комментарии и экспорт, который Настя случайно сохранила после тестирования."
    n "Картина была неприятной: причины возврата действительно менялись. Но не всегда в одну сторону."

    $ op_set_emotion("gg", "neutral")
    p "Здесь QA формулировку ужесточили. А здесь разработчики смягчили дефект перед отчетом."
    $ op_set_emotion("late_tester", "neutral")
    lateqa "То есть все правят историю?"
    $ op_set_emotion("gg", "serious")
    p "Не все. Но достаточно, чтобы никому нельзя было верить без логов."

    jump drama_qahalf_confession

label drama_logs_devops:
    $ op_clear_sprites()
    play music "audio/music/night.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene bg_server_room with fade
    $ op_clear_sprites()
    n "Костя сидел среди мониторов так, будто его случайно собрали из кофе, алертов и раздражения."

    $ op_set_emotion("devops", "angry")
    devops "Если ты пришел с фразой 'на пять минут', я сейчас выйду в окно."
    $ op_set_emotion("gg", "neutral")
    p "Нужны логи изменений задач. Есть подозрение, что причины возврата правили задним числом."
    $ op_set_emotion("devops", "tired")
    devops "О. То есть не инфраструктурный пожар, а человеческий. Такие хуже."

    n "Костя открыл несколько логов, сравнил таймстемпы и устало потер глаза."
    show ui_officepulse_logs at ui_panel_left

    $ op_set_emotion("devops", "tired")
    devops "Изменения были. Не только от QA. Сергей тоже правил пару записей через админку. А еще менеджер просила убрать конфликтные формулировки перед отправкой отчета китайцам."
    $ op_set_emotion("gg", "tired")
    p "А ты почему молчал?"
    $ op_set_emotion("devops", "tired")
    devops "Потому что я DevOps, а не совесть компании."

    jump drama_qahalf_confession

label drama_devlead_confront:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office1_evening with fade
    $ op_clear_sprites()
    n "Сергей выслушал меня молча. Чем дольше я говорил, тем сильнее он хмурился."

    $ op_set_emotion("dev_lead", "neutral")
    devlead "Покажи задачи."
    $ op_set_emotion("gg", "neutral")
    p "Вот. Причины возврата стали жестче."
    $ op_set_emotion("dev_lead", "angry")
    devlead "Виктор совсем охренел."
    $ op_set_emotion("gg", "neutral")
    p "Но есть и другие изменения. Здесь формулировку смягчили со стороны разработки."
    $ op_set_emotion("dev_lead", "angry")
    devlead "Это другое."
    $ op_set_emotion("gg", "neutral")
    p "Почему?"
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Потому что там требование было спорное."
    $ op_set_emotion("gg", "neutral")
    p "То есть когда вы правите контекст — это уточнение, а когда QA — манипуляция?"
    n "Сергей посмотрел на меня так, будто я внезапно стал не очень удобным союзником."

    $ op_set_emotion("dev_lead", "serious")
    devlead "Осторожнее, [player_name]. Правда без стратегии редко кому помогает."

    jump drama_qahalf_confession

label drama_qahalf_confession:
    $ op_clear_sprites()
    play music "audio/music/drama.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_corridor_evening with fade
    $ op_clear_sprites()
    n "В коридоре меня догнал Никита, QA полу-лид. Он говорил тихо, будто стены тоже были частью процесса."

    $ op_set_emotion("qa_halflead", "neutral")
    qahalf "Ты копаешь историю изменений?"
    $ op_set_emotion("gg", "neutral")
    p "Уже все знают?"
    $ op_set_emotion("qa_halflead", "neutral")
    qahalf "В маленьком офисе даже молчание ходит по кабинетам."

    $ op_set_emotion("gg", "neutral")
    p "Ты что-то знаешь?"
    $ op_set_emotion("qa_halflead", "serious")
    qahalf "Виктор часто правит формулировки перед пересмотрами. Он считает, что иначе люди не поймут серьезность ошибок."
    $ op_set_emotion("gg", "serious")
    p "Это подлог."
    $ op_set_emotion("qa_halflead", "awkward")
    qahalf "Иногда. А иногда он правит кривые баг-репорты стажеров, чтобы они не выглядели глупо."
    $ op_set_emotion("gg", "neutral")
    p "А почему не учит их нормально?"
    $ op_set_emotion("qa_halflead", "neutral")
    qahalf "Он думает, что учит. Просто его способ обучения похож на медленное утопление."

    n "Никита замолчал. Потом добавил почти шепотом."

    $ op_set_emotion("qa_halflead", "serious")
    qahalf "Марина хочет уходить. Кирилл боится заводить баги. Денис ругается с Костей из-за стендов. Все держится, потому что Виктор реально знает систему. Но люди рядом с ним не растут. Они выживают."

    menu:
        "Как поступить с этой информацией?"

        "Поговорить с Виктором лично":
            $ qa_rep += 1
            $ ethics += 1
            jump drama_talk_to_qalead

        "Собрать общее обсуждение с фактами":
            $ ethics += 2
            $ dev_rep += 1
            $ qa_rep += 1
            jump drama_common_meeting

        "Передать все руководству без обсуждения":
            $ control += 2
            $ ethics -= 1
            jump drama_send_to_management

        "Скрыть часть логов, чтобы не ломать людей":
            $ critical_bug_hidden = True
            $ ethics -= 2
            $ tech_debt += 2
            jump drama_hide_logs

label drama_talk_to_qalead:
    $ op_clear_sprites()
    play music "audio/music/drama.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office3_evening with fade
    $ op_clear_sprites()
    n "Я пришел в кабинет 3 после работы. Виктор сидел один и смотрел на старую диаграмму тестовых контуров."

    $ op_set_emotion("qa_lead", "serious")
    qalead "Если пришел обвинять — начинай с фактов. Я не люблю художественную литературу в рабочих разговорах."
    $ op_set_emotion("gg", "neutral")
    p "Причины возврата менялись после обсуждений. Иногда это влияло на пересмотр."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Да."
    $ op_set_emotion("gg", "neutral")
    p "Ты даже не отрицаешь?"
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Я исправлял формулировки. Плохой баг-репорт может похоронить реальную проблему."
    $ op_set_emotion("gg", "neutral")
    p "А хороший баг-репорт может похоронить человека, если его переписать против него."

    n "Виктор впервые не ответил сразу."

    $ op_set_emotion("qa_lead", "tired")
    qalead "Ты думаешь, я получаю удовольствие?"
    $ op_set_emotion("gg", "serious")
    p "Я думаю, ты стал системой, против которой сам должен был тестировать."
    $ op_set_emotion("qa_lead", "smirk")
    qalead "Сильная фраза. Запиши в свой OfficePulse."

    menu:
        "Что предложить Виктору?"

        "Оставить его экспертом, но убрать из зарплатных пересмотров":
            $ ethics += 2
            $ qa_rep += 2
            $ control -= 1
            $ op_set_emotion("gg", "neutral")
            p "Ты нужен как эксперт. Но не должен решать пересмотры в одиночку. Данные должны быть с контекстом и правом ответа."
            $ op_set_emotion("qa_lead", "serious")
            qalead "Ты хочешь забрать у меня рычаг."
            $ op_set_emotion("gg", "neutral")
            p "Я хочу, чтобы рычаг перестал быть дубиной."
            $ op_set_emotion("qa_lead", "angry")
            qalead "Хм. Возможно, ты не совсем бесполезен."
            jump finale_gate

        "Потребовать публичного признания":
            $ qa_rep -= 2
            $ dev_rep += 1
            $ ethics += 1
            $ op_set_emotion("gg", "neutral")
            p "Нужно признать это публично. Иначе доверия не будет."
            $ op_set_emotion("qa_lead", "angry")
            qalead "Публичная казнь редко улучшает процессы. Но часто радует толпу."
            $ op_set_emotion("gg", "serious")
            p "Это не казнь. Это ответственность."
            jump finale_gate

        "Использовать признание против него":
            $ control += 3
            $ ethics -= 3
            $ op_set_emotion("gg", "neutral")
            p "Спасибо за честность. Теперь у меня есть все, чтобы показать руководству, кто мешает процессу."
            $ op_set_emotion("qa_lead", "smirk")
            qalead "Вот теперь ты понял OfficePulse. Это не система. Это нож."
            jump finale_gate

label drama_common_meeting:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_evening with fade
    $ op_clear_sprites()
    n "На следующий день я собрал встречу. В комнате были Сергей, Виктор, Никита, Настя, Мила, Костя и Алена."

    $ op_set_emotion("gg", "neutral")
    p "OfficePulse показывает проблему не одного отдела. Историю правили разные люди. QA ужесточал формулировки. Dev иногда смягчал. Менеджмент просил убрать конфликтные поля перед китайскими отчетами."

    $ op_set_emotion("manager", "guilty")
    manager "Я не просила убрать правду. Я просила сделать ее дипломатичнее."
    $ op_set_emotion("devops", "tired")
    devops "Это когда пожар называют тепловой особенностью?"
    $ op_set_emotion("dev_lead", "serious")
    devlead "Я признаю: со стороны разработки тоже были правки. Но часто из-за спорных требований."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "А QA часто пытался вернуть смысл туда, где разработка оставила формальный чекбокс."
    $ op_set_emotion("new_tester", "formal")
    newqa "Значит, системе нужен не только аудит. Нужен комментарий стороны, история спора и финальное решение."
    $ op_set_emotion("young_accountant", "worried")
    youngacc "И нельзя использовать метрики для зарплаты без контекста. Иначе люди начнут играть в цифры."

    n "Это была первая встреча, где все спорили, но никто не мог полностью спрятаться."

    $ audit_enabled = True
    $ ethics += 2
    $ tech_quality += 2
    jump finale_gate

label drama_send_to_management:
    $ op_clear_sprites()
    play music "audio/music/bad_ending.ogg" fadeout 1.0 fadein 1.0
    scene bg_office2_evening with fade
    $ op_clear_sprites()
    n "Я выгрузил отчет и отправил руководству. Без обсуждения. Без предупреждения. Без возможности объясниться."
    n "Через два дня в офисе стало тихо. Не спокойно — именно тихо. Как в системе перед падением."

    $ op_set_emotion("qa_halflead", "serious")
    qahalf "Ты мог хотя бы дать людям сказать свою версию."
    $ op_set_emotion("gg", "neutral")
    p "Данные говорят сами."
    $ op_set_emotion("qa_halflead", "neutral")
    qahalf "Нет. Данные молчат. За них всегда говорит тот, кто делает отчет."

    $ control += 2
    jump finale_gate

label drama_hide_logs:
    $ op_clear_sprites()
    play music "audio/music/dark_ending.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene bg_office2_evening with fade
    $ op_clear_sprites()
    n "Я решил не показывать часть логов. Слишком много людей могло пострадать. Слишком много конфликтов могло взорваться сразу."
    n "На время стало спокойнее. Но спокойствие, построенное на скрытых данных, странно пахнет."

    $ op_set_emotion("late_tester", "neutral")
    lateqa "Ты убрал часть изменений?"
    $ op_set_emotion("gg", "neutral")
    p "Я оставил только то, что можно обсуждать без войны."
    $ op_set_emotion("late_tester", "serious")
    lateqa "То есть выбрал, какая правда безопасная."

    jump finale_gate

# =========================
# АРКА B. АБСУРД: КИТАЙСКИЙ РЕЛИЗ
