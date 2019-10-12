

label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"
    $ r_name = "Y & N"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    
    $ chapter = 0
    call ch0_main
    call poem
    
    $ chapter = 1
    call ch1_main
    call poemresponse_start
    call ch1_end
    call poem

    
    
    $ chapter = 2
    call ch2_main 
    call poemresponse_start 
    call ch2_end 
    call poem 


    $ chapter = 3
    call ch3_main 
    call poemresponse_start 
    call ch3_end 

    $ chapter = 4
    call ch4_main 
    
    $ chapter = 5
    call ch5_main

    $ chapter = 6
    call ch6_main
    jump credits
    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

