
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like


image mainmenu:
    "gui/main_menu.png"
    1.0
    "gui/main_menu2.png"
    0.5
    "gui/main_menu3.png"
    1.0
    "gui/main_menu2.png"
    0.5
    repeat

image main_menu_background = VBox(
    HBox(Solid("#000", xsize=325),"images/quickbar horizontal.png", ysize=150),"mainmenu")


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"

    hbox:
        xalign 0.5
        yoffset 40
        spacing 35

        textbutton _("START") action Start()

        textbutton _("LOAD") action ShowMenu("load")

        textbutton _("OPTIONS") action ShowMenu("preferences")

        textbutton _("ABOUT") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("HELP") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("QUIT") action Quit(confirm=not main_menu)

