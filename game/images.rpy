# images.rpy
# Объявления изображений для OfficePulse.
#
# ВАЖНО: у спрайтов используются уникальные теги через underscore:
# dev_mentor, dev_lead, qa_lead и т.д.
# Так Ren'Py не будет случайно заменять dev_mentor на dev_lead,
# что происходило бы при именах вида "image dev mentor neutral".

# =========================
# Фоны
# =========================

image bg_office1_day = "images/backgrounds/bg_office1_day.png"
image bg_office1_evening = "images/backgrounds/bg_office1_evening.png"
image bg_office2_day = "images/backgrounds/bg_office2_day.png"
image bg_office2_evening = "images/backgrounds/bg_office2_evening.png"
image bg_office3_day = "images/backgrounds/bg_office3_day.png"
image bg_office3_evening = "images/backgrounds/bg_office3_evening.png"
image bg_meeting_room_day = "images/backgrounds/bg_meeting_room_day.png"
image bg_meeting_room_evening = "images/backgrounds/bg_meeting_room_evening.png"
image bg_kitchen_day = "images/backgrounds/bg_kitchen_day.png"
image bg_corridor_day = "images/backgrounds/bg_corridor_day.png"
image bg_corridor_evening = "images/backgrounds/bg_corridor_evening.png"
image bg_night_office = "images/backgrounds/bg_night_office.png"
image bg_server_room = "images/backgrounds/bg_server_room.png"
image bg_office_entrance = "images/backgrounds/bg_office_entrance.png"
image bg_call_screen = "images/backgrounds/bg_call_screen.png"

# =========================
# CG
# =========================

image cg_first_day_office2 = "images/cg/cg_first_day_office2.png"
image cg_first_demo = "images/cg/cg_first_demo.png"
image cg_night_logs = "images/cg/cg_night_logs.png"
image cg_devops_alerts = "images/cg/cg_devops_alerts.png"
image cg_chinese_call = "images/cg/cg_chinese_call.png"
image cg_salary_review = "images/cg/cg_salary_review.png"
image cg_release_crisis = "images/cg/cg_release_crisis.png"
image cg_true_ending = "images/cg/cg_true_ending.png"
image cg_bad_ending = "images/cg/cg_bad_ending.png"
image cg_dark_ending = "images/cg/cg_dark_ending.png"

# =========================
# UI / OfficePulse screens
# =========================

image ui_textbox = "images/ui/textbox.png"
image ui_namebox = "images/ui/namebox.png"
image ui_choice_idle = "images/ui/choice_idle.png"
image ui_choice_hover = "images/ui/choice_hover.png"
image ui_officepulse_dashboard = "images/ui/officepulse_dashboard.png"
image ui_officepulse_task_card = "images/ui/officepulse_task_card.png"
image ui_officepulse_logs = "images/ui/officepulse_logs.png"
image ui_officepulse_salary_report = "images/ui/officepulse_salary_report.png"
image ui_officepulse_chinese_mode = "images/ui/officepulse_chinese_mode.png"
image ui_officepulse_error = "images/ui/officepulse_error.png"

# =========================
# Спрайты персонажей
# =========================

image gg neutral = "images/sprites/gg/gg_neutral.png"
image gg serious = "images/sprites/gg/gg_serious.png"
image gg tired = "images/sprites/gg/gg_tired.png"

image old_accountant neutral = "images/sprites/old_accountant/old_accountant_neutral.png"
image old_accountant strict = "images/sprites/old_accountant/old_accountant_strict.png"
image old_accountant smile = "images/sprites/old_accountant/old_accountant_smile.png"
image old_accountant suspicious = "images/sprites/old_accountant/old_accountant_suspicious.png"

image young_accountant neutral = "images/sprites/young_accountant/young_accountant_neutral.png"
image young_accountant tired = "images/sprites/young_accountant/young_accountant_tired.png"
image young_accountant smile = "images/sprites/young_accountant/young_accountant_smile.png"
image young_accountant worried = "images/sprites/young_accountant/young_accountant_worried.png"

image late_tester neutral = "images/sprites/late_tester/late_tester_neutral.png"
image late_tester sleepy = "images/sprites/late_tester/late_tester_sleepy.png"
image late_tester sarcastic = "images/sprites/late_tester/late_tester_sarcastic.png"
image late_tester serious = "images/sprites/late_tester/late_tester_serious.png"
image late_tester soft = "images/sprites/late_tester/late_tester_soft.png"

image dev_mentor neutral = "images/sprites/dev_mentor/dev_mentor_neutral.png"
image dev_mentor smile = "images/sprites/dev_mentor/dev_mentor_smile.png"
image dev_mentor tired = "images/sprites/dev_mentor/dev_mentor_tired.png"
image dev_mentor serious = "images/sprites/dev_mentor/dev_mentor_serious.png"

image junior_dev confused = "images/sprites/junior_dev/junior_dev_confused.png"
image junior_dev happy = "images/sprites/junior_dev/junior_dev_happy.png"
image junior_dev scared = "images/sprites/junior_dev/junior_dev_scared.png"
image junior_dev confident = "images/sprites/junior_dev/junior_dev_confident.png"

image dev_lead neutral = "images/sprites/dev_lead/dev_lead_neutral.png"
image dev_lead angry = "images/sprites/dev_lead/dev_lead_angry.png"
image dev_lead serious = "images/sprites/dev_lead/dev_lead_serious.png"
image dev_lead tired = "images/sprites/dev_lead/dev_lead_tired.png"

image qa_lead neutral = "images/sprites/qa_lead/qa_lead_neutral.png"
image qa_lead angry = "images/sprites/qa_lead/qa_lead_angry.png"
image qa_lead smirk = "images/sprites/qa_lead/qa_lead_smirk.png"
image qa_lead serious = "images/sprites/qa_lead/qa_lead_serious.png"
image qa_lead tired = "images/sprites/qa_lead/qa_lead_tired.png"

image qa_halflead neutral = "images/sprites/qa_halflead/qa_halflead_neutral.png"
image qa_halflead smile = "images/sprites/qa_halflead/qa_halflead_smile.png"
image qa_halflead awkward = "images/sprites/qa_halflead/qa_halflead_awkward.png"
image qa_halflead serious = "images/sprites/qa_halflead/qa_halflead_serious.png"

image new_tester neutral = "images/sprites/new_tester/new_tester_neutral.png"
image new_tester formal = "images/sprites/new_tester/new_tester_formal.png"
image new_tester angry = "images/sprites/new_tester/new_tester_angry.png"
image new_tester soft = "images/sprites/new_tester/new_tester_soft.png"
image new_tester disappointed = "images/sprites/new_tester/new_tester_disappointed.png"

image devops tired = "images/sprites/devops/devops_tired.png"
image devops angry = "images/sprites/devops/devops_angry.png"
image devops focused = "images/sprites/devops/devops_focused.png"
image devops grateful = "images/sprites/devops/devops_grateful.png"

image manager smile = "images/sprites/manager/manager_smile.png"
image manager business = "images/sprites/manager/manager_business.png"
image manager guilty = "images/sprites/manager/manager_guilty.png"
image manager panic = "images/sprites/manager/manager_panic.png"

image frontend_dev neutral = "images/sprites/background_devs/frontend_dev_neutral.png"
image frontend_dev annoyed = "images/sprites/background_devs/frontend_dev_annoyed.png"
image backend_dev neutral = "images/sprites/background_devs/backend_dev_neutral.png"
image backend_dev serious = "images/sprites/background_devs/backend_dev_serious.png"
image silent_senior neutral = "images/sprites/background_devs/silent_senior_neutral.png"
image silent_senior comment = "images/sprites/background_devs/silent_senior_comment.png"

image manual_qa neutral = "images/sprites/background_testers/manual_qa_neutral.png"
image manual_qa tired = "images/sprites/background_testers/manual_qa_tired.png"
image auto_qa neutral = "images/sprites/background_testers/auto_qa_neutral.png"
image auto_qa angry = "images/sprites/background_testers/auto_qa_angry.png"
image qa_intern confused = "images/sprites/background_testers/qa_intern_confused.png"
image qa_intern scared = "images/sprites/background_testers/qa_intern_scared.png"
