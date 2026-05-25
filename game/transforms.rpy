# transforms.rpy
# Позиции персонажей и UI-оверлеев.
# Система op_show_speaker() держит на экране максимум 3 персонажа:
# слева, по центру и справа. Говорящий увеличивается, остальные приглушаются.

transform left_pos:
    xalign 0.23
    yalign 1.0
    zoom 0.70

transform center_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.70

transform right_pos:
    xalign 0.77
    yalign 1.0
    zoom 0.70

transform op_left_focus:
    xalign 0.22
    yalign 1.0
    zoom 0.63
    alpha 1.0

transform op_center_focus:
    xalign 0.5
    yalign 1.0
    zoom 0.63
    alpha 1.0

transform op_right_focus:
    xalign 0.78
    yalign 1.0
    zoom 0.63
    alpha 1.0

transform op_left_dim:
    xalign 0.22
    yalign 1.0
    zoom 0.61
    alpha 0.64

transform op_center_dim:
    xalign 0.5
    yalign 1.0
    zoom 0.61
    alpha 0.64

transform op_right_dim:
    xalign 0.78
    yalign 1.0
    zoom 0.61
    alpha 0.64

transform left_far:
    xalign 0.08
    yalign 1.0
    zoom 0.64

transform right_far:
    xalign 0.92
    yalign 1.0
    zoom 0.64

transform ui_panel_left:
    xalign 0.18
    yalign 0.20
    zoom 0.34
    alpha 0.92

transform ui_panel_center:
    xalign 0.5
    yalign 0.22
    zoom 0.38
    alpha 0.92

transform ui_panel_right:
    xalign 0.82
    yalign 0.20
    zoom 0.34
    alpha 0.92

transform ui_panel_big:
    xalign 0.5
    yalign 0.18
    zoom 0.46
    alpha 0.94
