#Imports needed libraries and files.
import pygame
import command
import logic
from sys import exit
import random

#Intializes the game
pygame.init()

#Sets up resolution
height = 600
width = 800
screen = pygame.display.set_mode((width,height))

gamename = pygame.display.set_caption('Fapland SP')

#Accesses the clock for framedata
clock =  pygame.time.Clock()

#Creates timer events
dierolltimer = pygame.event.custom_type()
dieaddtimer = pygame.event.custom_type()
second = pygame.event.custom_type()
halfsecond = pygame.event.custom_type()

#Registers timers in events
pygame.time.set_timer(dierolltimer, 50)
pygame.time.set_timer(halfsecond, 500)
pygame.time.set_timer(dieaddtimer, 500)
pygame.time.set_timer(second, 1000)

#Text and Font Setup
text_color = (255, 255, 255)

#Pre-made function for drawing horizontally centered text
def draw_text_center(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    img_rect = img.get_rect(center=(x,y))
    screen.blit(img, img_rect)

#Pre-made function for drawing horizontally centered text   
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("mpv/font.ttf", size)

#Main Game Loop
def maingame():
    #Sets game as running
    run = True
    #Checks the general settings in the setting file
    gen_set = logic.general()
    perk_set = logic.perks()
    curse_set = logic.curses()
    invasionchance = gen_set.inv
    modifierchance = gen_set.mod
    pointsperperk = perk_set.ppp
    checkpointon = gen_set.checkp
    cursechance =  curse_set.baseinv
    invaded_check = 0

    #Checks the savedata for checkpoint(Will return 1 if no save)
    room = logic.loadsave()
    preroom = 1
    pausetime = 2
    pause = pausetime
    played = 0
    curse = ""

    #Variables for dice process
    dierollface = 1
    rollingtime = 20
    diefacecolor = 'grey'
    lowestroll=1
    highestroll=6

    #Game States
    canplay = True
    rolling = False
    addroll = False
    loadvideo = False
    reward = False
    choice1 = ""
    choice2 = ""
    skip = False
    activate = False
    cursed = False


    #Rewards
    perklist = perk_set.rewardlist
    curselist = curse_set.curselist
    myperks = []
    mycurses = []
    #Game loop starts here
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            #Button pressing stage
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ROLL.checkForInput(PLAY_MOUSE) and canplay:
                    rolled_num = random.randint(lowestroll,highestroll)
                    rollingtime = 30
                    rolling = True
                    canplay = False
                    diefacecolor = 'grey'
                    preroom = room

                elif CHECK.checkForInput(PLAY_MOUSE) and canplay and (room % 25 == 0 or room >= 100 or room == 1):
                    canplay = False
                    logic.video(room, invasionchance, modifierchance)
                    canplay = True
                elif DELETE.checkForInput(PLAY_MOUSE) and canplay:
                    logic.deletesave()
                    room = 1
                
                if CHOICE1.checkForInput(PLAY_MOUSE) and reward:
                    myperks.append(choice1)
                    activate = True
                elif CHOICE2.checkForInput(PLAY_MOUSE) and reward:
                    myperks.append(choice2)
                    activate = True

                if SKIP.checkForInput(PLAY_MOUSE) and skip:
                    canplay = True
                    skip = False
                    myperks.remove("Skip 1 Video")

                elif PLAY.checkForInput(PLAY_MOUSE) and skip:
                    loadvideo = True
                    skip = False
                
                if CONFIRM.checkForInput(PLAY_MOUSE) and cursed:
                    mycurses.append(curse)
                    activate = True
                
                
                #if SAVEON.checkForInput(PLAY_MOUSE) and canplay and room == 1:
                    #if checkpointon == "ON":
                        #checkpointon = "OFF"
                    #else:
                        #checkpointon = "ON"


            #Rolling the die stage
            if rolling:
                if rollingtime > 0:
                    if event.type == dierolltimer:
                        if dierollface == highestroll:
                            dierollface = lowestroll
                        else:
                            dierollface += 1
                        rollingtime -= 1
                else:
                    dierollface = rolled_num
                    diefacecolor = 'white'
                    if pause > 0:
                        if event.type == halfsecond:
                            pause -= 1
                    else:
                        pause = pausetime
                        rolling = False
                        addroll = True
                            
            #Adding up roll stage
            if addroll:
                if dierollface != 0:
                    if rolled_num > 0:
                        if event.type == dieaddtimer:    
                            dierollface -= 1
                            if room < 100:
                                room += 1
                    if rolled_num < 0:
                        if event.type == dieaddtimer:    
                            dierollface += 1
                            if room > 1:
                                room -= 1
                else:
                    if pause > 0:
                        if event.type == halfsecond:
                            pause -= 1
                    else:
                        pause = pausetime                   
                        addroll = False
                        if "Skip 1 Video" in myperks:
                            skip = True
                        else:
                            loadvideo = True     

            #Play Video stage
            if loadvideo:
                if pause > 0:
                    if event.type == halfsecond:
                        pause -= 1
                else:
                    pause = pausetime
                    if preroom % 25 > room % 25:
                        if checkpointon == "ON":
                            logic.saveit(str(room - room%25))
                            if cursechance + curse_set.invinc_checkp > 100:
                                cursechance = 100
                            else:    
                                cursechance += curse_set.invinc_checkp
                        if invasionchance + gen_set.checkinv > 100:
                            invasionchance = 100
                        else:
                            invasionchance += gen_set.checkinv
                        if modifierchance + gen_set.checkmod > 100:
                            modifierchance = 100
                        else:
                            modifierchance += gen_set.checkmod
                        if room % 25 != 0:
                            logic.video(room - room%25, invasionchance, modifierchance)
                    if room < 100:
                        if room % 25 != 0:
                            print("Playing Round #" + str(room))
                            print("")
                            played += 1
                        if "No Invasions Next Round" in myperks:
                            invaded_check += logic.video(room, 0, modifierchance)
                            myperks.remove("No Invasions Next Round")
                        else:
                            invaded_check += logic.video(room, invasionchance, modifierchance)
                        print("Break")
                        print("")
                        invaded_check += logic.image(invasionchance)
                    loadvideo = False
                    if (cursechance + (curse_set.invinc * invaded_check)) <= 100:
                        cursechance += curse_set.invinc * invaded_check
                    else:
                        cursechance = 100
                    applycurse = random.randint(1, 100 // cursechance)
                    if curse_set.curse == "ON" and applycurse == 1:
                        print("Cursed!")
                        cursed = True
                        curseprimed = False
                    elif played % pointsperperk == 0 and perk_set.perks == "ON":
                        print("Perk!")
                        perkprimed = False
                        reward = True
                    else:
                        canplay = True
                    invaded_check = 0
            

            if cursed:
                if curseprimed == False:
                    curse = random.choice(curselist)
                    curseprimed = True
                    

            #Reward Stage
            if reward:
                if perkprimed == False:
                    choice1 = random.choice(perklist)
                    perklist2 = perklist.copy()
                    perklist2.remove(choice1)
                    choice2 = random.choice(perklist2)
                    perkprimed = True

            if activate == True:
                if "Increase Die Size" in myperks:
                    highestroll = highestroll + perk_set.morerollnum
                    myperks.remove("Increase Die Size")
                if "Decrease Invasion Chance" in myperks:
                    if invasionchance - perk_set.invnum < 0:
                        invasionchance = 0
                    else:    
                        invasionchance = invasionchance - perk_set.invnum
                    myperks.remove("Decrease Invasion Chance")
                if "Decrease Modifier Chance" in myperks:
                    if modifierchance - perk_set.modnum < 0:
                        modifierchance = 0
                    else:
                        modifierchance = modifierchance - perk_set.modnum
                    myperks.remove("Decrease Modifier Chance")
                
                if "Decreased Die's Maximum Size!" in mycurses:
                    highestroll = highestroll - curse_set.diemaxdec
                    mycurses.remove("Decreased Die's Maximum Size!")
                if "Decreased Die's Minimum Size!" in mycurses:
                    lowestroll = lowestroll - curse_set.diemindec
                    mycurses.remove("Decreased Die's Minimum Size!")
                if "Invasion Chance Increased!" in mycurses:
                    if invasionchance + curse_set.invnum > 100:
                        invasionchance = 100
                    else:
                        invasionchance += curse_set.invnum
                    mycurses.remove("Invasion Chance Increased!")
                if "Modifier Chance Increased!" in mycurses:
                    if modifierchance + curse_set.modnum > 100:
                        modifierchance = 100
                    else:
                        modifierchance += curse_set.modnum
                    mycurses.remove("Modifier Chance Increased!")
                if "Moving Back X Rounds!" in mycurses:
                    moveback = random.randint(1, curse_set.movebackmax)
                    if room - moveback < 1:
                        room = 1
                    else:
                        room -= moveback
                if played % pointsperperk == 0 and perk_set.perks == "ON" and cursed:
                    print("Perk!")
                    perkprimed = False
                    reward = True
                else:
                    reward = False
                    canplay = True
                activate = False
                cursed = False

                
        #Black Background
        screen.fill("black")

        #Draws game version and round on the screen
        draw_text("FapLandSP VER.0.2", get_font(16), 'white', 0, 5)
        if room < 100:
            draw_text_center("Round:"+ str(room), get_font(50), 'white', 400, 100)
        else:
            draw_text_center("FapLand Completed!", get_font(40), 'white', 400, 100)
        
        #UI Info
        draw_text("Points: " + str(played), get_font(16), 'white', 0, 30)
        draw_text("Die Size: " + str(lowestroll) + ":" + str(highestroll), get_font(16), 'white', 0, 55)
        #draw_text("Pause: " + str(perk_set.pausenum * myperks.count("Pause Each Video for 10 Seconds")), get_font(16), 'white', 0, 105)
        draw_text("Skips: " + str(myperks.count("Skip 1 Video")), get_font(16), 'white', 0, 80)

        #if (preroom % 25 > room % 25 or room % 25 == 0) or gen_set.checkp == "ON" or room == 1:
        #if :
        draw_text_center("Checkpoint: " + str(room - room%25) +"%", get_font(20), text_color, 400, 480)
        if gen_set.invon == "ON":
            draw_text_center("Invasion Chance: " + str(invasionchance) +"%", get_font(20), text_color, 400, 525)
        if gen_set.modon == "ON":
            draw_text_center("Modifier Chance: " + str(modifierchance) +"%", get_font(20), text_color, 400, 550)
        draw_text_center("Save Progress?: " + checkpointon, get_font(20), text_color, 400, 575)

        if room < 100 and loadvideo:
            draw_text_center("Playing Round: " + str(room), get_font(20), text_color, 400, 300)

        if rolling or addroll:
            draw_text_center(str(dierollface), get_font(35), diefacecolor, 400, 250)
        
        if (addroll or loadvideo) and room < 100:
            draw_text_center("Rolled a " + str(rolled_num), get_font(20), text_color, 400, 370)
        
        #Buttons
        if canplay or reward or skip or cursed:
            PLAY_MOUSE = pygame.mouse.get_pos()

        ROLL = command.Button(image=None,pos=(400,200), text_input= "Roll", font=get_font(20), base_color="white", hovering_color="grey")
        if canplay and room < 100:
            ROLL.changeColor(PLAY_MOUSE)
            ROLL.update(screen)
            rollbox = pygame.Rect.scale_by(ROLL.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', rollbox, 3)


        CHOICE1 = command.Button(image=None,pos=(600,350), text_input= "Pick", font=get_font(20), base_color="white", hovering_color="grey")
        CHOICE2 = command.Button(image=None,pos=(200,350), text_input= "Pick", font=get_font(20), base_color="white", hovering_color="grey")
        if reward and room < 100 and perkprimed:
            CHOICE1.changeColor(PLAY_MOUSE)
            CHOICE1.update(screen)
            choice1box = pygame.Rect.scale_by(CHOICE1.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', choice1box, 3)
            first, *middle, last = str(choice1).split()
            mid = " ".join(middle)
            draw_text_center(first + " " + str(mid), get_font(15), text_color, 600, 200)
            draw_text_center(last, get_font(15), text_color, 600, 230)

            CHOICE2.changeColor(PLAY_MOUSE)
            CHOICE2.update(screen)
            choice2box = pygame.Rect.scale_by(CHOICE2.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', choice2box, 3)
            first, *middle, last = str(choice2).split()
            mid = " ".join(middle)
            draw_text_center(first + " "+ str(mid), get_font(15), text_color, 200, 200)
            draw_text_center(last, get_font(15), text_color, 200, 230)
            draw_text_center("Pick a Perk...", get_font(20), text_color, 400, 160)
        
        SKIP = command.Button(image=None,pos=(550,350), text_input= "Skip", font=get_font(20), base_color="white", hovering_color="grey")
        if skip and room < 100:
            SKIP.changeColor(PLAY_MOUSE)
            SKIP.update(screen)
            skipbox = pygame.Rect.scale_by(SKIP.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', skipbox, 3)

        PLAY = command.Button(image=None,pos=(250,350), text_input= "Play", font=get_font(20), base_color="white", hovering_color="grey")
        if skip and room < 100:
            PLAY.changeColor(PLAY_MOUSE)
            PLAY.update(screen)
            playbox = pygame.Rect.scale_by(PLAY.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', playbox, 3)
        
        
        CONFIRM = command.Button(image=None,pos=(400,350), text_input= "Okay", font=get_font(20), base_color="red", hovering_color="grey")
        if cursed and room < 100:
            pygame.draw.rect(screen, 'red', pygame.Rect(30,145,750,250), 3)

            CONFIRM.changeColor(PLAY_MOUSE)
            CONFIRM.update(screen)
            confirmbox = pygame.Rect.scale_by(CONFIRM.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'red', confirmbox, 3)
            draw_text_center(curse, get_font(16), "red", 400, 230)
            draw_text_center("That Round carried a curse!", get_font(25), "red", 400, 170)
            


        #SAVEON = command.Button(image=None,pos=(605,575), text_input= "*", font=get_font(20), base_color="white", hovering_color="grey")
        #if canplay and room == 1:
            #if checkpointon == "ON":
                #SAVEON.changeColor(PLAY_MOUSE)
                #SAVEON.update(screen)
            #savebox = pygame.Rect.scale_by(SAVEON.text_rect, 1.2, 1.6)
            #pygame.draw.rect(screen, 'white', savebox, 3)

        if room == 1 and canplay:
            CHECK = command.Button(image=None,pos=(400,150), text_input= "Play Intro?", font=get_font(20), base_color="white", hovering_color="grey")
        elif room < 100 and canplay:
            CHECK = command.Button(image=None,pos=(400,150), text_input= "Play Checkpoint?", font=get_font(20), base_color="white", hovering_color="grey")
        if room >= 100 and canplay:
            CHECK = command.Button(image=None,pos=(400,180), text_input= "You Win!", font=get_font(20), base_color="white", hovering_color="grey")
        if canplay:
            CHECK.changeColor(PLAY_MOUSE)
        if room % 25 == 0 or room >= 100 or room == 1 and canplay:
            CHECK.update(screen)
            checkbox = pygame.Rect.scale_by(CHECK.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', checkbox, 3)
       
        if checkpointon == "ON" and room >= 25:
            DELETE = command.Button(image=None,pos=(400, 50), text_input= "Delete Save?", font=get_font(20), base_color="white", hovering_color="grey")
        else:
            DELETE = command.Button(image=None,pos=(400, 50), text_input= "Restart?", font=get_font(20), base_color="white", hovering_color="grey")
        if canplay and room > 1:
            DELETE.changeColor(PLAY_MOUSE)
            DELETE.update(screen)
            deletebox = pygame.Rect.scale_by(DELETE.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', deletebox, 3)

        #Updates the display every frame
        pygame.display.update()

        #Updates the clock and limits it to 60 fps
        clock.tick(30)
maingame()

#Ends the game on exit.
pygame.quit()
exit()
