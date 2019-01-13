label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    if ch4_scene == "sayori":
        call ch5_end_sayori
        return
    if ch4_scene == "harem":
        call ch5_end_harem
        return
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    if ch4_scene == "natsuki":
        "I managed to carry all the cupcakes myself by carefully stacking two trays."
        "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    if ch4_scene == "lonely":
        "I'm more excited for it to be over so I can spend time with everyone at the festival."
    else:
        "I'm more excited for it to be over so I can spend time with [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    play music t2
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    if monika_complete:
        "They must be the ones we prepared that has all the poems we're performing."
    else:
        "They must be the ones she prepared that has all the poems we're performing."
    if ch4_scene == "natsuki":
        "In the end, I found a random poem online that I thought Natsuki would like, and submitted it."
    else:
        "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    if ch4_scene == "lonely":
        "I say that but immediately get a sinking sensation in my stomach..."
    else:
        "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m "You shouldn't worry about her so much."
    m "I told you that I would make sure that she's fine."
    m "It's kinda hurtful that you'd think I'd go back on my word."
    if monika_complete:
        jump ch5_end_monika
        return
    if ch4_scene == "lonely":
        jump ch5_end_lonely
        return
    "I want to trust Monika, but something just doesn't sit right with me."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika zorder 1 at thide
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practiced."    
    show monika 2d at t11
    m "What's wrong?"
    mc "Ah, nothing..."
    m 2r "Sigh"
    m "I guess you'll just never trust me after all..."
    m "Not that I blame you."
    "I check my phone and suddenly see a message from Sayori."
    "She apologizes for waking up late and says that she'll be at school soon."
    "I feel oddly relieved."
    "I apologize about not waiting for her and tell her to hurry up."
    "Not too much longer, everyone else shows up."
    "."
    ".."
    "..."
    call expression "ch5_end_" + ch4_scene
    return
    
label ch5_end_monika:
    mc "No, it's not like that you."
    mc "I trust you really."
    mc "I just can't help but worry about Sayori sometimes."
    m 1e "If you say so."
    "I pick up one of the pamphlets we made"
    mc "These really did turn out well."
    m 5a "You really think so?"
    m "I mean it's mostly because I had so much help."
    mc "Well I certainly had fun doing it."
    m 1k "That's good to hear."
    m 3k "I'd ask you to stop by some other time."
    m "But I don't want to be a hassle."
    show monika at thide
    hide monika
    with wipeleft
    "Monika continues setting everything up."
    "I can't help but think back to what Sayori and Yuri mentioned yesterday."
    "I check my phone and suddenly see a message from Sayori."
    "She apologizes for waking up late and says that she'll be at school soon."
    "I feel oddly relieved."
    "I apologize about not waiting for her and tell her to hurry up."
    "She asks if I've talked to Monika yet."
    "I don't know what to tell her, so I just wait for her to get here and see for herself."
    show natsuki 4a at t21
    show yuri 1a at t22
    with wipeleft_scene
    "Meanwhile, Yuri and Natsuki show up."
    hide yuri
    hide natsuki
    with wipeleft
    "."
    ".."
    "..."
    show yuri 1a at t11
    "Yuri puts the final touches on the banner."
    mc "Hey Yuri"
    show yuri 1p at hop
    "Yuri jumps so hard that she almost messes up the banner." 
    y 3n "Y-Yeah?"
    mc "About what you mentioned about Monika."
    y 3f "A-...Ah..."
    y 1q "Forget about it."
    y "It was out of line for me to make such baseless assumptions."
    y "I'd hate to be someone who started a rumor."
    mc "I was just going to ask if you know anything I could for her."
    mc "Sayori and I visited her last night."
    mc "Monika definitely seems to be off."
    y 1l "Well..."
    y 2f "If it was me..."
    y "I guess it would mean a lot if you stayed for her performance today."
    y "She's going last today."
    y "And it may not hurt to help her clean up."
    y "But that's just what I would do..."
    y 3t "I'm sorry I can't be of more help."
    mc "No"
    mc "That's really helpful."
    mc "Thanks Yuri."
    y 3f "If you don't mind me asking."
    y "Why the sudden interest in our President here?"
    "I honestly don't have a proper answer to Yuri's question."
    "Sure, I kind of knew Monika before all of this."
    "But never intimately."
    mc "Well I never knew her too well before."
    mc "And I guess I've decided that I want to now."
    y 1b "Huhu"
    y "If you say so."
    show yuri at thide
    hide yuri
    "Yuri continues working on the banner with a smile."
    show sayori 4p at t11
    with wipeleft_scene
    "Sayori shows up not too much later as the festival is about to start."
    s "Sorry, i'm late!"
    mc "It's okay."
    hide sayori
    with wipeleft
    "We barely get everything together and ready by the time people start showing up."
    show yuri 1a at t44
    show natsuki 1a at t43
    show monika 1a at t42
    show sayori 1a at t41 
    "I feel nervous in front of everyone."
    "But if the other four can do it, then so can I."
    "I get up and give my poem before anyone shows up."
    "..."
    show yuri 3d at t44
    show natsuki 4z at t43
    show monika 2k at t42
    show sayori 4r at t41
    with wipeleft
    "The entire club applauds."
    "But, it feels like a hollow victory."
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "Still, I'm just glad to have it be over with."
    show natsuki 3d at t11
    "Natsuki gives her performance while the crowd is still somewhat thin."
    "It goes over fairly well, although she is pretty clearly just happy to be done with it all."
    "She mingles around for a bit until she slips away to enjoy the rest of the festival."
    show natsuki at rhide
    hide natsuki
    show yuri 4b at l11
    "After her is Yuri."
    "Just like the other day, Yuri has a little bit of a weak start because of her nerves."
    show yuri 3f
    "But once she gets into her groove she performs incredibly well."
    show yuri 3b 
    "The crowd gives her quite the welcoming applause."
    "She ends up running off because of all the attention."
    show yuri at thide
    hide yuri
    "After that is Sayori."
    show sayori 1a at l11
    "Sayori gets up and gives a great performance."
    show sayori 2r
    "It exudes happiness and enthusiasm."
    show sayori 4q
    "After she finishes up, everyone seems to be in a better mood."
    show sayori at rhide
    hide sayori
    "Sayori comes over to me."
    show sayori 1g at t11
    s "I talked to Monika earlier."
    mc "And?"
    s "I hate to say this"
    s 1h "But I think you should spend some more time with her."
    s "You seem to brighten her mood."
    mc "Really?"
    s 3l "I mean..."
    s "You kind of have that effect."
    s 3k "Besides..."
    s "If I can't make someone happy."
    s 1j"Then you have to..."
    mc "I don't think that's how this works."
    s 4l "Well too bad."
    s 2l "I'm going to go check out the rest of the festival."
    show sayori at lhide
    hide sayori
    "Sayori ends up leaving."
    "The only two club members left are Monika and I."
    "I go up to her."
    stop music fadeout .5
    play music t5
    show monika 1q at t11
    mc "Hey Monika."
    m 1d "Yeah?"
    mc "I was curious if I could see more of your poems."
    mc "I think they're really cool."
    mc "Even if I don't always get it."
    show monika 1s at h11
    "Monika seems genuinely stunned."
    m 3l "Yeah"
    m 1e "Sure"
    m "Let me go see if I brought one with me."
    show monika at thide
    hide monika
    "..."
    show monika 1a at t11
    "She comes back a couple minutes later brandishing a piece of paper."
    m 1e "I don't if you've seen this one before."
    m "But..."
    "Monika hands me the poem."
    show monika at thide
    hide monika
    call showpoem (poem_m4, music=True)
    show monika 3b at l11
    "I don't get to say anything to Monika before she gets up to perform her poem."
    "."
    ".."
    "..."
    show monika 1j
    with wipeleft_scene
    "Her performance can only be described as other-worldly."
    "After everyone has applauded for her, she gets their attention."
    m 1b "I want to thank everybody for coming."
    m "You all have truly made today a special day."
    m 1k "Some more than others."
    "As she says that, she looks directly at me."
    m 2a "That being said, we're going to have to clean up now."
    m "There will be a fireworks show in a little bit."
    m 2k "So you all should find a good spot to watch it from."
    hide monika with wipeleft
    "Everyone slowly filters out."
    "Eventually it's just Monika and I."
    "I start helping her take everything down."
    show monika 3e at t11
    m "You really didn't have to stay here with me."
    m "I'm not gonna mess anything up this time."
    m 1p "Besides, shouldn't you be spending with the others?"
    mc "Well"
    mc "To be honest"
    mc "I'd rather stay here and help you."
    show monika 2h
    "All of a sudden she seems really angry."
    m 2i "You really are the worst."
    m "You know you shouldn't even be bothered with me."
    m 2r "Yet here you are, continuing to torture me with your presence."
    m "Haven't I already been punished enough?"
    m 5b "You can't have any idea how hard this all is!"
    "I don't know what to say to her."
    "So I say the only thing I can think of."
    mc "Then let me help."
    m 2i "What?"
    mc "I don't know what's going on with you."
    mc "But everyone is really worried about you."
    mc "Especially me."
    show monika 1d
    "Monika looks at me with pure confusion"
    stop music fadeout 2.0
    show monika 1o
    "Then she looks down at the ground"
    m 1p "If anything"
    m "I'm just becoming like them."
    mc "And that's the problem."
    play music "bgm/monika-end.ogg"    
    mc "We don't want you to be them."
    mc "We want you to be you Monika."
    mc "I think you're an absolutely amazing person."
    mc "And I wouldn't want you to be anything else."
    mc "Honestly, everyone else is really cool."
    mc "But to me, you're probably the most amazing."
    mc "I don't know if this is coming right or anything."
    mc "But I kinda like you."
    show monika 1s at h11
    mc "And I want to spend more time with you."
    mc "So if nothing else, please just continue to be yourself."
    show monika 1f
    "After confessing to Monika, she just looks at me."
    "If she was stunned before."
    "Then this is pure paralysis."
    "I wait for her to reject my confession."
    "After all, she's completely out of my league."
    m 1r "I think I get it now."
    m "You don't just love the club."
    m "You don't just love one person in the club."
    m 1p "You love it all."
    m "You're infinitely selfish."
    m "You want to be friends with everyone."
    m 1u "And you want to be with me?"
    m "That being said."
    m "I can't help myself."
    m 1t "I still love you."
    m "No matter what happens."
    m "No matter what we have gone through."
    m "No matter what."
    show monika 1u
    pause .1
    $ _window_hide(trans=False)
    show monika at uface
    scene black with Dissolve(0.25)
    m "I love you"
    hide monika
    "She wraps her arms around me."
    "I hold her incredibly tight."
    "I can't believe everything is actually working out."
    m "It's gonna be tough."
    scene mrd with Dissolve(1)
    show monika 1u at tface
    m "But I guess I'm finally..."
    $ _window_hide(trans=False)
    show monika 1v with Dissolve(1)
    m "...Getting my {i}Happy Ending{/i}."
    scene black with Dissolve(1)
    "..."
    "..."
    "..."
    return

label ch5_end_sayori:
    scene scg2 with dissolve_cg
    "I think back to what we talked about yesterday."
    "I decide to go check up on her."
    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "That really is something that a boyfriend would do, isn't it?"
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    scene sayori_bedroom with wipeleft
    "As the door opens, I see Sayori still in bed."
    "She must still be sound asleep."
    "I think back to a couple days ago."
    "Was she watching me sleep just like this?"
    "She seems so peaceful."
    "A few seconds pass."
    "She opens her eyes."
    show sayori 1bm at h11
    s "Uwaa!"
    show sayori at thide
    with vpunch
    hide sayori
    "Sayori jumps awake and then throws her blanket over her head."
    mc "You dummy."
    mc "You overslept."
    s "So you came to wake me up?"
    mc "Well yeah.."
    mc "That's what boyfriends do, right?"
    "I hear her giggle from under the blanket."
    mc "What is it?"
    show sayori 4br at t11
    s "Nothing."
    s "I guess I'm still just getting used to that."
    show sayori at thide
    hide sayori
    "I do everything I can to help Sayori get ready for the day so that way we can both make it on time."
    scene bg club_day with wipeleft_scene
    "Unfortunately we're still the last two to arrive at the club."
    show sayori 1p at t21
    show monika 1b at t22
    "Monika seems to smile about something."
    m 3b "I see you made sure to bring Sayori with you this time."
    mc "Yeah, I couldn't let her be late on the day of the festival."
    show monika 1j
    "Monika smiles a little more as I hand over the poster to Yuri to finish up."
    show monika at thide
    show sayori at thide
    hide monika
    hide sayori
    "I apologize to Yuri for showing up late like this."
    "She insists that it's fine."
    "She says something about it being romantic but I don't follow."
    "I pick up one of the pamphlets sitting on one of the desks."
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    "For a minute, I swear I see something happen with Sayori's poem, but it's the same one she practiced."
    show monika 2d at t11
    m "What's wrong?"
    mc "Ah, nothing..."
    m 2r "Sigh"
    m "I guess you'll just never trust me after all..."
    m "Not that I blame you."
    show monika at thide
    hide monika
    "The entire festival starts to pick up as a lot of guests start showing up."
    "I feel nervous in front of everyone."
    "But if the other four can do it, then so can I."
    "I get up and give my poem before anyone shows up."
    "..."
    show yuri 3d at t44
    show natsuki 4z at t43
    show monika 2k at t42
    show sayori 4r at t41
    with wipeleft
    "The entire club applauds."
    "But, it feels like a hollow victory."
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "Still, I'm just glad to have it be over with."
    show natsuki 3d at t11
    "Natsuki gives her performance while the crowd is still somewhat thin."
    "It goes over fairly well, although she is pretty clearly just happy to be done with it all."
    "She mingles around for a bit until she slips away to enjoy the rest of the festival."
    show natsuki at rhide
    hide natsuki
    show yuri 4b at l11
    "After her is Yuri."
    "Just like the other day, Yuri has a little bit of a weak start because of her nerves."
    show yuri 3f
    "But once she gets into her groove she performs incredibly well."
    show yuri 3b 
    "The crowd gives her quite the welcoming applause."
    "She ends up running off because of all the attention."
    show yuri at thide
    hide yuri
    "After that is Sayori."
    show sayori 1a at l11
    "Sayori gets ready to perform hers."
    "I give a slight nod to her, knowing she can do it."
    show sayori 4r at t11
    "She immediately goes overboard with it."
    show sayori at thide
    hide sayori
    "There's times where I almost can't stop myself from laughing."
    "The crowd seems to be enjoying it as much as she is."
    "By the time she finishes, everyone is either laughing or applauding."
    "It really does amaze me how she can be such a big bright light to everyone."
    "Especially when she herself is having so many problems."
    show sayori 1x at t11
    s "So did I do good?"
    mc "Yeah, that was amazing."
    mc "And to think that you were gonna be late today."
    s 4s "Hehe"
    s "That's why I have you."
    s "To wake me up and get me going"
    "I can't help but blush a little at the compliment."
    s 4q "Well, should we go out to our first date then?"
    "Sayori giggles as she says that."
    scene black with wipeleft_scene
    "Honestly, I'm really excited though."
    "I may never understand her, but I love being around her."
    "By the time we get to see the rest of festival, it's already pretty late."
    "We feel bad about leaving Monika to clean up by herself."
    "But she insists it's fine."
    "Before I know it, the day is already over."
    "We hear that they're gonna be launching fireworks so we stick around to watch them."
    scene bg firework with wipeleft
    "Sayori and I find a great spot by ourselves to watch them go off."
    scene bg fireworks
    play music firework
    with Dissolve(1)
    "As the fireworks explode in the night sky, I see something out of the corner of my eye."
    show sayori 1q at rsface
    "Sayori is smiling"
    "Not a fake smile, but a true, earnest, joyful, smile."
    show sayori at thide2
    hide sayori
    "She wraps her arms around me in a tight embrace."
    "I hold her close as the night sky is illuminated."
    "..."
    "..."
    "..."
    stop music fadeout 1
    scene nhouse with dissolve_scene_full
    "After the fireworks finish, I walk her home, as always."
    show sayori 5a at t11
    "She stops me right outside her house."
    mc "What is it?"
    s 5 "I just wanted to thank you."
    s "Not just for waking me up today."
    s "Or for spending time with me."
    s "But for everything."
    s 3y "It may have only been for a moment earlier."
    s  "But it felt like the rainclouds went away."
    mc "I'm glad."
    mc "It's gonna be a slow process."
    mc "But I plan to chase them away permanently."
    show sayori 4s
    "Sayori blushes once more."
    s "Well you're off to a great start."
    s "I can't wait to see you again tomorrow."
    $ _window_hide(trans=False)
    show sayori at uface
    scene black with dissolve
    pause .5
    show nhouse
    show sayori 1y at i11 
    with dissolve
    "."
    ".."
    "..."
    show sayori 1s at thide
    pause .25
    hide sayori
    "Sayori kisses me on the cheek, then walk away."
    "I swear I can see her still smiling."
    "It may take a while."
    "But she's gonna get better."
    return
    
label ch5_end_natsuki:
    with wipeleft_scene
    "Natsuki inspects the cupcakes and touches a couple of things that got damaged on the way."
    show yuri 1a at t44
    show natsuki 1a at t43
    show monika 1a at t42
    show sayori 1a at t41 
    "I feel nervous in front of everyone."
    "But if the other four can do it, then so can I."
    "I get up and give my poem before anyone shows up."
    "..."
    show yuri 3d at t44
    show natsuki 4z at t43
    show monika 2k at t42
    show sayori 4r at t41
    with wipeleft
    "The entire club applauds."
    "But, it feels like a hollow victory."
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "Still, I'm just glad to have it be over with."
    show natsuki 3j at l11
    "Immediately after me, is Natsuki."
    "She gets up and she seems fairly calm."
    "There's not too many people here yet."
    "I guess something about the crowd is still getting to her a little bit though."
    "She seems to search around in the crowd for support."
    show natsuki 3k at h11
    "She makes eye contact with me."
    show natsuki 2l
    "She smiles and goes right into it."
    show natsuki 2q 
    "Natsuki start reading her poem."
    "If cuteness had a sound, I'm sure everyone in the room was hearing it."
    "Every word is bustling with energy and happiness."
    show natsuki 4t at rhide
    pause .25
    hide natsuki
    "The crowd gives a fairly warm reception and applauds for her."
    "Natsuki walks over to me, with her usual confidence."
    show natsuki 2a at t11
    n "Since we're both already done."
    n 4l "Do you want to go check out the rest of the festival?."
    mc "I don't see why not."
    hide natsuki
    scene corridor
    with wipeleft_scene
    show natsuki 4a at t11
    "Natsuki and I manage to slip away from the literature club."
    "The entire day is blast."
    "She seems so excited by everything and it's adorable."
    "It may just be me, but she feels slightly different than usual."
    "In a good way, though."
    "Like she's not trying to hide anything."
    show natsuki 1p at h11
    "All of a sudden though, she jumps behind me in a panic."
    mc "Is everything okay?"
    n "Oh no, why is he here?"
    n 1v  "Quick, we've got to hide."
    n"I don't want him to see you."
    show natsuki at lhide
    hide natsuki
    "Natsuki's acting weird and runs away."
    "I have no idea who she was talking about."
    show man at t11
    "Suddenly a fairly large man comes up to me."
    c "Excuse me, but you wouldn't have happened to see my daughter?"
    mc "I doubt it. Who's your daughter?"
    c "Her name's Natsuki."
    c "I could have sworn I saw you with her earlier."
    "Oh so Natsuki must be hiding from her dad."
    "I can't fathom why though..."
    mc "Oh yeah, I did see her earlier."
    c "Oh yeah?"
    c "Where?"
    "Is it just me or does this guy seem a little aggressive?"
    mc "Well she was just around here a couple minutes ago."
    mc "But I don't really know where she ran off to."
    c "You'd do best to stay away from her."
    c "I wouldn't want her getting someone tied up in this."
    mc "I don't really know what you're talking about."
    mc "We're just in the literature club together."
    c "Hmph."
    c "Well you better keep that in mind."
    c "If you see her, tell her she needs to come see me."
    c "I told her that she was going to be spending today with me."
    "What is this guy's problem?"
    mc "Uh sure, I'll make sure to tell her that."
    mc "But I don't know if I'll see her again."
    mc "There's a lot of people around today."
    mc "You could try checking the literature club's performances to see if she went back there."
    c "Whatever."
    show man at thide
    hide man
    "The man stomps away a few minutes later."
    "I breathe a sigh of relief and start to walk away."
    "I feel someone pull me into a little nook."
    "I see that it's Natsuki."
    "She must have been hiding right here through all of that."
    show natsuki 5m at t11 
    n "I'm sorry about all that."
    n "I hate him."
    n "He's always telling me what to do."
    n 5u "I wish I could just run away."
    mc "Things are that bad, huh?"
    n 5n "I'm sorry, I really didn't mean to drag you into all of this."
    n 2u "Forget any of it happened, please."
    show natsuki at thide
    hide natsuki
    with wipeleft
    "I feel so bad for her."
    "Things must really not be good at home."
    "No wonder she spends so much time at the club."
    "I wish there was something I could do."
    mc "Hey Natsuki"
    show natsuki 2k at t11
    n "Huh...?"
    mc "Anytime you want a break."
    mc "You know, from home."
    mc "Well, you're more than welcome to spend as much time at my place as you want."
    show natsuki 1p at h11
    "Natsuki blushes"
    n 1h "Do you really mean that?"
    n "Are you really going to take that much responsibility of me?"
    mc "Yeah"
    n 1q "What about after we graduate?"
    n "How long are you willing to put up with me?"
    mc "Well..."
    mc "I guess forever if that's what it takes."
    n 1h "Do you really mean that?"
    mc "Yes" 
    $ _window_hide(trans=False)
    show natsuki 1r at h11
    pause .5
    show natsuki 1i
    pause .5
    show natsuki at uface
    scene black with Dissolve(0.25)
    "She grabs onto me and hugs me tight,"
    n "Will you promise me you won't make this weird?"
    "What is she talking about?"
    scene corridor
    show natsuki 12c at face
    with dissolve
    pause .1
    show natsuki at t11
    n "Please listen to this carefully"
    n "I'm not going to repeat this."
    n 12b "..."
    n "I-"
    n "I-"
    n 12a "I may kinda, sorta, like you..."
    n "T-There I said it."
    mc "..."
    mc "Well, I kinda, sorta, like you too."
    show natsuki 12g at h11
    "A tears running down Natsuki cheeks"
    n "Really?" 
    n "I-I guess that makes us a couple then."
    $ _window_hide(trans=False)
    show natsuki 12h at t11 with dissolve_cg
    n 12i "So you better mean it when you say you're gonna take care of me."
    "I nod my head."
    show natsuki 12h at uface
    scene black with Dissolve(0.25)
    "Natsuki hugs me back."
    "I'm not entirely sure what all I just signed up for."
    "But I'm happy, nonetheless."
    "By the time we had finished talking, the festival was already over."
    "I felt bad about Natsuki missing out on the festival, but she said she liked how she spent her time more."
    "."
    ".."
    "..."
    return
label ch5_end_yuri:
    show yuri 1b at t11
    "Yuri show up and talk to me."
    y "Thanks for bringing me the banner and finishes it up."
    show yuri at thide
    hide yuri
    "The entire festival starts to pick up as a lot of guests start showing up."
    "I feel nervous in front of everyone."
    "But if the other four can do it, then so can I."
    "I get up and give my poem before anyone shows up."
    "..."
    show yuri 3d at t44
    show natsuki 4z at t43
    show monika 2k at t42
    show sayori 4r at t41
    with wipeleft
    "The entire club applauds."
    "But, it feels like a hollow victory."
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "Still, I'm just glad to have it be over with."
    show natsuki 3d at t11
    "Natsuki gives her performance while the crowd is still somewhat thin."
    "It goes over fairly well, although she is pretty clearly just happy to be done with it all."
    "She mingles around for a bit until she slips away to enjoy the rest of the festival."
    show natsuki at rhide
    hide natsuki
    show yuri 4b at l11
    "After her is Yuri."
    "Yuri seems incredibly uneasy as she gets up to perform her poem."
    show yuri 1v
    "She looks around."
    show yuri 1f
    "We make eye contact and I flash her a smile."
    show yuri 3a
    "..."
    show yuri 2m
    "She takes a deep breath and then starts reading her poem."
    show yuri 2h
    "Her delivery is impeccable and leaves everyone absolutely silent for a moment."
    "I immediately feel bad because this keeps happening."
    "But Yuri is always so shy and reserved, but her deliveries are so confident and full of power."
    show yuri 2j
    "Thankfully this time, everyone gives a large thunderous applause."
    show yuri 4c at h11
    pause .25
    show yuri at lhide
    hide yuri
    "She blushes and hurries away."
    "i start after yuri."
    scene corridor 
    show yuri 4c at t11
    with wipeleft_scene
    "I manage to catch up to her a few minutes later."
    mc "Yuri, that was amazing."
    y 4a "Really?"
    mc "Every time you say one of your poems, everyone is just awestruck."
    mc "You're just too good."
    y 3a "Well, I guess if you look at it that way."
    y 3b "Then I guess it really is a good thing."
    "She smiles brightly at me."
    y 3j "I probably wouldn't have been able to do it if you weren't encouraging me."
    "This time, it's me that smiles."
    y 3v "Hey..."
    y "W-would you want to go enjoy the festival with me?"
    "I'm at a loss for words."
    "After everything that happened yesterday, and now this?"
    show yuri at h11
    mc "I'd love to."
    show yuri 3c
    "Yuri smiles brighter than I've ever seen."
    y 3d "Let's go then."
    mc "Shouldn't we let Monika know first?"
    y "I'm sure she'll figure it out."
    scene black with Dissolve(.25)
    "Next thing I know Yuri is pulling me away."
    "We go from stall to stall, viewing the various things the school's clubs have put together."
    "Yuri seems pretty uncomfortable though."
    "She must not be used to being around this many people."
    "Not to mention the feeling like every pair of eyes on us."
    scene corridor 
    show yuri 1u at t11
    with dissolve_cg
    mc "Hey Yuri"
    y 2f "Yeah?"
    mc "Did you bring your copy of the book today?"
    y "I did, yes."
    mc "Would you want to get away from this for a little bit and go read together?"
    y 3d "YES!"
    y 1q "I mean, only if you want to that is."
    mc "Sure let's go."
    scene class
    show yuri 1a at t11
    with wipeleft_scene
    "We find a nice secluded spot away from everyone."
    "Yuri immediately seems to be more calm and relaxed now."
    scene y_cg1_base with Dissolve(.5)
    "We open up the book and begin reading together."
    "Unlike before, there's no awkwardness."
    "Sure the entire thing still feels romantic."
    "But it also feels natural too now."
    scene ycg2 with Dissolve(1)
    "Before long, I notice that Yuri's actually fallen asleep."
    "Am I that slow of a reader compared to her?"
    "Or did the festival take that much out of her?"
    "Then I suddenly see something on her arms."
    scene class 
    show yuri 3k at t11
    with dissolve_cg
    "It doesn't look like much, but I roll up her sleeves a bit to see."
    show yuri cuts2 with Dissolve(.25)
    "She stirs a little bit."
    "The cuts don't seem to be fresh."
    "But they all appear to self-inflicted."
    show yuri cuts3 with Dissolve(.25)
    "She lifts her head, blushing a little bit."
    $ _window_hide(trans=False)
    show yuri cuts at h11
    pause .5
    show yuri 1n
    "Suddenly she looks at her rolled up sleeves and panics."
    y 1p "It's-it's-it's"
    y "It's not what it looks like!"
    mc "Yuri"
    y 1o "It's"
    mc "Yuri"
    show yuri 4b
    "She falls silent."
    mc "How long?"
    y 1v "I've been doing it for while."
    y 1w "But I promise I haven't done it for a while."
    y  "To be exact, I haven't done it since..."
    y 3v "Well...since you joined the club..."
    mc "So as long as I'm around, you don't do it."
    show yuri at nods
    "Yuri nods."
    y 3u "When I'm around you, I feel a rush unlike anything else."
    y "It all had felt good."
    y "But it doesn't compare to how I feel when I'm with you."
    y 2t "When I'm with you...everything just feels so pure"
    y "So natural."
    y "So wonderful..." 
    y 3v "This isn't how I had planned on telling you"
    y 3w "But I've fallen in love with you."
    y 3t "Will you go out with me?"
    show yuri at thide
    hide yuri
    "As soon as she says that, she pulls her book up to cover her face."
    mc "Yuri"
    mc "I'd love to go out with you."
    show yuri 2u at t11
    "She lowers her book from her face'"
    y 2v "You would?"
    mc "On one condition"
    y 2t "What's that?"
    mc "I don't want you doing this to yourself ever again."
    mc "I hate seeing you hurt."
    mc "I wouldn't be able to stand being around you when you hurt yourself."
    mc "Promise me you won't ever do it again."
    y 3s "I promise."
    y "Besides, if I have you."
    y 4e "I won't ever need anymore of a rush."
    "She smiles and blushes."
    show yuri at uface
    "Then, she hugs me."
    show yuri 1c with Dissolve(.5)
    "It must be tough for her to be this straight forward."
    scene classet with dissolve_cg
    "But I'm glad that things seem to finally have worked out."
    "We both embrace each other as the sun sets on the festival."
    "..."
    "..."
    "..."
    return
label ch5_end_lonely:
    mc "No, it's not like that you."
    mc "I trust you really."
    mc "I just can't help but worry about Sayori sometimes."
    m 1e "If you say so."
    show monika at thide
    hide monika
    with wipeleft
    "Monika continues setting everything up."
    "I check my phone and suddenly see a message from Sayori."
    "She apologizes for waking up late and says that she'll be at school soon."
    "I feel oddly relieved."
    "I apologize about not waiting for her and tell her to hurry up."
    "She asks if I've talked to Monika yet."
    "I don't know what to tell her, so I just wait for her to get here and see for herself."
    show natsuki 4a at t21
    show yuri 1a at t22
    with wipeleft_scene
    "Meanwhile, Yuri and Natsuki show up."
    hide yuri
    hide natsuki
    with wipeleft
    "."
    ".."
    "..."
    show yuri 1a at t11
    "Yuri puts the final touches on the banner."
    mc "Hey Yuri"
    show yuri 1p at hop
    "Yuri jumps so hard that she almost messes up the banner." 
    y 3n "Y-Yeah?"
    mc "About what you mentioned about Monika."
    y 3f "A-...Ah..."
    y 1q "Forget about it."
    y "It was out of line for me to make such baseless assumptions."
    y "I'd hate to be someone who started a rumor."
    mc "I was just going to ask if you know anything I could for her."
    mc "Sayori and I visited her last night."
    mc "Monika definitely seems to be off."
    y 1l "Well..."
    y 2f "If it was me..."
    y "I guess it would mean a lot if you stayed for her performance today."
    y "She's going last today."
    y "And it may not hurt to help her clean up."
    y "But that's just what I would do..."
    y 3t "I'm sorry I can't be of more help."
    mc "No"
    mc "That's really helpful."
    mc "Thanks Yuri."
    y 3f "If you don't mind me asking."
    y "Why the sudden interest in our President here?"
    "I honestly don't have a proper answer to Yuri's question."
    "Sure, I kind of knew Monika before all of this."
    "But never intimately."
    mc "Well I never knew her too well before."
    mc "And I guess I've decided that I want to now."
    y 1b "Huhu"
    y "If you say so."
    show yuri at thide
    hide yuri
    "Yuri continues working on the banner with a smile."
    show sayori 4p at t11
    with wipeleft_scene
    "Sayori shows up not too much later as the festival is about to start."
    s "Sorry, i'm late!"
    mc "It's okay."
    hide sayori
    with wipeleft
    "We barely get everything together and ready by the time people start showing up."
    show yuri 1a at t44
    show natsuki 1a at t43
    show monika 1a at t42
    show sayori 1a at t41 
    "I feel nervous in front of everyone."
    "But if the other four can do it, then so can I."
    "I get up and give my poem before anyone shows up."
    "..."
    show yuri 3d at t44
    show natsuki 4z at t43
    show monika 2k at t42
    show sayori 4r at t41
    with wipeleft
    "The entire club applauds."
    "But, it feels like a hollow victory."
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "Still, I'm just glad to have it be over with."
    show natsuki 3d at t11
    "Natsuki gives her performance while the crowd is still somewhat thin."
    "It goes over fairly well, although she is pretty clearly just happy to be done with it all."
    "She mingles around for a bit until she slips away to enjoy the rest of the festival."
    show natsuki at rhide
    hide natsuki
    show yuri 4b at l11
    "After her is Yuri."
    "Just like the other day, Yuri has a little bit of a weak start because of her nerves."
    show yuri 3f
    "But once she gets into her groove she performs incredibly well."
    show yuri 3b 
    "The crowd gives her quite the welcoming applause."
    "She ends up running off because of all the attention."
    show yuri at thide
    hide yuri
    "After that is Sayori."
    show sayori 1a at l11
    "Sayori gets up and gives a great performance."
    show sayori 2r
    "It exudes happiness and enthusiasm."
    show sayori 4q
    "After she finishes up, everyone seems to be in a better mood."
    show sayori at rhide
    hide sayori
    "Sayori comes over to me."
    show sayori 1g at t11
    s "I talked to Monika earlier."
    mc "And?"
    s "I hate to say this"
    s 1h "But I think you should spend some more time with her."
    s "You seem to brighten her mood."
    mc "Really?"
    s 3l "I mean..."
    s "I'm sure you'll be able to connect with her."
    s "You both just kinda seem lonely."
    s "And they say misery loves company right?"
    show sayori at lhide
    hide sayori
    "Sayori ends up leaving."
    "The only two club members left are Monika and I."
    "I go up to her."
    show monika 1q at t11
    mc "Hey Monika."
    m 1d "Yeah?"
    mc "I was curious if I could see more of your poems."
    mc "I think they're really cool."
    mc "Even if I don't always get it."
    show monika 1q at h11
    "Monika seems unenthused."
    m 1r "You can drop the act now."
    mc "Huh?"
    m 1i "Maybe if you had tried a little harder, you might've connected with someone."
    m "But... you didn't at all, did you?"
    m 1r "Why did you even join this club?"
    m "Did you just see pretty girls and think you'd end up with dates without trying?"
    mc "I...ummm..."
    m 2i "Save it."
    m "Do me a favor and just go ahead and leave."
    show monika at thide
    hide monika
    m "I'd rather clean up all the messes you make by myself."
    "I remain quiet for a couple seconds."
    "She's completely right."
    "I never made any kind of effort with anyone."
    "There's so much I could've done but didn't."
    "I guess that's what they call hindsight."
    "I had one chance and I blew it."
    "Now I'll never get closer to any of these girls."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never."
label ch5_end_harem:
    "I decide to go check up on her."
    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "That really is something that a boyfriend would do, isn't it?"
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    scene sayori_bedroom with wipeleft
    "As the door opens, I see Sayori still in bed."
    "She must still be sound asleep."
    "I think back to a couple days ago."
    "Was she watching me sleep just like this?"
    "She seems so peaceful."
    "A few seconds pass."
    "She opens her eyes."
    show sayori 1bm at h11
    s "Uwaa!"
    show sayori at thide
    with vpunch
    hide sayori
    "Sayori jumps awake and then throws her blanket over her head."
    mc "You dummy."
    mc "You overslept."
    s "So you came to wake me up?"
    mc "Well yeah.."

    mc "Are you coming?"
    "I do everything I can to help Sayori get ready for the day so that way we can both make it on time."
    scene bg house with wipeleft
    "We go back to my house."
    show yuri 1a at t33
    show natsuki 5i at t32
    show sayori 1a at t31
    y "Uh, good morning!"
    show sayori 1n at h31
    with vpunch
    "Sayori and I both jump a little."
    "Natsuki and Yuri must have been waiting here for a while."
    n 5q "Took you two long enough."
    mc "What are you two doing here?"
    n 2h "Well we figured that since you had so much left here."
    n "That we could help and bring everything to school."
    n "We had tried texting you, but we didn't get a response."
    show natsuki 2s
    "I check my phone to see dozens of messages from both Yuri and Natsuki."
    mc "I'm sorry."
    mc "Somebody decided to over sleep again."
    y 1b "That is very thoughtful of you."
    mc "Well..."
    mc "I'd do the exact same for either of you."
    show natsuki at h32
    show yuri at h33
    "They both seem to squirm a little when I say this."
    n 4t "We might have to hold you to that some time."
    "I swear I see Natsuki wink at me."
    scene residential
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "We all work together to make sure everything gets to school."
    "It feels a little weird, but everyone seems to be getting along together in a group like this."
    "Funnily enough, I probably feel the same way as Natsuki about the event."
    "I'm more excited for it to be over so I can spend time with everyone at the festival."
    "But knowing Monika, I'm sure the event will be great, too."
    scene club with wipeleft_scene
    show monika 5 zorder 2 at t11
    play music t2
    m "[player]!"
    m "You all came together."
    "I suddenly remember our conversation from yesterday and feel awful."
    show monika at thide
    hide monika
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones we prepared that has all the poems we're performing."
    "In the end, I found a random poem online that I thought Yuri would like, and submitted it."
    "So, that's the one I'll be performing."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh hey this turned out really good."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    "For a minute, I swear I see something happen with Sayori's poem, but it's the same one she practiced."
    show monika 2d at t11
    m "What's wrong?"
    mc "Ah, nothing..."
    m 2f "Sigh"
    m "I guess you'll just never trust me after all..."
    m "Not that I blame you."
    show monika at thide
    hide monika
    with wipeleft_scene
    "Natsuki inspects and cupcakes and touches a couple of things that got damaged on the way."
    "Yuri puts some finishing touches on the banner."
    "Sayori seems to be checking through the pamphlets that she helped design."
    "I decide to go and talk to Monika for a minute."
    show monika 1d at t11
    m "Hey, what's up?"
    mc "I wanted to apologize for not including you."
    mc "Again."
    m 2k "Don't worry about it."
    mc "Well, why don't you give me your number so that way it doesn't happen again?"
    show monika 1n at h11
    "I hear my heart thump in my chest as Monika stares at me in surprise."
    "Doki Doki."
    show monika 3k at t11
    "After a couple seconds I see Monika smile brightly."
    m "Sure, why not?"
    "Monika and I exchange numbers quickly."
    show monika at thide
    hide monika
    "She immediately sends me a message."
    "I can't believe this is all actually working out."

    "The entire festival starts to pick up as a lot of guests start showing up."
    show yuri 1a at t44
    show natsuki 1a at t43
    show monika 1a at t42
    show sayori 1a at t41 
    "I feel nervous in front of everyone."
    "But if the other four can do it, then so can I."
    "I get up and give my poem before anyone shows up."
    "..."
    show yuri 3d at t44
    show natsuki 4z at t43
    show monika 2k at t42
    show sayori 4r at t41
    with wipeleft
    "The entire club applauds."
    "But, it feels like a hollow victory."
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft_scene
    "Still, I'm just glad to have it be over with."
    show natsuki 3j at t11
    "Immediately after me, is Natsuki."
    "She gets up and she seems fairly calm."
    "There's not too many people here yet."
    "I guess something about the crowd is still getting to her a little bit though."
    "She seems to search around in the crowd for support."
    show natsuki 3k at h11
    "She makes eye contact with me."
    show natsuki 2l
    "She smiles and goes right into it."
    show natsuki 2q 
    "Natsuki start reading her poem."
    "If cuteness had a sound, I'm sure everyone in the room was hearing it."
    "Every word is bustling with energy and happiness."
    show natsuki 4t at rhide
    pause .25
    hide natsuki
    "The crowd gives a fairly warm reception and applauds for her."
    "Natsuki walks over to me, with her usual confidence."
    show natsuki 2a at t11
    n "Since we're both already done."
    n 4l "Do you want to go check out the rest of the festival?."
    mc "I don't see why not."
    hide natsuki
    scene corridor
    with wipeleft_scene
    show natsuki 4a at t11
    "Natsuki and I manage to slip away from the literature club."
    "The entire day is a blast."
    "She seems so excited by everything and it's adorable."
    "It may just be me, but she feels slightly different than usual."
    "In a good way, though."
    "Like she's not trying to hide anything."
    show natsuki 1p at h11
    "All of a sudden though, she jumps behind me in a panic."
    mc "Is everything okay?"
    n "Oh no, why is he here?"
    n 1v  "Quick, we've got to hide."
    n"I don't want him to see you."
    show natsuki at lhide
    hide natsuki
    "Natsuki's acting weird and runs away."
    "I have no idea who she was talking about."
    show man at t11
    "Suddenly a fairly large man comes up to me."
    c "Excuse me, but you wouldn't have happened to see my daughter?"
    mc "I doubt it. Who's your daughter?"
    c "Her name's Natsuki."
    c "I could have sworn I saw you with her earlier."
    "Oh so Natsuki must be hiding from her dad."
    "I can't fathom why though..."
    mc "Oh yeah, I did see her earlier."
    c "Oh yeah?"
    c "Where?"
    "Is it just me or does this guy seem a little aggressive?"
    mc "Well she was just around here a couple minutes ago."
    mc "But I don't really know where she ran off to."
    c "You'd do best to stay away from her."
    c "I wouldn't want her getting someone tied up in this."
    mc "I don't really know what you're talking about."
    mc "We're just in the literature club together."
    c "Hmph."
    c "Well you better keep that in mind."
    c "If you see her, tell her she needs to come see me."
    c "I told her that she was going to be spending today with me."
    "What is this guy's problem?"
    mc "Uh sure, I'll make sure to tell her that."
    mc "But I don't know if I'll see her again."
    mc "There's a lot of people around today."
    mc "You could try checking the literature club's performances to see if she went back there."
    c "Whatever."
    show man at thide
    hide man
    "The man stomps away a few minutes later."
    "I breathe a sigh of relief and start to walk away."
    "I feel someone pull me into a little nook."
    "I see that it's Natsuki."
    "She must have been hiding right here through all of that."
    show natsuki 5m at t11 
    n "I'm sorry about all that."
    n "I hate him."
    n "He's always telling me what to do."
    n 5u "I wish I could just run away."
    mc "Things are that bad, huh?"
    n 5n "I'm sorry, I really didn't mean to drag you into all of this."
    n 2u "Forget any of it happened, please."
    show natsuki at thide
    hide natsuki
    with wipeleft
    "I feel so bad for her."
    "Things must really not be good at home."
    "No wonder she spends so much time at the club."
    "I wish there was something I could do."
    mc "Hey Natsuki"
    show natsuki 2k at t11
    n "Huh...?"
    mc "Anytime you want a break."
    mc "You know, from home."
    mc "Well, you're more than welcome to spend as much time at my place as you want."
    show natsuki 1p at h11
    "Natsuki blushes"
    n 1h "Do you really mean that?"
    n "Are you really going to take that much responsibility of me?"
    mc "Yeah"
    n 1q "What about after we graduate?"
    n "How long are you willing to put up with me?"
    mc "Well..."
    mc "I guess forever if that's what it takes."
    n 1h "Do you really mean that?"
    mc "Yes" 
    $ _window_hide(trans=False)
    show natsuki 1r at h11
    pause .5
    show natsuki 1i
    pause .5
    show natsuki at uface
    scene black with Dissolve(0.25)
    "She grabs onto me and hugs me tight,"
    n "Will you promise me you won't make this weird?"
    "What is she talking about?"
    scene corridor
    show natsuki 12c at face
    with dissolve
    pause .1
    show natsuki at t11
    n "Please listen to this carefully"
    n "I'm not going to repeat this."
    n 12b "..."
    n "I-"
    n "I-"
    n 12a "I may kinda, sorta, like you..."
    n "T-There I said it."
    mc "..."
    mc "Well, I kinda, sorta, like you too."
    show natsuki 12g at h11
    "A tears running down Natsuki cheeks"
    n "Really?" 
    n "I-I guess that makes a couple then."
    $ _window_hide(trans=False)
    show natsuki 12h at t11 with dissolve_cg
    n 12i "So you better mean it when you say you're gonna take care of me."
    "I nod my head."
    show natsuki 12h at uface
    scene black with Dissolve(0.25)
    "Natsuki hugs me back."
    "I'm not entirely sure what all I just signed up for."
    "But I'm happy, nonetheless."

    "After Natsuki calms down a little, she decides to go and find her dad before he gets any angrier."
    "I offer to go with her but she declines."
    scene bg club_day
    show yuri 1h at t11
    with dissolve_scene_full
    "In the meantime, I decide to head back to the club room and I find Yuri along the way."
    "I manage to catch the very end of Yuri delivering her poem and catch up to her a few moments later."
    show yuri 1b at t11
    with wipeleft_scene
    mc "Yuri, that was amazing."
    y 4a "Really?"
    mc "Every time you say one of your poems, everyone is just awestruck."
    mc "You're just too good."
    y 3a "Well, I guess if you look at it that way."
    y 3b "Then I guess it really is a good thing."
    "She smiles brightly at me."
    y 3j "I probably wouldn't have been able to do it if you weren't encouraging me."
    "This time, it's me that smiles."
    y 3v "Hey..."
    y "W-would you want to go enjoy the festival with me?"
    "I'm at a loss for words."
    "After everything that happened yesterday, and now this?"
    show yuri at h11
    mc "I'd love to."
    show yuri 3c
    "Yuri smiles brighter than I've ever seen."
    y 3d "Let's go then."
    mc "Shouldn't we let Monika know first?"
    y "I'm sure she'll figure it out."
    scene black with Dissolve(.25)
    "Next thing I know Yuri is pulling me away."
    "We go from stall to stall, viewing the various things the school's clubs have put together."
    "Yuri seems pretty uncomfortable though."
    "She must not be used to being around this many people."
    "Not to mention the feeling like every pair of eyes on us."
    scene bg corridor 
    show yuri 1u at t11
    with dissolve_cg
    mc "Hey Yuri"
    y 2f "Yeah?"
    mc "Did you bring your copy of the book today?"
    y "I did, yes."
    mc "Would you want to get away from this for a little bit and go read together?"
    y 3d "YES!"
    y 1q "I mean, only if you want to that is."
    mc "Sure let's go."
    scene class
    show yuri 1a at t11
    with wipeleft_scene
    "We find a nice secluded spot away from everyone."
    "Yuri immediately seems to be more calm and relaxed now."
    scene y_cg1_base with Dissolve(.5)
    "We open up the book and begin reading together."
    "Unlike before, there's no awkwardness."
    "Sure the entire thing still feels romantic."
    "But it also feels natural too now."
    scene ycg2 with Dissolve(1)
    "Before long, I notice that Yuri's actually fallen asleep."
    "Am I that slow of a reader compared to her?"
    "Or did the festival take that much out of her?"
    "Then I suddenly see something on her arms."
    scene class 
    show yuri 3k at t11
    with dissolve_cg
    "It doesn't look like much, but I roll up her sleeves a bit to see."
    show yuri cuts2 with Dissolve(.25)
    "She stirs a little bit."
    "The cuts don't seem to be fresh."
    "But they all appear to self-inflicted."
    show yuri cuts3 with Dissolve(.25)
    "She lifts her head, blushing a little bit."
    $ _window_hide(trans=False)
    show yuri cuts at h11
    pause .5
    show yuri 1n
    "Suddenly she looks at her rolled up sleeves and panics."
    y 1p "It's-it's-it's"
    y "It's not what it looks like!"
    mc "Yuri"
    y 1o "It's"
    mc "Yuri"
    show yuri 4b
    "She falls silent."
    mc "How long?"
    y 1v "I've been doing it for while."
    y 1w "But I promise I haven't done it for a while."
    y  "To be exact, I haven't done it since..."
    y 3v "Well...since you joined the club..."
    mc "So as long as I'm around, you don't do it."
    show yuri at nods
    "Yuri nods."
    y 3u "When I'm around you, I feel a rush unlike anything else."
    y "It all had felt good."
    y "But it doesn't compare to how I feel when I'm with you."
    y 2t "When I'm with you...everything just feels so pure"
    y "So natural."
    y "So wonderful..." 
    y 3v "This isn't how I had planned on telling you"
    y 3w "But I've fallen in love with you."
    y 3t "Will you go out with me?"
    show yuri at thide
    hide yuri
    "As soon as she says that, she pulls her book up to cover her face."
    mc "Yuri"
    mc "I definitely like you too."
    "As the words leave my mouth, I think back to Natsuki and Sayori."
    "I must show it on my face because Yuri immediately reacts."
    show yuri 2v at t11
    y "It's okay."
    y "I know I'm not the only one."
    y "But I think"
    y 2w "I can manage with it in time."
    y "As long as you really do you like me, that is."
    mc "There's another problem."
    y 2t "What's that?"
    mc "I don't want you doing this to yourself ever again."
    mc "I hate seeing you hurt."
    mc "I wouldn't be able to stand being around you when you hurt yourself."
    mc "Promise me you won't ever do it again."
    y 3s "I promise."
    y "Besides, if I have you."
    y 4e "I won't ever need anymore of a rush."
    "She smiles and blushes."
    "It must be tough for her to be this straightforward."
    "But I'm glad that things seem to finally have worked out."
    scene bg club_day 
    show sayori 3b at t11
    with wipeleft_scene
    "We end up deciding to go back to the club room and see Sayori's poem."
    "Sayori sees us and she clearly gets filled with confidence."
    show sayori 4r at t11
    "She immediately goes overboard with it."
    show sayori at thide
    hide sayori
    "There's times where I almost can't stop myself from laughing."
    "The crowd seems to be enjoying it as much as she is."
    "By the time she finishes, everyone is either laughing or applauding."
    "It really does amaze me how she can be such a big bright light to everyone."
    "Especially when she herself is having so many problems."
    show sayori 1x at t11
    s "So did I do good?"
    mc "Yeah, that was amazing."
    mc "And to think that you were gonna be late today."
    s 4s "Hehe"
    s "That's why I have you."
    s "To wake me up and get me going"
    "I can't help but blush a little at the compliment."
    "Yuri nudges me forward and motions that it's okay."
    scene bg corridor with wipeleft_scene
    "Sayori and I sneak off without another word."
    "Honestly, I'm really excited though."
    "I may never understand her, but I love being around her."
    "By the time we get to see the rest of festival, it's already pretty late."
    mc "Hey Sayori."
    show sayori 3b at t11 
    s "Yeah?"
    mc "Will you wait for me at the school gate?"
    s "Yeah, why?"
    mc "I kinda have to go take care of something."
    mc "I promised Monika I'd help her clean up."
    s 3b "I could come too."
    mc "I think she wanted to talk to me about a couple of things, alone."
    s 1k "Oh..."
    s 4q "You better get going then."
    s "You don't want to keep either her or I waiting too long."
    "I thank my luck that she's willing to be understanding about all of this."
    scene bg club_day with wipeleft_scene
    "By the time I get into the club room, Monika is already cleaning everything up."
    "I go up to her."
    play music t5
    show monika 1q at t11
    mc "Hey Monika."
    m 1d "Yeah?"
    mc "I was curious if I could see more of your poems."
    mc "I think they're really cool."
    mc "Even if I don't always get it."
    show monika 1s at h11
    "Monika seems genuinely stunned."
    m 3l "Yeah"
    m 1e "Sure"
    m "Let me go see if I brought one with me."
    show monika at thide
    hide monika
    "..."
    show monika 1a at t11
    "She comes back a couple minutes later brandishing a piece of paper."
    m 1e "I don't if you've seen this one before."
    m "But..."
    "Monika hands me the poem."
    call showpoem (poem_m5, music=True)
    "After I finish reading the poem, I can't help but stare."
    m 1r "How long do you think you can keep this up?"
    mc "What do you mean?"
    m 3m "Getting four girls to confess to you and keeping them around."
    mc "It's not quite like I'm trying to."
    mc "And what do you mean four?"
    show monika 1s at h11
    "Monika blushes and is clearly frustrated."
    m "Well that's not how I meant to do that, but oh well."
    m "I guess it doesn't really matter does it?"
    mc "Well, I'll be honest I can't answer to your feelings Monika."
    mc "Because I can't really answer to anyone."
    m 1c "What do you mean?"
    m 2d "Isn't this what you wanted?"
    m "For everyone to be happy?"
    m "To be with everyone."
    mc "Well yeah but..."
    m 2b "Then don't overcomplicate things."
    m "Just go with the flow."
    m "It's just like writing."
    mc "In that case, I guess I'll just have to find the answer in time."
    m 4k "Don't worry, I'll help you as much as I can."
    m "I'm not going to mess with them though."
    m "I still have that promise to keep."
    mc "Thanks I guess."
    m 4b "Don't you have someone waiting for you?"
    mc "Oh right!"
    mc "Thanks"
    scene bg corridor
    show sayori 3a at t11
    with wipeleft_scene
    "I rush off to find Sayori who waited outside for me."
    mc "Thanks for waiting."
    s 3c "Did you say everything you needed to?"
    mc "I think so."
    mc "Hey Sayori"
    s 1b "Hmm?"
    mc "Are you okay with everything going on?"
    mc "I mean like with Monika, Natsuki, and Yuri."
    s 4x "I think as long as you continue to wake me up."
    s "That I can manage."
    hide sayori
    with wipeleft
    "We hear that they're gonna be launching fireworks so we stick around to watch them."
    scene bg firework with wipeleft
    "Sayori and I find a great spot by ourselves to watch them go off."
    scene bg fireworks
    with Dissolve(1)
    "As the fireworks explode in the night sky, I see something out of the corner of my eye."
    show sayori 1q at rsface
    "Sayori is smiling"
    "Not a fake smile, but a true, earnest, joyful, smile."
    show sayori at thide2
    hide sayori
    "She wraps her arms around me in a tight embrace."
    "I hold her close as the night sky is illuminated."
    "..."
    "..."
    "..."
    scene nhouse with dissolve_scene_full
    "After the fireworks finish, I walk her home, as always."
    show sayori 5a at t11
    "She stops me right outside her house."
    mc "What is it?"
    s 5 "I just wanted to thank you."
    s "Not just for waking me up today."
    s "Or for spending time with me."
    s "But for everything."
    s 3y "It may have only been for a moment earlier."
    s  "But it felt like the rainclouds went away."
    mc "I'm glad."
    mc "It's gonna be a slow process."
    mc "But I plan to chase them away permanently."
    show sayori 4s
    "Sayori blushes once more."
    s "Well you're off to a great start."
    s "I can't wait to see you again tomorrow."
    $ _window_hide(trans=False)
    show sayori at uface
    scene black with dissolve
    pause .5
    show nhouse
    show sayori 1y at i11 
    with dissolve
    "."
    ".."
    "..."
    show sayori 1s at thide
    pause .25
    hide sayori
    "Sayori kisses me on the cheek, then walk away."
    "I swear I can see her still smiling."
    "It may take a while."
    "But she's gonna get better."
    return
