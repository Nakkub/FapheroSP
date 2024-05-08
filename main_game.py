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
    #Checks the savedata for checkpoint(Will return 1 if no save)
    room = logic.loadsave()
    preroom = 1
    pausetime = 2
    pause = pausetime
    
    #Variables for dice process
    dierollface = 1
    rollingtime = 20
    diefacecolor = 'grey'

    #Game States
    canplay = True
    rolling = False
    addroll = False
    loadvideo = False

    #Game loop starts here
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            #Button pressing stage
            if canplay:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ROLL.checkForInput(PLAY_MOUSE) and canplay:
                        rolled_num = random.randint(1,6)
                        rollingtime = 30
                        rolling = True
                        canplay = False
                        diefacecolor = 'grey'
                        preroom = room
                    
                    elif CHECK.checkForInput(PLAY_MOUSE) and canplay and (room % 25 == 0 or room >= 100 or room == 1):
                        canplay = False
                        logic.video(room)
                        canplay = True
                    elif DELETE.checkForInput(PLAY_MOUSE) and canplay:
                        logic.deletesave()
                        room = 1

            #Rolling the die stage
            if rolling:
                if rollingtime > 0:
                    if event.type == dierolltimer:
                        if dierollface == 6:
                            dierollface = 1
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
                    if event.type == dieaddtimer:    
                        dierollface -= 1
                        room += 1
                else:
                    if pause > 0:
                        if event.type == halfsecond:
                            pause -= 1
                    else:
                        pause = pausetime                   
                        addroll = False
                        loadvideo = True

            if loadvideo:
                if pause > 0:
                    if event.type == halfsecond:
                        pause -= 1
                else:
                    pause = pausetime
                    if preroom % 25 > room % 25:
                        if room % 25 != 0:
                            logic.video(room - room%25)
                    if room < 100:
                        if room % 25 != 0:
                            print("Playing Round #" + str(room))
                            print("")
                        logic.video(room)
                        print("Break")
                        print("")
                        logic.image()
                    loadvideo = False
                    canplay = True
        #Black Background
        screen.fill("black")

        #Draws game version and round on the screen
        draw_text("FapLandSP VER.0.1", get_font(16), 'white', 0, 5)
        if room < 100:
            draw_text_center("Round:"+ str(room), get_font(50), 'white', 400, 100)
        else:
            draw_text_center("FapLand Completed!", get_font(40), 'white', 400, 100)
        
        #UI Info
        if (preroom % 25 > room % 25 or room % 25 == 0) or gen_set.checkp == "ON":
            draw_text_center("Checkpoint: " + str(room - room%25) +"%", get_font(20), text_color, 400, 450)
        if room < 100 and loadvideo:
            draw_text_center("Playing Round: " + str(room), get_font(20), text_color, 400, 300)

        if rolling or addroll:
            draw_text_center(str(dierollface), get_font(35), diefacecolor, 400, 250)
        
        if (addroll or loadvideo) and room < 100:
            draw_text_center("Rolled a " + str(rolled_num), get_font(20), text_color, 400, 370)
        if canplay:
            PLAY_MOUSE = pygame.mouse.get_pos()

        ROLL = command.Button(image=None,pos=(400,200), text_input= "Roll", font=get_font(20), base_color="white", hovering_color="grey")
        if canplay and room < 100:
            ROLL.changeColor(PLAY_MOUSE)
            ROLL.update(screen)
            rollbox = pygame.Rect.scale_by(ROLL.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', rollbox, 3)

        if room == 1:
            CHECK = command.Button(image=None,pos=(400,150), text_input= "Play Intro?", font=get_font(20), base_color="white", hovering_color="grey")
        elif room < 100:
            CHECK = command.Button(image=None,pos=(400,150), text_input= "Play Checkpoint?", font=get_font(20), base_color="white", hovering_color="grey")
        if room >= 100:
            CHECK = command.Button(image=None,pos=(400,180), text_input= "You Win!", font=get_font(20), base_color="white", hovering_color="grey")
        if canplay:
            CHECK.changeColor(PLAY_MOUSE)
        if room % 25 == 0 or room >= 100 or room == 1 and canplay:
            CHECK.update(screen)
            checkbox = pygame.Rect.scale_by(CHECK.text_rect, 1.2, 1.6)
            pygame.draw.rect(screen, 'white', checkbox, 3)
       
        if gen_set.checkp == "ON" and room >= 25:
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