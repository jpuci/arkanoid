import pygame, sys
import math
import time
import random
from paddle import paddle
from ball import ball
from block import block
from specials import special_opt
from pointer import pointer
from setting import set_pics
import os

#path of current running file
path = os.path.dirname(os.path.abspath(__file__))

#pre init mixer to cancel delay when playing sounds
pygame.mixer.pre_init(44100, -16, 1, 512)

#setting display and clock
pygame.init()
win_size = (800, 600)
win = pygame.display.set_mode(win_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Break")

#load background images
bg = pygame.image.load(path + '\\backgrounds\\bg.png')
menu_bg = pygame.image.load(path + "\\backgrounds\\menu_bg.png")
scores_bg = pygame.image.load(path +"\\backgrounds\\scores_bg.png")
set_bg = pygame.image.load(path +"\\backgrounds\\set_bg.png")
inst_bg = pygame.image.load(path+"\\backgrounds\\inst_bg.png")
cred_bg = pygame.image.load(path+"\\backgrounds\\cred_bg.png")

#load sounds
ping_sound = pygame.mixer.Sound(path+"\\sounds\\ping_sound.wav")
crack_sound = pygame.mixer.Sound(path+"\\sounds\\crack_sound.wav")
pygame.mixer.Sound.set_volume(crack_sound, 0.5)
lose_sound = pygame.mixer.Sound(path+"\\sounds\\lose.wav")
lost_life_sound = pygame.mixer.Sound(path+"\\sounds\\lost_of_life.wav")
puck_sound = pygame.mixer.Sound(path+"\\sounds\\puck.wav")
pygame.mixer.Sound.set_volume(puck_sound, 0.5)
win_sound = pygame.mixer.Sound(path+"\\sounds\\win_sound.wav")
pygame.mixer.music.load(path+"\\sounds\\egypt_music.mp3")
pygame.mixer.music.set_volume(0.1)
is_sound = True
#play music
pygame.mixer.music.play(-1)

#fonts
font = pygame.font.SysFont('papyrus', 22, True)
font2 = pygame.font.SysFont('papyrus', 40, True)
font3 = pygame.font.SysFont('papyrus', 40, True)

#colors
red = (150, 0, 0)
green = (38, 88, 14)

def menu_fun():
    """display menu background,
    initalize point of class pointer
    hadles events form keyboard. """

    #init pointer
    pointSprite = pygame.sprite.RenderClear()
    point = pointer((200, 187))
    pointSprite.add(point)

    global menu
    global instruction
    global credit
    global run
    global settings
    global infty
    global scores
    global pointerloop

    #init global variables
    run = False
    instruction = False
    credit = False
    settings = False
    scores = False


    while menu:
        clock.tick(100)
        #blit background image
        win.blit(menu_bg, (0, 0))

        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                #play sound when key is pressed
                if is_sound:
                    puck_sound.play()

                #move point
                if event.key == pygame.K_DOWN:
                    if point.rect.center[1] == 497:
                        pointSprite.update(-310)
                    else:
                        pointSprite.update(62)
                elif event.key == pygame.K_UP:
                    if point.rect.center[1] == 187:
                        pointSprite.update(310)
                    else:
                        pointSprite.update(-62)

                #when enter is pressed in specific positions
                elif event.key == pygame.K_RETURN:

                    # if in first position run (game) is set to true
                    #menu to false and timer is initalized
                    if point.rect.center[1] == 187:
                        menu = False
                        run = True
                        global timer
                        timer = time.time()

                    #if in second position menu is set to false
                    #settings to true and settings_fun is called
                    elif point.rect.center[1] == 249:
                        menu = False
                        settings = True
                        settings_fun()

                    #if in third menu is set to false
                    #instruction to true and instruction_fun is called
                    elif point.rect.center[1] == 311:
                        menu = False
                        instruction = True
                        instruction_fun()

                    #if in fourth menu is set to false
                    #scores to true and scores_fun is called
                    elif point.rect.center[1] == 373:
                        menu = False
                        scores = True
                        scores_fun()

                    #if in fifth menu is set to false
                    #credit to true and cred_fun is called
                    elif point.rect.center[1] == 435:
                        menu = False
                        credit = True
                        cred_fun()

                    #if in sixth exit the process
                    elif point.rect.center[1] == 497:
                        sys.exit(0)

        #draw point
        pointSprite.draw(win)
        #update display
        pygame.display.update()


def scores_fun():
    """Create lists of best scores from
    classic and infinite modes and display them.
    Blit scores_bg as background. Handle events."""
    global scores
    global menu

    scores_list = []
    #appending not blank lines to scores_list
    f = open("wyniki.txt", "r+").readlines()
    for line in f:
        if line != "" and line != "\n":
            scores_list.append(float(line.strip("\n")))
    #sort
    scores_list = sorted(scores_list)

    #if needed append to 10 positions with 0.00 values
    if len(scores_list) < 10:
        for i in range(10 - len(scores_list)):
            scores_list.append(0.00)

    inf_scores_list = []

    #repeat procedure for scores from infinite mode
    f = open("inf_wyniki.txt", "r+").readlines()
    for line in f:
        if line != "" and line != "\n":
            inf_scores_list.append(float(line.strip("\n")))


    # but revere them so the highest number would be on top
    inf_scores_list = sorted(inf_scores_list, reverse=True)


    if len(inf_scores_list) < 10:
        for i in range(10 - len(inf_scores_list)):
            inf_scores_list.append(0.00)


    while scores:
        clock.tick(100)
        #blit background image
        win.blit(scores_bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                #play sound when key is pressed
                if is_sound:
                    puck_sound.play()
                if event.key == pygame.K_ESCAPE:
                    #if esc is pressed return to menu
                    scores = False
                    menu = True
                    menu_fun()


        #blit best scores
        for i in range(10):
            if i == 9:
                distance = - 25
            else:
                distance = 0
            text = font2.render(str(i + 1) + ".   " + str(scores_list[i]), 1, green)
            text2 = font2.render(str(i + 1) + ".   " + str(inf_scores_list[i]), 1, green)
            win.blit(text, (140 + distance, 180 + i * 30))
            win.blit(text2, (450 + distance, 180 + i * 30))

        #update display
        pygame.display.update()

def settings_fun():
    """Initalize three vars of type
    set_pics, responsible for display of icons and pointer.
    Blit set_bg as background. Hadles events"""

    global settings
    global menu
    global is_sound
    global inf_mode

    #initialize set_pics vars
    setSprite = pygame.sprite.RenderClear()
    mymusic = set_pics((320, 220), 1, "music")
    mysound = set_pics((320, 310), 1, "sound")
    myinfty = set_pics((320, 400), 0, "infty")
    setSprite.add(mymusic)
    setSprite.add(mysound)
    setSprite.add(myinfty)

    #initalize pointer
    pointSprite = pygame.sprite.RenderClear()
    point = pointer((150, 220))
    pointSprite.add(point)


    while settings:
        clock.tick(100)
        #blit background image
        win.blit(set_bg, (0, 0))
        setSprite.draw(win)
        pointSprite.draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                #play sound when key is pressed
                if is_sound:
                    puck_sound.play()
                if event.key == pygame.K_DOWN:
                    #move pointer
                    if point.rect.center[1] == 400:
                        point.update(-180)
                    else:
                        point.update(90)
                elif event.key == pygame.K_UP:
                    #move pointer
                    if point.rect.center[1] == 220:
                        point.update(180)
                    else:
                        point.update(-90)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #changes options of set_pics var if pointer is in the right position
                    for i in setSprite:
                        if point.rect.center[1] == i.rect.center[1]:
                            if i.option == 0:
                                i.option = 1
                            else:
                                i.option = 0
                elif event.key == pygame.K_ESCAPE:
                    #if esc is pressed return to menu
                    #inf_mode set to last myinfty option

                    settings = False
                    menu = True
                    inf_mode = myinfty.option
                    menu_fun()

        #update sprites (change images)
        setSprite.update()

        #stop and play the music
        if mymusic.option == 0:
            pygame.mixer.music.pause()
        elif mymusic.option == 1:
            pygame.mixer.music.unpause()

        #set mysound to true or false based on mysound option
        if mysound.option == 0:
            is_sound = False
        else:
            is_sound = True

def instruction_fun():
    """Blit inst_bg as background.
    Handle events"""
    global instruction
    global menu

    while instruction:
        #blit background image
        win.blit(inst_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                #if esc is pressed return to menu
                if event.key == pygame.K_ESCAPE:
                    instruction = False
                    menu = True
                    menu_fun()
        #update display
        pygame.display.update()

def cred_fun():
    """Blit inst_bg as background.
        Handle events"""
    global menu
    global credit
    while credit:
        #blit background
        win.blit(cred_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #if esc is pressed return to menu
                    instruction = False
                    menu = True
                    menu_fun()
        #update display
        pygame.display.update()


def redraw_game_window():
    '''Blit everything that is displayed
    in the window during the game'''

    #bacground image
    win.blit(bg, (0, 0))

    #update and draw paddle
    mypaddleSprite.update(win_size)
    mypaddleSprite.draw(win)

    #update and draw blocks
    myblockSprite.update()
    myblockSprite.draw(win)

    #draw ball and lives
    myball.draw(win)
    myball.lives(win)

    #update and draw special effects
    myspecialSprite.update()
    myspecialSprite.draw(win)

    #blit text
    text = font.render("lives: ", 1, green)
    win.blit(text, (5, 530))



    #if game over
    if myball.lives_count < 0:
        #blit text to win
        text8 = font.render("Press ENTER to return to menu or ESC to quit", 1, red)
        middle_blit(text8, 400)
        text3 = font3.render("GAME OVER", 1, red)
        middle_blit(text3, 250)

        if inf_mode:
            #if inf_mode blit score
            text7 = font3.render("SCORE: " + str(inf_scores_count), 1, red)
            middle_blit(text7, 330)




    elif len(myblockSprite) <= 0:
        #blit text
        text8 = font.render("Press ENTER to return to menu or ESC to quit", 1, red)
        middle_blit(text8, 400)
        text4 = font3.render("YOU WON", 1, red)
        #scores
        if inf_mode:
            text5 = font3.render("SCORE: " + str(inf_scores_count), 1, (255,0,0))
        else:
            text5 = font3.render("SCORE: " + str(final_time), 1, red)
        middle_blit(text4, 200)
        middle_blit(text5, 300)

    if not len(myblockSprite) <= 0 and not myball.lives_count < 0 and not inf_mode:
        #draw timer if not in infinity mode
        draw_timer()

    if inf_mode:
        # if in infinity mode blit score
        text6 = font.render("Score: " + str(inf_scores_count), 1, green)
        win.blit(text6, (15, 3))

    #update display
    pygame.display.update()


def create_blocks(y, myblockSprite, dur=0):
    '''Take three arguments: y coorindate,
    grup of Sprites and dur (durability).
    Creates full row ofinstances of type
    block and add it to the sprite.'''
    i = 50
    block_list = []

    while i < 800:
        if inf_mode:
            dur = random.choice([1, 2, 3])
        special = random.choice([True, False])
        myblock = block(dur, i, y, special)
        block_list.append(myblock)
        myblockSprite.add(myblock)
        i += 100
    return block_list


def paddle_bounce():
    """Handle ball bouncing when it
    hits the paddle"""

    #check if ball collide with paddle and if it's free
    if mypaddle.rect.left < myball.x + 8 and myball.x - 8 < mypaddle.rect.right and 460 < myball.y < 476 and myball.free:
        #play sound
        if is_sound:
            ping_sound.play()
        center = (mypaddle.rect.left + mypaddle.rect.right)/2
        mid_len = mypaddle.rect.right - center
        fraction = math.fabs(myball.x - center)/mid_len
        #get angle
        alpha = (math.pi/2) * (1 - (2/3)*fraction)

        #change velocity x for collision on the right side
        if myball.x > center:
            #if special options are currently in use velocity change
            if count_list[1] > 1:
                myball.vel_x = round(14 * math.cos(alpha))
            elif count_list[0] > 1:
                myball.vel_x = round(3.5 * math.cos(alpha))
            else:
                myball.vel_x = round(7 * math.cos(alpha))

        #change velocity x for collision on the left side
        else:
            if count_list[1] > 1:
                myball.vel_x = round(-14 * math.cos(alpha))

            elif count_list[0] > 1:
                myball.vel_x = round(-3.5 * math.cos(alpha))

            else:
                myball.vel_x = round(-7 * math.cos(alpha))

        #change velocity y
        if count_list[1] > 1:
            myball.vel_y = round(-14 * math.sin(alpha))
        elif count_list[0] > 1:
            myball.vel_y = round(-3.5 * math.sin(alpha))
        else:
            myball.vel_y = round(-7 * math.sin(alpha))



def draw_timer():
    """With use of timer variable
    gets time since the begining of the game
    and blit it to screen"""
    counting_seconds = str(round(time.time() - timer, 2))
    text = font.render("time: " + counting_seconds, 1, green)
    win.blit(text, (15, 3))

def update_score():
    """Add scores to files:
    scores from infinite mode to inf_wyniki.tex,
    from classic mode to wyniki.tex"""
    if inf_mode:
        with open("inf_wyniki.txt", "a+") as f:
            f.write(str(inf_scores_count) + "\r\n")
        f.close()
    else:
        with open("wyniki.txt", "a+") as f:
            f.write(str(final_time) + "\r\n")
        f.close()

def middle_blit(text, y):
    """Get text and y cooridinate and
    blit text in the middle of the screen"""
    text_width = text.get_width()
    win.blit(text, (win_size[0] // 2 - text_width // 2, y))

#set inf_mode to deafult value
inf_mode = False

#run menu function
menu = True
menu_fun()


#init paddle
mypaddleSprite = pygame.sprite.RenderClear()
mypaddle = paddle(win_size)
mypaddleSprite.add(mypaddle)

#init ball
myball = ball()

#init blocks
myblockSprite = pygame.sprite.RenderClear()
blocks1 = create_blocks(170, myblockSprite, 1)
blocks2 = create_blocks(115, myblockSprite, 2)
blocks3 = create_blocks(60, myblockSprite, 3)

#init specials
myspecialSprite = pygame.sprite.RenderClear()
count_list = [0, 0, 0, 0]


#set count for infinite mode and score count
inf_count = 600
inf_scores_count = 0

def reset():
    """Sets variables to deafult value
    and update them to globals to allow
    playing next game"""
    # set count for infinite mode and score count
    inf_count = 600
    inf_scores_count = 0
    # init specials
    myspecialSprite = pygame.sprite.RenderClear()
    count_list = [0, 0, 0, 0]
    # init blocks
    myblockSprite = pygame.sprite.RenderClear()
    blocks1 = create_blocks(170,myblockSprite, 1)
    blocks2 = create_blocks(115,myblockSprite, 2)
    blocks3 = create_blocks(60,myblockSprite, 3)
    # init ball
    myball = ball()

    # init paddle
    mypaddleSprite = pygame.sprite.RenderClear()
    mypaddle = paddle(win_size)
    mypaddleSprite.add(mypaddle)
    globals().update(locals())

#main loop
while run:
    #fps
    clock.tick(30)

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            #move paddle
            if event.key == pygame.K_LEFT:
                mypaddle.vel = -5
            #move paddle
            elif event.key == pygame.K_RIGHT:
                mypaddle.vel = 5
            #free the ball
            elif event.key == pygame.K_SPACE:
                if not myball.free:
                    myball.vel_x = 0
                    if count_list[0] > 1:
                        myball.vel_y = -3.5
                    elif count_list[1] > 1:
                        myball.vel_y = -14
                    else:
                        myball.vel_y = -7
                myball.free = True

        elif event.type == pygame.KEYUP:
            #stop moving paddle when key is not pressed
            if event.key == pygame.K_LEFT:
                mypaddle.vel = 0

            elif event.key == pygame.K_RIGHT:
                mypaddle.vel = 0

    if inf_mode:
        if inf_count > 0:
            #counting down
            inf_count -= 1
        if inf_count == 0:
            #after 20s move all blocks down
            for i in myblockSprite:
                i.move_down()
            #and create new row of random durability
            create_blocks(60, myblockSprite)
            #reset count
            inf_count = 600


    #if ball is not free it is placed above the paddle
    if not myball.free:
        myball.x = mypaddle.rect.center[0]
        myball.y = mypaddle.rect.top - 8
        myball.vel_x, myball.vel_y = 0, 0

    #move ball
    myball.move(lost_life_sound, is_sound, ping_sound)

    #check and execute collision with paddle
    paddle_bounce()

    #check collisions with blocks
    direction = 1
    for i in myblockSprite:
        if myball.hitbox.colliderect(i.rect):
            i.dur -= 1
            direction += 1
            inf_scores_count += 1
            #play sound
            if is_sound:
                crack_sound.play()
        if i.dur == 0:
            i.kill()
            if i.special:
                myspecialSprite.add(special_opt(i.rect.center))
    #variable direction allows to properly move ball when it hits
    #more than one block during a short period of time
    if direction != 1:
        myball.vel_y *= -1

    #check paddle collision with special
    for i in myspecialSprite:
        if mypaddle.rect.colliderect(i.rect):

            #if option is 0 (slow paddle) change velocity
            if i.option == 0:
                if count_list[0] <= 1:
                    #set count
                    count_list[0] = 300
                    myball.vel_x *= 0.5
                    myball.vel_y *= 0.5

            #if option is 1 (fast paddle) change velocity
            elif i.option == 1:
                if count_list[1] <= 1:
                    #set count
                    count_list[1] = 300
                    myball.vel_x *= 1.4
                    myball.vel_y *= 1.4

            #if option is 2 (long paddle) update paddle image
            elif i.option == 2:
                if count_list[2] <= 1:
                    count_list[2] = 300
                    mypaddle.len = 1
                    mypaddle.change_paddle()

            #if option is 3 (short paddle) update paddle image
            elif i.option == 3:
                if count_list[3] <= 1:
                    count_list[2] = 300
                    mypaddle.len = -1
                    mypaddle.change_paddle()

            #destroy block when it collide
            i.kill()

    for i in range(4):
        #count down on counts
        if count_list[i] > 1:
            count_list[i] -= 1

        #when count value is 1 reset to default values
        elif count_list[i] == 1:
            if i == 0:
                myball.vel_x *= 2
                myball.vel_y *= 2
                count_list[i] = 0

            elif i == 1:
                myball.vel_x *= 10/14
                myball.vel_y *= 10/14
                count_list[i] = 0

            elif i == 2:
                mypaddle.len = 0
                count_list[i] = 0
                mypaddle.change_paddle()

            elif i == 3:
                mypaddle.len = 0
                count_list[i] = 0
                mypaddle.change_paddle()

    #if there are more than six rows of blocks at the time
    for i in myblockSprite:
        if i.rect.center[1] >= 335:
            #you lose
            myball.lives_count = -1

    #if your used all lives
    if myball.lives_count < 0:
        #play sound
        if is_sound:
            lose_sound.play()
        #if in infinite mode update score
        if inf_mode:
            update_score()

    #if there are no blocks left
    if len(myblockSprite) == 0:
        if is_sound:
            win_sound.play()
        #your final time is your score (in classic mode)
        final_time = round(time.time() - timer, 2)
        update_score()

    #when the game is over
    while myball.lives_count < 0 or len(myblockSprite) == 0:
        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #if enter go back to menu
                    #and reset all variables to default
                    menu = True
                    reset()
                    menu_fun()
                elif event.key == pygame.K_ESCAPE:
                    #if esc exit
                    sys.exit(0)

        #update display
        redraw_game_window()
    #update display
    redraw_game_window()
