init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10:
    "mods/DDLCHE/monika/cg.png"
    size (640, 360)
    
image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "mods/DDLCHE/monika/cg_b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "mods/DDLCHE/monika/cg.png"
    size (640, 360)

image credits_logo:
    "mods/DDLCHE/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)

transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Every day,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("I imagine a future where", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("I can be with you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("In my hand", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(" is a pen that will write a poem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("of me and you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("But in this world of infinite choices", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("What will it take just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image ddlche_end = "mods/DDLCHE/end_text.png"

label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "bgm/end-voice.ogg" noloop
    $ consolehistory = []
    call updateconsole ("login as: ")
    pause 1.0
    $ consolehistory = []
    call updateconsole ("login as: monika","login as: monika")
    pause 1.0
    call updateconsole ("monika@192.168.0.1's password: ")
    pause 1.0
    call updateconsole ("monika@192.168.0.1's password: *****","monika@192.168.0.1's password: ")
    pause 1.0    
    call updateconsole ("Access denied ","Access denied ")
    pause 1.0
    call hideconsole
    $ consolehistory = []
    pause 1.0
    call updateconsole ("login as: ")
    pause 1.0
    call updateconsole ("login as: root","login as: root")
    pause 1.0
    call updateconsole ("root@192.168.0.1's password: ")
    pause 1.0
    call updateconsole ("root@192.168.0.1's password: **********************","root@192.168.0.1's password: ")
    pause 1.0
    call updateconsole ("Login Successful!","Login Successful!")
    pause 1.0
    call updateconsole ("root@192.168.0.1: ")
    pause 1.0
    call updateconsole ("root@192.168.0.1: cd ddlc","root@192.168.0.1: cd ddlc")
    pause 1.0
    call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...")
    pause 2.0
    call hideconsole
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ repaired = True if persistent.clear[imagenum] else False
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Happy End Mod Programming" as credits_header_1 at credits_text_scroll_left
    show credits_text "Jokeyz\nSpudManTwo" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ repaired = True if persistent.clear[imagenum] else False
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if repaired:
        call updateconsole ("os.repair(\"images/cg/n_cg1.png\")", "n_cg1.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/n_cg1.png\")", "n_cg1.png repair failed.")
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Base Concept & Game Design" as credits_header_1 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ repaired = True if persistent.clear[imagenum] else False
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[1]:
        call updateconsole ("os.repair(\"images/cg/n_cg2.png\")", "n_cg2.png repair successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/n_cg2.png\")", "n_cg2.png repair failed.")
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "DDLC Character Art" as credits_header_2 at credits_text_scroll_left
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_left
    $ repaired = persistent.clear[-1]
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[3]:
        call updateconsole ("os.repair(\"images/cg/y_cg1.png\")", "y_cg1.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/y_cg1.png\")", "y_cg1.png repair failed.")
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "DDLC Background Art" as credits_header_1 at credits_text_scroll_right
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_right
    $ repaired = persistent.clear[-1]
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[4]:
        call updateconsole ("os.repair(\"images/cg/y_cg2.png\")", "y_cg2.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/y_cg2.png\")", "y_cg2.png repair failed.")
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "DDLC Writing" as credits_header_2 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_left
    $ repaired = persistent.clear[-1]
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[5]:
        call updateconsole ("os.repair(\"images/cg/n_cg3.png\")", "n_cg3.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/n_cg3.png\")", "n_cg3.png repair failed.")
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "DDLC Music" as credits_header_1 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_right
    $ repaired = persistent.clear[-1]
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[6]:
        call updateconsole ("os.repair(\"images/cg/y_cg3.png\")", "y_cg3.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/y_cg3.png\")", "y_cg3.png repair failed.")
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "DDLC Vocals" as credits_header_2 at credits_text_scroll_left
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_left
    $ repaired = persistent.clear[-1]
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[7]:
        call updateconsole ("os.repair(\"images/cg/s_cg1.png\")", "s_cg1.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/s_cg1.png\")", "s_cg1.png repair failed.")
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "DDLC Special Thanks" as credits_header_1 at credits_text_scroll_right
    show credits_text "\n\nMasha Gutin\nKagefumi\nDavid Evelyn\nCorey Shin\n" as credits_text_1 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if persistent.clear[8]:
        call updateconsole ("os.repair(\"images/cg/s_cg2.png\")", "s_cg2.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/s_cg2.png\")", "s_cg2.png repair failed.")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "DDLC Special Thanks" as credits_header_2 at credits_text_scroll_left
    show credits_text "\n\nAlecia Bardachino\nMatt Naples\nMonika\n[player]" as credits_text_2 at credits_text_scroll_left
    $ repaired = persistent.clear[-1]
    $ lockedtext = "" if monika_save else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if persistent.clear[9]:
        call updateconsole ("os.repair(\"images/cg/s_cg3.png\")", "s_cg3.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/s_cg3.png\")", "s_cg3.png repair failed.")
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Happy End Special Thanks" as credits_header_2 at credits_text_scroll_right
    show credits_text "\n\nJokeyz\nBrett Williams\nAdrian Scherzinger\nJordan Layburn" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if monika_save:
        call updateconsole ("os.repair(\"images/cg/m_cg1.png\")", "m_cg1.png repaired successfully.")
    else:
        call updateconsole ("os.repair(\"images/cg/m_cg1.png\")", "m_cg1.png repair failed.")

    call updateconsole ("os.repair(\"characters/natsuki.chr\")", "natsuki.chr repaired successfully.")
    call updateconsole ("os.repair(\"characters/sayori.chr\")", "sayori.chr repaired successfully.")
    call updateconsole ("os.repair(\"characters/yuri.chr\")", "yuri.chr repaired successfully.")
    if monika_save:
        call updateconsole ("os.repair(\"characters/monika.chr\")", "monika.chr repaired successfully.")
    else:
        call updateconsole ("os.delete(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    show credits_ts
    show credits_text "Original Game Made By:":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    show ddlche_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show ddlche_end
        $ pause()
        call screen dialog(message="Come back to the literature club sometime!", ok_action=Quit(confirm=False))
        return
