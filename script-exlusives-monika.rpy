label monika_exclusive_1:
    scene bg club_day
    "I decide to go over and ask Monika about music."
    show monika 1 zorder 1 at t11
    mc "Hey Monika, you said earlier that you had taken up the harp?"
    m 1c "Ah..."
    m 1j "Yes, that's right."
    mc "I didn't know you were talented in that way too."
    mc "Do you play any other instruments or sing?"
    m 3b "Well I used to play the piano for a while."
    m 5a "And I still do for people really important to me."
    mc "Used to?"
    mc "Do you not anymore?"
    m 1l "Well, I thought a small change in my life might make things a bit better."
    m "I'm sorry if it screws anything up."
    mc "Screws anything up?"
    mc "I think it's really cool that you're talented enough to play multiple different instruments."
    mc "Why did you want to change though?"
    mc "Isn't learning a new instrument really tough."
    m 1m "I mean..."
    m "It's amazing what you can do with a keyboard."
    m 3m "But sometimes not touching one can be more cathartic."
    mc "I think I see."
    mc "You mentioned you liked the feeling of it on your fingers."
    mc "Right?"
    m 1k "Yup!"
    mc "But isn't it a little bit painful?"
    mc "I've heard you can get blisters from string instruments."
    m 1l "Well, I think that's part of the fun."
    m "Part of the rush of it all."
    m "Maybe that's the reason why Yuri..."
    mc "Huh?"
    mc "What's that about Yuri?"
    m 1n "Never mind I said anything."
    m 1m "She's a wonderful girl and she'd be lucky if you chose her."
    mc "Ch-ch-chose?"
    mc "Who said anything about me choosing someone?"
    m 2q "Come on."
    m 2r "We both know how this ends."
    m 2i "Boy joins club."
    m "Boy finds out club is full of cute girls."
    m "Boy chooses one and confesses to her."
    m "Girl accepts the guys feelings."
    m 2f "Meanwhile the other girls feel slightly left out."
    m 2m "Maybe drifting away a little."
    mc "That sounds like one of those romance game scenarios."
    m 5a "Well what do you think you're in?"
    mc "Uh..."
    mc "I mean..."
    stop music fadeout 2.0
    mc "I don't even know what a confession sounds like."
    mc "I've never confessed or been confessed to."
    m 1h "You mean you've never had someone turn to you."
    show monika 1h zorder 1
    play music "bgm/monika-end.ogg"
    m "Reach out and tenderly hold your hand."
    "Monika demonstrates by grabbing and holding my hand."
    show monika 1h at face(y=600) with dissolve
    "Our fingers lock as she demonstrates."
    m "Have them turn to you."
    show monika 1m at face(y=600) with dissolve
    m "Look you in the eyes."
    "I stare deep into Monika's eyes."
    "Despite her poem yesterday, her eyes don't appear burnt at all."
    "More of, a brilliant shimmering emerald."
    stop music fadeout 2.0
    m "Then say,"
    m "I love you."
    "There is a long awkward pause before Monika pulls away."
    show monika 1m at hop
    "I'm not certain which one of us is blushing more right now."
    play music t6 
    m "Anyways"
    m 1l "I wouldn't blame you."
    m 2l "A lot of people who never get to experience those things find other ways to do it."
    mc "Like a romance story?"
    m 3a "Exactly."
    m 5a "Just because someone is on a computer screen doesn't mean they're not real."
    m "Or real to you at least."
    mc "Heh"
    mc "You almost sound like you play them."
    m 4a "You could say I have some experience with them."
    m 4l "But never as someone who plays them."
    m "More of..."
    m 4j "A writer."
    mc "That makes sense then."
    m "Hmm?"
    mc "Of why you're in charge of the literature club."
    mc "If you already are a writer."
    mc "Then it would only make sense."
    m 3k "I guess that's one way to look at it."
    m 4k "Speaking of writing, did you remember to write your poem today."
    return

label monika_exclusive_2:
    $ m_exclusivewatched = True
    play music t8
    scene bg club_day
    with wipeleft_scene
    "Rather than just sit and wait, I go ahead and pull out my poem."
    "I start writing and rewriting it, trying to make it perfect."
    "I get so into what I’m doing that I don’t even notice Monika appear in front of me."
    show monika 5b zorder 2 at t11
    m "That’s just making my life that much harder, you know?"
    mc "Ah, I’m sorry."
    mc "I was just trying to make it better."
    m "Sometimes things are better when you just leave them as they should be."
    mc "But then wouldn’t you end up with a black puddle?"
    show monika 1d
    "Monika looks at me a bit confused."
    mc "Didn’t you say earlier about leaving your pen in the same spot for too long making a black puddle of ink?"
    show monika 1a
    "Monika’s smile returns, understanding a bit better."
    m 3b "Oh yeah, I did mention that."
    m 3k "I didn’t think you’d remember it."
    "Monika seems genuinely happy that I seem to have remembered what she had mentioned before."
    show monika 3j
    mc "So I’m just trying to go with the flow and make things a bit better."
    mc "It’s not like they’re perfect."
    mc "I’m not you."
    show monika 1h
    "I say the last under my breath, not expecting her to hear it."
    "Based upon on how her face changes, I think she still did though."
    m 3i "I’m not perfect by any means."
    m 3l "Given the opportunity, I think I’d probably make the biggest mistakes of all."
    mc "Then how you come you aren’t making any now."
    m "It’s because I can’t afford to."
    m 3m "There’s too much pressure to get this right."
    m 3n "It’s all a bit too important."
    m 1p "I’m afraid even one mistake could send everything spiraling."
    mc "Is that why you push yourself to be so perfect?"
    m "Hmm..."
    m 2p "I guess you could put it that way."
    mc "But then, how will you ever get better?"
    show monika 1d
    "Monika looks at me confused again."
    mc "People only get better by making mistakes."
    mc "Take my poem, for example."
    mc "I’m only able to rewrite it and make it better because I’m trying different things, making mistakes, and learning what is good and bad."
    mc "Without those mistakes, I would never be able to tell if I’m getting better or not."    
    m 1r "So you’re saying the mistakes made earlier"
    m 1h "They all had to happen just so I could become a better version of myself?"
    mc "Well I wouldn’t compare you to one of my crappy poems."
    mc "I guess what I’m trying to say is this."
    show monika 1f
    mc "No matter what mistakes you make."
    mc "The important thing is to learn from them, and move on."
    mc "Try to make the mistake right, and learn from it."
    mc "I guess you could call that, My Writing Tip for the Day."
    mc "Thanks for listening."
    show monika 1e
    "With that last part, I laugh a little."
    "Monika seems to be frozen for a bit, like a computer program stalling out on a hard task."
    show monika 1k
    "Then she breaks into a big smile and laughs as well."
    m 1b "Thanks."
    m "I really needed that."
    m 1a "You seem to be able to brighten everyone’s life up a little."
    mc "It must be Sayori rubbing off on me."
    m "Well whatever it is, I think it definitely makes everyone around here like you."
    m 5a "Myself included."
    "I blush at the compliment."
    "Monika seems about to say something else but cuts herself short."
    m 5b "We never seem to have enough time to talk."
    m "It’s such a pity."    
    m 4q "Oh well, it’s time to grab everyone and share our poems."
    return