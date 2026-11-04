
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    hbox:
        for i in items:
            textbutton i.caption action i.action


style choice_hbox:
    xalign 0.5
    ypos 100
    yanchor 0
    spacing 33

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (500, 400)
    background Frame("gui/button/choice_[prefix_]background.png",
        150, 25, 150, 25, tile=False)
    padding (12, 12)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    idle_color "#ccc"
    hover_color "#fff"
    insensitive_color "#444"
