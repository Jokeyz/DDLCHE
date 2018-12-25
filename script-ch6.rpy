label ch6_main
    "The rest of the year seemed to fly past."
    if ch4_scene == "lonely":
        call ch6_end_lonely
        return
    "Despite the weird beginning, The Literature Club was amazing."
    "I loved spending time with everyone so much."
    "I was amazed at how similar Natsuki and Yuri seemed to be once they got past their differences."
    "It wasn't long until those two ended up being best friends."
    if ch4_scene == "monika":
        call ch6_end_monika
        return
    "The club really has pulled everyone together and made them better."
    "That beind said, I remember Monika coming to tell us sad news."
    m "Okay, everyone!"
    m "Why don’t we all gather together."
    m "I have some important news to share."
    s "Is it about that notice we got the other day?"
    m "Um..."
    m "Ah..."
    m "I don’t know how to say this but..."
    m "The school has decided that we’re too small of a club to sponsor anymore."
    m "They’re breaking us all up."
    Yuri and n "Eh?!?"
    m "I’m sorry, I tried to work things out, but I was afraid I would’ve just made things instead of better."
    "Natsuki: This isn’t fair!"
    n "Now where am I supposed to go after school?"
    y "It is rather unfortunate that we’ll lose our meeting place and time."
    s "But that doesn’t mean it has to end."
    n "What do you mean?"
    s "I mean..."
    s "Just because the school says they won’t sponsor us, doesn’t mean we can’t have a club."
    y "A club that meets outside of the school?"
    y "It wouldn’t be the first time something like that existed."
    n "I’ve heard worse ideas."
    y "Not to mention that if we met outside of the school, we could visit each others’ houses."
    n "Well most of us."
    s "Not to mention that we could all spend more time together as group then."
    s "Yahoo!"
    "Monika smiles."
    m "Leave it to Sayori to turn bad news into good."
    "She said something about the administrators saying the club had to be disbanded."
    "We didn't let that stop us though."
    "We all continued to get together anyways."
    if ch4_scene == "harem":
        call ch6_end_harem
        return
    "Monika never seemed to join us after that though."
    "I don't know if she felt guilty about not being able to protect the club or what."
    "Last thing we heard was that she moved away."
    "Nobody ever got to say goodbye or anything."
    "She just kind of, disappeared one day."
    "It was like she just stopped existing."
    "We didn't let it affect us though."
    "The remaining girls and I became the best of friends."
    "And in a very certain case, more than friends."
    "I remember us going through graduation together."
    "I looked at [ch4_scene] and couldn't wait to see what the future would bring."
    call expression "ch6_end_" + ch4_scene
    return
label ch6_end_monika:
    "Monika never seemed to calm down though."
    "For some reason, she always on edge and worried about everyone else."
    "I think she and Sayori had more in common than either imagined."
    "Thanks to everyone else in the club though, she was able to keep her head throughout whatever was going with her."
    "I couldn't help but smile as she gave her graduation speech as class president."
    "Every minute I got to spend with her was precious, namely because it felt like they were few and far between."
    "She never let it bother her though."
    "She made sure that we both got into top universities together."
    "It seems like lately that she's finally starting to relax a little."
    "She would occasionally mention something about a third eye or about another world."
    "I always assumed it was something from a story she read."
    "But lately, she's been bringing it up less and less."
    "I don't if she's forgetting about it or what, but I'm glad that it doesn't seem to bother her anymore."
    "We still cherish every moment we get together and we've even managed to keep the literature club going too."
    "Sure, we've all graduated and are living our seperate lives, but that doesn't mean we have to stop being friends."
    "Besides, I don't think any of us would have survived that year without each other."
    return
label ch6_end_sayori:
    "It took a while for things with Sayori to get better."
    "Depression isn't a battle won in day."
    "It's a war that can often take a life time."
    "I think it definitely helped that we ended up going to University together."
    "We both performed fairly well in all of our classes."
    "I think it's in part because we've managed to keep everyone together still."
    "Natsuki runs a small little bakery that is doing well now."
    "Yuri has actually become a decently well known author."
    "As for Sayori."
    "I can't remember the last time she brought up {i}the rain clouds{/i}."
    "Every one of her smiles feels just like the one that night of the festival."
    return
label ch6_end_natsuki:
    "It took some arranging but we managed to get her out of her house after we graduated."
    "Then when I left to go to university, she came with me."
    "She found a job at a nearby bakery and started working there immediately."
    "She did really well and brought the bakery a lot of business."
    "It wasn't a surprise to anyone though, she was always incredibly talented."
    "Once I graduated from University, Natsuki had enough money saved up to start her little baked goods stand."
    "The stand exploded in popularity."
    "She ended up having to expand and buy a real store not long after."
    "Yuri still stops by the shop every day to get some baked goods as well as Sayori."
    "Sayori can't ever seem to get enough and Yuri ends up bringing in business with her writing and book discussions."
    "It took years for it to happen, but Natsuki eventually reached out to her family."
    "Things are still strained, but it seems like she's happy still being connected to everyone."
    return
label ch6_end_yuri:
    "I still don't know why Yuri chose to go to university with me."
    "She got into much better places."
    "She always said that the best place was with me, though."
    "She ended up taking a position for the school writing for the paper."
    "She took to it really well and started to get noticed."
    "Pretty soon after we left university, she was writing up a storm."
    "Next thing I know, I'm involved with a very successful author."
    "She still worries me when she's holding sharp objects, but she says not to be concerned."
    "She insists that because of me, she's left all of that behind."
    "We still get the occasional message from Sayori or Natsuki, but these days we just enjoy our quiet life together".
    return
label ch6_end_lonely:
    "The rest of the year seemed to fly past."
    "Things didn't really improve."
    "I guess Monika was right."
    "I was amazed at how similar Natsuki and Yuri seemed to be once they got past their differences."
    "I tried to join them in their trips to the book store but it kinda seemed to be their thing."
    "Sayori started seeming more and more distant as her and Monika bonded."
    "She said that it seemed like I changed since I joined the club, but I never could understand her anyways."
    "I was autmoatically notified by the school that The Literature Club had been disbanded."
    "I guess Monika didn't feel the need to tell me."
    "After that, I kind of fell out with everyone and didn't really hear from them."
    "That's fine though, I had been fine before without them and I could be fine now."
    "Even if it meant that Sayori stopped walking home with me."
    "I ended up going to University with a couple of them, but we never really talked."
    "I guess I went my seperate way and they went theirs."
    return
label ch6_end_harem:
    "We became closer than ever."
    "There were times were it felt stressful because the girls were all vying for my attention."
    "I was always careful to never say the word {i}harem{/i} around them, but it's certainly how it felt."
    "I remember us going through graduation together."
    "They all seemed to look at me and each other like they were up to something."
    "Little did I realize but they had already set things up for when we would get to college."
    "How I ever survived living under one roof with all of them, I'll never be able to say."
    "Natsuki found a job at a nearby bakery and started working there immediately."
    "The little cafe attached to it quickly became our new meeting spot."
    "She did really well and brought the bakery a lot of business."
    "It wasn't a surprise to anyone though, she was always incredibly talented."
    "University was always tough."
    "Yuri and Monika were always helping me study and pushing me to do better."
    "Yuri's writing ended up taking off in University and next thing we know we have a published author living with us."
    "She was always modest about it."
    "Sayori's depression seemed to get better as time went on."
    "I think having everyone around at all times definitely helped."
    "I'm sure the stress from the relationship that we all shared didn't make things better, but I like to think it helped more than it hurt."
    "Monika was a little weird for a while, but she seemed adamant about wanting to be around."
    "I don't know what happened to her to make her so insecure, but she was always worried about being left out."
    "Much like Sayori, she got better with time too."
    "Once I graduated from University, the girls surprised me with something."
    "Apparently they had been saving up money and bought a little house in Okinawa for us all to live in."
    "Natsuki had even bought up a little cupcake stand there."
    "The stand exploded in popularity."
    "She ended up having to expand and buy a real store not long after."
    "We all still live together to this day."
    "Things get weird on occasion when I go on dates with the various girls, but they all seem to be willing to make things work to some degree."
    "Everyone is happy, and I couldn't be happier."
    return
