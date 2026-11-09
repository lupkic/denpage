## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 375
define config.thumbnail_height = 207


screen save():

    tag menu

    add "#000"
    add HBox(Solid("#000", xsize=325),"images/quickbar horizontal.png") # The background; can be whatever

    use file_slots(_("Save"))


screen load():

    tag menu

    add "#000"
    add HBox(Solid("#000", xsize=325),"images/quickbar horizontal.png") # The background; can be whatever

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Auto saves"),
        quick=_("Quick saves"))

    use game_menu(title)

    fixed:
        xsize 500 xalign 0.5
        yoffset 110
        ysize 600
        
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.
        button:
            style "page_label"
            key_events True
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid 3 2:
            style_prefix "slot"

            for i in range(3*2):
                $ slot = i + 1

                button:
                    action FileAction(slot)
                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    ## https://www.fabriziomusacchio.com/blog/2021-08-15-strftime_Cheat_Sheet/
                    text FileTime(slot,
                            format=_("%Y-%m-%d %H:%M"),
                            empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot) style "slot_name_text"

                    # This means the player can hover this save
                    # slot and hit delete to delete it
                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        vbox:
            style_prefix "page"
            hbox:
                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

#            if config.has_sync:
#                if CurrentScreenName() == "save":
#                    textbutton _("Upload Sync"):
#                        action UploadSync()
#                else:
#                    textbutton _("Download Sync"):
#                        action DownloadSync()


style page_label: #text that says Page x. TODO broken for auto/quicksave
    xpadding 0
    ypadding -50
    xalign -0.95

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color '#C2BBC9'

style slot_grid:
    xalign 0.53 #TODO i dont think this is aligned properly but its almost 11pm.
    yalign 0.1
    spacing 40

style slot_time_text:
    size 20
    xalign 0.5

style slot_vbox:
    spacing 1

style slot_button:
    xysize (375 , 207) #TODO this seems to be our active area but it fucks up a looottt more ok wait did i do it???
    padding (20, 20, 20, 20)
    background "gui/button/slot_[prefix_]background.png"

style slot_button_text:
    size 21
    xalign 0.5
    idle_color '#aaaaaa'
    hover_color '#C2BBC9'
    selected_idle_color '#ffffff'

style page_hbox:
    xalign 0.5
    spacing 5

style page_vbox:
    xalign 0.5
    yalign 1.0
    spacing 5

style page_button:
    padding (15, 6, 15, 6)
    xalign 0.5

