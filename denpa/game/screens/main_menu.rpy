
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like



image main_menu_background = VBox(
    HBox(Solid("#000", xsize=325),"images/quickbar horizontal.png", ysize=150),
    HBox(Solid("#000", xsize=100),"gui/main_menu.jpg"),
)

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

        textbutton _("PREFERENCES") action ShowMenu("preferences")

        textbutton _("ABOUT") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("HELP") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("QUIT") action Quit(confirm=not main_menu)

