init python:
    class RoutePoint:
        def __init__(mrp, srp, npr, yrp):
                self.mrp = mRPoint
                self.srp = sRPoint
                self.nrp = nRPoint
                self.yrp = yRPoint
                self.hrp = hRPoint
                self.lrp = lRPoint
            
default mRPoint = 0
default sRPoint = 0
default nRPoint = 0
default yRPoint = 0
default hRPoint = 0
default lRPoint = 0


label SERoute:
    if mRPoint == 1:
        call SEnd_monika
    if sRPoint == 1:
        call SEnd_sayori
    if nRPoint == 1:
        call SEnd_natsuki
    if yRPoint == 1:
        call SEnd_yuri  
    return
    
label SEnd_natsuki:
    scene bg club_day
    with wipeleft_scene
    play music t3
    show natsuki 4z at h11
    n "Hey! Good job there! i'm looking forward next!"
    return