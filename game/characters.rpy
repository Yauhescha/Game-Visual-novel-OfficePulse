# characters.rpy
# Персонажи OfficePulse + автоматический показ спрайтов.
#
# Основная логика:
# - перед репликой в сценарии выставляется эмоция через op_set_emotion(tag, emotion);
# - callback персонажа вызывает op_show_speaker(tag);
# - на экране одновременно держится максимум 3 персонажа;
# - говорящий персонаж увеличивается, остальные уменьшаются и приглушаются;
# - если приходит четвертый персонаж, самый старый скрывается.

init python:
    renpy.music.register_channel("ambient", mixer="sfx", loop=True, stop_on_mute=True)

    OP_SPRITE_TAGS = [
        "gg",
        "old_accountant",
        "young_accountant",
        "late_tester",
        "dev_mentor",
        "junior_dev",
        "dev_lead",
        "qa_lead",
        "qa_halflead",
        "new_tester",
        "devops",
        "manager",
        "frontend_dev",
        "backend_dev",
        "silent_senior",
        "manual_qa",
        "auto_qa",
        "qa_intern",
    ]

    OP_DEFAULT_EMOTIONS = {
        "gg": "neutral",
        "old_accountant": "neutral",
        "young_accountant": "neutral",
        "late_tester": "neutral",
        "dev_mentor": "neutral",
        "junior_dev": "confused",
        "dev_lead": "neutral",
        "qa_lead": "neutral",
        "qa_halflead": "neutral",
        "new_tester": "neutral",
        "devops": "tired",
        "manager": "smile",
        "frontend_dev": "neutral",
        "backend_dev": "neutral",
        "silent_senior": "neutral",
        "manual_qa": "neutral",
        "auto_qa": "neutral",
        "qa_intern": "confused",
    }

    OP_CURRENT_EMOTIONS = {}
    OP_ONSCREEN = []
    OP_TAG_TO_SLOT = {}
    OP_SLOTS = ["left", "center", "right"]

    def op_set_emotion(tag, emotion):
        OP_CURRENT_EMOTIONS[tag] = emotion

    def op_clear_sprites():
        for tag in OP_SPRITE_TAGS:
            renpy.hide(tag)
        OP_ONSCREEN[:] = []
        OP_TAG_TO_SLOT.clear()

    def op_hide_sprite(tag):
        if tag in OP_ONSCREEN:
            OP_ONSCREEN.remove(tag)
        if tag in OP_TAG_TO_SLOT:
            del OP_TAG_TO_SLOT[tag]
        renpy.hide(tag)

    def op_prune_invisible():
        # После scene Ren'Py сам очищает экран. Этот метод синхронизирует внутренний список.
        for tag in list(OP_ONSCREEN):
            try:
                if not renpy.showing(tag):
                    OP_ONSCREEN.remove(tag)
                    OP_TAG_TO_SLOT.pop(tag, None)
            except Exception:
                pass

    def op_free_slot():
        used = set(OP_TAG_TO_SLOT.values())
        for slot in OP_SLOTS:
            if slot not in used:
                return slot
        return OP_SLOTS[0]

    def op_transform_for(slot, focused):
        name = "op_%s_%s" % (slot, "focus" if focused else "dim")
        return getattr(renpy.store, name)

    def op_refresh_sprites(focus_tag=None):
        for tag in list(OP_ONSCREEN):
            emotion = OP_CURRENT_EMOTIONS.get(tag, OP_DEFAULT_EMOTIONS.get(tag, "neutral"))
            image_name = "%s %s" % (tag, emotion)
            slot = OP_TAG_TO_SLOT.get(tag, op_free_slot())
            transform = op_transform_for(slot, tag == focus_tag)
            zorder = 20 if tag == focus_tag else 10
            renpy.show(image_name, at_list=[transform], zorder=zorder)

    def op_show_speaker(tag):
        op_prune_invisible()

        if tag not in OP_ONSCREEN:
            if len(OP_ONSCREEN) >= 3:
                old_tag = OP_ONSCREEN.pop(0)
                renpy.hide(old_tag)
                OP_TAG_TO_SLOT.pop(old_tag, None)

            OP_ONSCREEN.append(tag)
            OP_TAG_TO_SLOT[tag] = op_free_slot()
        else:
            # Перемещаем говорящего в конец очереди, чтобы он не исчезал первым.
            OP_ONSCREEN.remove(tag)
            OP_ONSCREEN.append(tag)

        op_refresh_sprites(tag)

    def op_sprite_callback(tag):
        def _callback(event, interact=True, **kwargs):
            if event == "show":
                op_show_speaker(tag)
        return _callback

# =========================
# Персонажи без спрайтов
# =========================

define n = Character(None)
define china = Character("Китайская сторона", color="#ffdfba")
define system = Character("OfficePulse", color="#bdb2ff")

# =========================
# Главный герой
# =========================

define p = Character("[player_name]", color="#c8e6ff", callback=op_sprite_callback("gg"))

# =========================
# Основные персонажи
# =========================

define dev1 = Character("Артем", color="#8fd18f", callback=op_sprite_callback("dev_mentor"))
define lateqa = Character("Лера", color="#ffb6d5", callback=op_sprite_callback("late_tester"))
define oldacc = Character("Раиса Петровна", color="#f0d28a", callback=op_sprite_callback("old_accountant"))
define youngacc = Character("Мила", color="#ffe0a3", callback=op_sprite_callback("young_accountant"))
define devlead = Character("Сергей", color="#a8d8ff", callback=op_sprite_callback("dev_lead"))
define qalead = Character("Виктор", color="#ff8a8a", callback=op_sprite_callback("qa_lead"))
define qahalf = Character("Никита", color="#b7f7d4", callback=op_sprite_callback("qa_halflead"))
define newqa = Character("Настя", color="#ffc6ff", callback=op_sprite_callback("new_tester"))
define devops = Character("Костя", color="#d0d0d0", callback=op_sprite_callback("devops"))
define junior = Character("Даня", color="#d7c1ff", callback=op_sprite_callback("junior_dev"))
define manager = Character("Алена", color="#ffd1a1", callback=op_sprite_callback("manager"))

# =========================
# Фоновые персонажи
# =========================

define fe = Character("Паша", color="#b5e8ff", callback=op_sprite_callback("frontend_dev"))
define legacy = Character("Игорь", color="#b0ffb0", callback=op_sprite_callback("backend_dev"))
define senior = Character("Слава", color="#e0e0e0", callback=op_sprite_callback("silent_senior"))
define manualqa = Character("Марина", color="#ffcad4", callback=op_sprite_callback("manual_qa"))
define autoqa = Character("Денис", color="#caffbf", callback=op_sprite_callback("auto_qa"))
define qaintern = Character("Кирилл", color="#fdffb6", callback=op_sprite_callback("qa_intern"))
