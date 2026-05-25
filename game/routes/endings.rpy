# routes/endings.rpy

label finale_gate:
    $ op_clear_sprites()
    play music "audio/music/tension.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_meeting_room_evening with fade
    $ op_clear_sprites()
    n "Наступил день финального решения по OfficePulse. Система была почти готова. Или почти опасна. Иногда это одно и то же."

    if critical_bug_hidden:
        jump ending_scapegoat

    if control >= 7 or ethics <= -5:
        jump ending_dark_admin

    if absurdity >= 7 and chinese_mode_enabled:
        jump ending_absurd_button

    if devops_module_enabled and devops_rep >= 4:
        jump ending_devops

    if junior_helped and junior_rep >= 3 and route_name == "human":
        jump ending_mentor

    if newqa_rep >= 3 and tech_quality >= 4:
        jump ending_newqa

    if salary_module_enabled and accountant_rep >= 3:
        jump ending_accounting

    if qa_rep >= 4 and dev_rep < 3:
        jump ending_qa

    if dev_rep >= 4 and qa_rep < 3:
        jump ending_dev_room

    if ethics >= 6 and audit_enabled and tech_quality >= 5:
        jump ending_true

    jump ending_middle_forever

# =========================
# 10 КОНЦОВОК
# =========================

label ending_true:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_true_ending with fade
    $ op_clear_sprites()
    n "Концовка 1 из 10: «Прозрачный офис»."

    n "OfficePulse вышел позже, чем хотела Алена, сложнее, чем хотел Сергей, жестче, чем надеялась бухгалтерия, и честнее, чем было удобно почти всем."

    $ op_set_emotion("gg", "serious")
    p "Метрики нельзя смотреть без истории. Историю нельзя править без следа. Решения нельзя принимать без комментария человека."

    $ op_set_emotion("qa_lead", "neutral")
    qalead "Не люблю признавать, но это правильная система. Она мешает всем одинаково. Значит, есть шанс, что она честная."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Разработка больше не крайняя по умолчанию. QA больше не враг по должности. Это уже прогресс."
    $ op_set_emotion("young_accountant", "tired")
    youngacc "Переработки наконец-то видны. Премии можно объяснить цифрами, а не памятью."
    $ op_set_emotion("old_accountant", "neutral")
    oldacc "Память все равно важнее. Но теперь у нее есть помощник."
    $ op_set_emotion("devops", "tired")
    devops "А заявки на стенды через систему. Я впервые за год выключил рабочий чат вечером."
    $ op_set_emotion("manager", "smile")
    manager "Китайская команда согласилась на адаптированную версию. С аудитом. Они назвали это зрелым подходом."
    $ op_set_emotion("frontend_dev", "annoyed")
    fe "А цвет 'ответственный коралл'?"
    $ op_set_emotion("manager", "smile")
    manager "Оставили как тему оформления."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Я знал, что зло не исчезнет полностью."

    n "Виктора убрали с единоличных зарплатных пересмотров, но оставили главным экспертом по качеству. Сергей стал официальным тимлидом. Мила получила нормальную отчетность. Костя перестал быть единственным шлюзом в хаос."

    n "А я остался в кабинете 2. Уже не просто новичком. Человеком, который написал систему — и не дал ей стать оружием."

    $ op_set_emotion("gg", "serious")
    p "Правда не сделала офис идеальным. Но хотя бы теперь ее нельзя было тихо отредактировать."

    return

label ending_dev_room:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_first_demo with fade
    $ op_clear_sprites()
    n "Концовка 2 из 10: «Кабинет 2 победил»."

    n "OfficePulse стал главным аргументом разработки. Система показала, сколько задач возвращалось из-за спорных требований, неясных критериев и поздних изменений."

    $ op_set_emotion("dev_lead", "neutral")
    devlead "Теперь видно: не каждый возврат — вина разработчика. Иногда это просто требование, которое переобулось на ходу."
    $ op_set_emotion("dev_mentor", "serious")
    dev1 "Кабинет 2 официально перестал быть мусорным баком чужих формулировок."
    $ op_set_emotion("junior_dev", "confused")
    junior "Это значит, нас меньше будут ругать?"
    $ op_set_emotion("silent_senior", "neutral")
    senior "Нет. Но теперь иногда за дело."

    n "Виктор потерял часть влияния. QA стал осторожнее. Баги начали заводить мягче, споры фиксировались формальнее."

    $ op_set_emotion("new_tester", "formal")
    newqa "Вы выиграли спор. Но часть реальных дефектов теперь называют 'неоднозначностью требований'."
    $ op_set_emotion("gg", "neutral")
    p "Ты думаешь, мы перегнули?"
    $ op_set_emotion("new_tester", "neutral")
    newqa "Я думаю, маятник редко останавливается посередине."

    n "В кабинете 2 заказали пиццу. Все смеялись. На экране висел список отложенных багов."

    $ op_set_emotion("gg", "neutral")
    p "Мы победили. Но почему-то список проблем не стал короче."

    return

label ending_qa:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_first_demo with fade
    $ op_clear_sprites()
    n "Концовка 3 из 10: «Баг не враг»."

    n "Я сделал OfficePulse системой, которая уважала QA-процесс. Не просто считала возвраты, а показывала риски, воспроизводимость, спорность требований и цену дефекта."

    $ op_set_emotion("qa_lead", "neutral")
    qalead "Ты начал понимать. Тестирование — это не кнопки тыкать. Это защищать систему от людей, которые слишком уверены в своем коде."
    $ op_set_emotion("gg", "neutral")
    p "А разработка — это не фабрика багов."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "Иногда."

    n "Настя стала главным проводником новой модели проверки. Марина перестала писать баги как обвинения. Кирилл получил наставничество. Денис добавил автотесты на критичные сценарии OfficePulse."

    $ op_set_emotion("dev_lead", "neutral")
    devlead "Система стала лучше. Но разработчики чувствуют, что ты отдал QA слишком много веса."
    $ op_set_emotion("dev_mentor", "serious")
    dev1 "Не обижайся, но кабинет 2 теперь шутит, что ты переехал в кабинет 3 душой."

    n "Я не переехал. Просто понял, что хороший баг — это не атака. Это шанс не уронить прод."

    $ op_set_emotion("gg", "neutral")
    p "Я потерял часть доверия своих. Но стал сильнее как инженер. Иногда это тоже цена качества."

    return

label ending_accounting:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_salary_review with fade
    $ op_clear_sprites()
    n "Концовка 4 из 10: «Excel больше не бог»."

    n "OfficePulse получил модуль отчетности: переработки, премии, задачи, ручные корректировки, причины штрафов и согласования."

    $ op_set_emotion("young_accountant", "smile")
    youngacc "Теперь я могу объяснить расчет, а не просто сказать 'так получилось'."
    $ op_set_emotion("old_accountant", "neutral")
    oldacc "Не радуйся слишком рано. Программа считает быстро, но думать все равно придется."
    $ op_set_emotion("young_accountant", "tired")
    youngacc "Зато теперь думать можно не в одиночку."

    n "Раиса Петровна сначала сопротивлялась. Потом начала приносить старые правила расчета, которые никто не записывал. Мы превратили ее память в справочник."

    $ op_set_emotion("old_accountant", "neutral")
    oldacc "Вот это поле назовите не 'корректировка', а 'ручное основание'. Корректировка звучит так, будто кто-то ошибся."
    $ op_set_emotion("gg", "neutral")
    p "А разве не ошибся?"
    $ op_set_emotion("old_accountant", "strict")
    oldacc "Молодой человек, в бухгалтерии не ошибаются. В бухгалтерии уточняют период."

    n "Офис не стал идеальным. QA все еще спорил с разработкой. Менеджер все еще приносила требования. DevOps все еще уставал."
    n "Но деньги перестали быть туманом. А это изменило больше, чем казалось."

    $ op_set_emotion("gg", "neutral")
    p "Иногда самая важная прозрачность — не в коде, а в том, почему человеку заплатили именно столько."

    return

label ending_devops:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_devops_alerts with fade
    $ op_clear_sprites()
    n "Концовка 5 из 10: «Не трогайте прод руками»."

    n "Я сделал модуль DevOps-заявок. Теперь нельзя было просто написать Косте в личку: 'подними стенд, там на пять минут'."

    $ op_set_emotion("devops", "focused")
    devops "Заявка. Приоритет. Окружение. Причина. Ответственный. История. Я почти плачу, но у меня обезвоживание от кофе."

    $ op_set_emotion("manager", "smile")
    manager "А если очень срочно?"
    $ op_set_emotion("devops", "focused")
    devops "Тогда срочная заявка."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "А если прямо совсем?"
    $ op_set_emotion("devops", "focused")
    devops "Тогда инцидент."
    $ op_set_emotion("qa_lead", "neutral")
    qalead "А если QA блокирует релиз?"
    $ op_set_emotion("devops", "angry")
    devops "Тогда это не ко мне. Это к семейному психологу."

    n "Первые недели все ворчали. Потом оказалось, что стенды падают реже, доступы не теряются, а релизы можно планировать."

    n "Костя впервые ушел домой до темноты. На моем столе он оставил банку энергетика."

    $ op_set_emotion("devops", "grateful")
    devops "Это не благодарность. Это знак уважения. И предупреждение: если сломаешь модуль, я найду тебя."

    $ op_set_emotion("gg", "neutral")
    p "В офисе стало меньше хаоса. Не потому что люди стали лучше. Просто теперь хаосу нужно было создавать заявку."

    return

label ending_newqa:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_night_logs with fade
    $ op_clear_sprites()
    n "Концовка 6 из 10: «Один баг на двоих»."

    n "Я и Настя перестали работать по схеме 'разработчик сделал — тестировщик сломал'. Мы начали обсуждать риски до того, как они становились багами."

    $ op_set_emotion("new_tester", "formal")
    newqa "Здесь нужен аудит. Иначе роль администратора сможет менять историю."
    $ op_set_emotion("gg", "neutral")
    p "Согласен. А здесь я добавлю тест на старый API."
    $ op_set_emotion("new_tester", "formal")
    newqa "И негативный сценарий на китайский режим."
    $ op_set_emotion("gg", "neutral")
    p "Ты сейчас говоришь как человек, который хочет испортить мне вечер."
    $ op_set_emotion("new_tester", "neutral")
    newqa "Я хочу спасти тебе релиз. Разница тонкая, но важная."

    n "На финальном демо мы выступали вместе. Я показывал архитектуру, Настя — сценарии проверки и риски."

    $ op_set_emotion("qa_lead", "neutral")
    qalead "Сильная работа. Обоих."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "Когда dev и QA не тратят силы на войну, продукт неожиданно становится лучше. Кто бы мог подумать."
    $ op_set_emotion("late_tester", "neutral")
    lateqa "Не говорите это слишком громко. Офис может потерять основную форму досуга."

    n "После демо мы остались у окна в коридоре. За стеклом город жил так, будто в нем не существовало ни багов, ни пересмотров, ни требований от китайцев."

    $ op_set_emotion("new_tester", "soft")
    newqa "Знаешь, мне впервые кажется, что эту систему не страшно тестировать."
    $ op_set_emotion("gg", "neutral")
    p "А мне впервые кажется, что баг-репорт может быть началом разговора, а не концом самооценки."

    return

label ending_mentor:
    $ op_clear_sprites()
    play music "audio/music/good_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_first_day_office2 with fade
    $ op_clear_sprites()
    n "Концовка 7 из 10: «Теперь ты проводишь онбординг»."

    n "OfficePulse вышел позже, чем планировалось. Не все модули вошли в релиз. Не все отчеты были идеальны. Но Даня вырос."

    $ op_set_emotion("junior_dev", "confident")
    junior "Я закрыл задачу по справочнику статусов. И Настя нашла только один баг."
    $ op_set_emotion("new_tester", "neutral")
    newqa "Два. Один я простила как стилистический."
    $ op_set_emotion("junior_dev", "confident")
    junior "Это считается?"
    $ op_set_emotion("silent_senior", "neutral")
    senior "Прощенный баг — это не баг. Это аванс."

    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Ты мог закрывать задачи быстрее сам. Но выбрал учить. Это редко ценят сразу. Зато потом команда внезапно становится командой."
    $ op_set_emotion("gg", "neutral")
    p "Я просто вспомнил, как сам пришел сюда и ничего не понимал."
    $ op_set_emotion("dev_mentor", "smile")
    dev1 "Никто здесь до конца ничего не понимает. Просто некоторые делают вид увереннее."

    n "Через пару месяцев в офис пришел новый сотрудник. Артем кивнул в мою сторону."

    $ op_set_emotion("dev_mentor", "serious")
    dev1 "[player_name], проведешь онбординг?"
    $ op_set_emotion("gg", "neutral")
    p "Да."

    n "Новичок вошел в кабинет 2 и растерянно посмотрел на столы, мониторы и кружку 'QA sees you'."

    $ op_set_emotion("gg", "neutral")
    p "Главное — не спорь с QA-лидом до первой зарплаты. А если очень хочется — сначала спроси меня."

    return

label ending_absurd_button:
    $ op_clear_sprites()
    play music "audio/music/absurd.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene cg_chinese_call with fade
    $ op_clear_sprites()
    n "Концовка 8 из 10: «Красная кнопка согласования»."

    n "OfficePulse стал чудовищем гибкости. В системе было сорок два статуса, семнадцать ролей, шесть вариантов красного цвета и отдельная настройка 'показывать правду дипломатично'."

    $ op_set_emotion("frontend_dev", "annoyed")
    fe "Я добавил цвет responsible coral. Еще есть calm danger, positive block и warning harmony."
    $ op_set_emotion("qa_lead", "angry")
    qalead "Я отказываюсь тестировать цвета, которые звучат как психологический диагноз."
    $ op_set_emotion("manager", "smile")
    manager "Зато китайской стороне нравится. Они говорят, система очень адаптивная."
    $ op_set_emotion("devops", "tired")
    devops "Она не адаптивная. Она выжила после мутации."

    china "Reject button now guides user to constructive non-approval. Good."
    $ op_set_emotion("manager", "smile")
    manager "Кнопка 'Отклонить' теперь не отклоняет, а ведет к конструктивному несогласованию. Им нравится."
    $ op_set_emotion("dev_mentor", "neutral")
    dev1 "Что происходит, если нажать два раза?"
    $ op_set_emotion("frontend_dev", "neutral")
    fe "Открывается окно 'Вы уверены, что не уверены?'."
    $ op_set_emotion("silent_senior", "comment")
    senior "Я видел меньше абсурда в легаси без тестов."

    n "Руководство было довольно. Китайская команда была довольна. Алена получила благодарность. Система стала международной."

    $ op_set_emotion("gg", "neutral")
    p "Я не знаю, сделал ли я хорошую систему. Но я точно сделал систему, которую можно настроить под любую форму отрицания реальности."

    return

label ending_scapegoat:
    $ op_clear_sprites()
    play music "audio/music/bad_ending.ogg" fadeout 1.0 fadein 1.0
    scene cg_bad_ending with fade
    $ op_clear_sprites()
    n "Концовка 9 из 10: «Козел отпущения»."

    n "Я скрыл проблему. Не потому что хотел зла. Потому что устал, боялся сорвать релиз и надеялся, что успею исправить потом."
    n "Потом не наступило. Наступил понедельник."

    system "Ошибка: история задачи изменена через старый API. Данные отчета не совпадают с текущим состоянием."

    $ op_set_emotion("young_accountant", "tired")
    youngacc "Отчет по премиям неверный. У нас суммы не сходятся с задачами."
    $ op_set_emotion("qa_lead", "serious")
    qalead "История изменений недостоверна. Я предупреждал."
    $ op_set_emotion("dev_lead", "neutral")
    devlead "[player_name], ты знал о баге?"
    $ op_set_emotion("new_tester", "neutral")
    newqa "Скажи, что не знал."

    n "Я молчал слишком долго. Этого хватило."

    $ op_set_emotion("devops", "focused")
    devops "Я откатил систему. Ночь потеряна. Доверие тоже."
    $ op_set_emotion("manager", "panic")
    manager "Китайское демо отменено. Руководство просит объяснение."
    $ op_set_emotion("old_accountant", "strict")
    oldacc "Молодой человек, ошибки бывают у всех. Но скрытые ошибки стоят дороже."

    n "Через неделю OfficePulse передали другой команде. Я остался в кабинете 2, но кабинет стал другим. Или другим стал я."

    $ op_set_emotion("gg", "tired")
    p "Я хотел пережить один релиз. В итоге стал причиной, по которой системе больше не верили."

    return

label ending_dark_admin:
    $ op_clear_sprites()
    play music "audio/music/dark_ending.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/rain.ogg" fadein 1.0
    scene cg_dark_ending with fade
    $ op_clear_sprites()
    n "Концовка 10 из 10: «Администратор офиса»."

    n "Я понял, что OfficePulse может больше, чем помогать. Он может показывать слабые места людей. А тот, кто показывает слабые места, получает власть."

    n "Я добавил скрытый дашборд: опоздания, конфликтные комментарии, частоту возвратов, срочные просьбы к DevOps, правки истории, влияние на пересмотры, связи между сотрудниками."
    show ui_officepulse_dashboard at ui_panel_big

    $ op_set_emotion("manager", "business")
    manager "Руководству понравилось. Очень. Они говорят, это новый уровень прозрачности."
    $ op_set_emotion("young_accountant", "worried")
    youngacc "Это не прозрачность. Это наблюдение."
    $ op_set_emotion("devops", "tired")
    devops "Теперь хаос не исчез. Просто у него появился админ."
    $ op_set_emotion("qa_lead", "serious")
    qalead "Ты сделал то, чего все боялись. Не систему качества. Систему контроля."
    $ op_set_emotion("gg", "neutral")
    p "Контроль тоже качество."
    $ op_set_emotion("qa_lead", "serious")
    qalead "Нет. Контроль — это то, что остается, когда людям больше не доверяют."

    n "Виктора отстранили от пересмотров. Сергей стал осторожнее. Тестировщики начали писать меньше комментариев. Разработчики перестали шутить в задачах. DevOps больше не отвечал в личке без заявки."

    n "Офис стал эффективнее. Холоднее. Тише."

    n "Мое рабочее место перенесли из кабинета 2 в отдельную переговорку. На большом экране висел дашборд всех сотрудников. Зеленые, желтые, красные зоны. Риски. Поведение. Динамика."

    $ op_set_emotion("gg", "neutral")
    p "Теперь я точно знаю, кто здесь работает плохо. Осталось решить, кто здесь вообще нужен."

    return

label ending_middle_forever:
    $ op_clear_sprites()
    play music "audio/music/office_evening.ogg" fadeout 1.0 fadein 1.0
    play ambient "audio/sfx/office_noise.ogg" fadein 1.0
    scene bg_office2_day with fade
    $ op_clear_sprites()
    n "Дополнительная нейтральная концовка: «Вечный мидл»."
    n "Эта концовка срабатывает, если ни одна сильная ветка не набрала достаточно веса. Ее можно оставить как скрытую или заменить одной из основных."

    n "OfficePulse вышел. Формально. Задачи создавались, баги связывались, отчеты открывались, китайский режим существовал в настройках, DevOps-заявки лежали в планах."

    $ op_set_emotion("dev_lead", "tired")
    devlead "Нормально. Для первого релиза пойдет."
    $ op_set_emotion("qa_lead", "tired")
    qalead "Средне. Но не катастрофа."
    $ op_set_emotion("manager", "smile")
    manager "Главное, что можно показать прогресс."
    $ op_set_emotion("devops", "tired")
    devops "Прогресс — это когда старый хаос завернули в новый интерфейс."

    n "Прошел год. Я все еще сидел в кабинете 2. Новые люди приходили и уходили. Виктор все еще душил пересмотры. Мила все еще сверяла часть отчетов руками. Костя все еще выглядел так, будто его деплоили без сна."

    $ op_set_emotion("gg", "neutral")
    p "Я не провалился. Не победил. Не изменил офис. Просто стал его частью."
    n "Иногда самое страшное — не плохая концовка. Иногда самое страшное — нейтральная."

    return

# =========================
# КОНЕЦ ФАЙЛА
# =========================
