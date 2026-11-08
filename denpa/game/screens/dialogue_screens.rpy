
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 1.0
    xysize (1231, 277)
    padding (40, 10, 40, 40)
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    ypos 60

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xpos 20
    xysize (None, None)
    # background Frame("gui/namebox.png", 5, 5, 5, 5, tile=False, xalign=0.0)
    padding (5, 5, 5, 5)

# Style for the text with the speaker's name
style say_label:
    color '#f93c3e'
    xalign 0.0
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

transform qbar: #position of quickbar
    xalign 0.01
    yoffset 50

transform rexbar: #position of quickbar FOR REX (SPECIAL AND UNIQUE)
    xalign 0.99
    yoffset 50

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        if nvl_mode == "rex" or nvl_mode== "selfie" or nvl_mode== "creepy":
            image 'quickbar.png' at rexbar
        elif nvl_mode != "ed":
            image 'quickbar.png' at qbar
        vbox:
            if nvl_mode == "rex" or nvl_mode== "selfie" or nvl_mode== "creepy":
                style_prefix "inverse"
            elif nvl_mode !="ed":
                style_prefix "quick"

            if nvl_mode !="ed":
                textbutton _("BACK") action Rollback()
                textbutton _("LOG") action ShowMenu('history')
                textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("AUTO") action Preference("auto-forward", "toggle")
                textbutton _("SAVE") action ShowMenu('save')
                textbutton _("OPTION") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_vbox: #quickmenu box
    xalign 0.015
    yalign 0.50
    spacing 40

style inverse_vbox:
    xalign 0.965 
    yalign 0.50
    spacing 40

style quick_button:
    background None
    padding (15, 6, 15, 0)

style quick_button_text: #colors for back history etc
    size 20
    selected_color '#9a9a9a'
    idle_color "#484848"
    
style inverse_button_text: #colors for back history etc
    size 20
    selected_color '#9a9a9a'
    idle_color "#484848"

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl



screen nvl(dialogue, items=None):

    zorder 10
    window:
        if nvl_mode == "ed":
            style "ed_window"
        elif nvl_mode == "rex":
            style "rex_window"
        elif nvl_mode == "selfie":
            style "selfie_window"
        elif nvl_mode == "creepy":
            style "creepy_window"
        else:
            style "nvl_window"

        has vbox
        spacing 0

        use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                if nvl_mode == "rex" or nvl_mode== "selfie" or nvl_mode== "creepy":
                    style "rex_button"
                else:
                    style "nvl_button"

    # add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:
                    

                    text d.who:
                        if nvl_mode == "rex" or nvl_mode== "selfie" or nvl_mode== "creepy": #special rex position for special rex
                            xpos 410
                        id d.who_id

                text d.what:
                    if nvl_mode == "ed": #position for ending nvl segment
                        xpos 240
                        xsize 800
                    elif nvl_mode == "rex" or nvl_mode== "selfie" or nvl_mode== "creepy":
                        xpos 410
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 20

style ed_window:
    is default
    xfill True yfill True
    background "gui/nvl2.png"
    padding (0, 0, 0, 15)

style rex_window:
    is default
    xfill True yfill True
    background "gui/nvlrex.png"
    padding (0, 0, 0, 15)

style selfie_window:
    is rex_window
    xfill True yfill True
    background "gui/nvlselfie.png"
    padding (0, 0, 0, 15)

    
style creepy_window:
    is rex_window
    xfill True yfill True
    background "gui/nvlcreepshot.png"
    padding (0, 0, 0, 15)



# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 0, 0, 15)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 170
    ypos 30
    xsize 10
    min_width 10
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    
    xpos 170
    ypos 35 yanchor -10
    xsize 700
    min_width 100

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    xpos 170
    ypos -10 yanchor -10 #yanchor -15 for ed
    xsize 700
    min_width 100
    # is nvl_dialogue

style nvl_button: #nvl choice button position
    xpos 170
    ypos 25

style rex_button: #special rex button position for rex
    xpos 410
    ypos 25

style nvl_button_text: #nvl choice button text
    font "CarroisGothic-Regular.ttf"
    size 20
    bold False
#    xanchor 0.0

style rex_button_text:
    is nvl_button_text

## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window:
    is empty
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    is empty
    xalign 0.5

style bubble_who:
    is default
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    is default
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}
