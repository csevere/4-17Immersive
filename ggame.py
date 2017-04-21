#include pygame which we got from pip
#in order to use pygame, we have to run the init method

import pygame
import time
import math
pygame.init()
#clock = pygame.time.Clock()

from math import fabs
from random import randint

# 3 Create a screen with a size

screen = {
    "height": 512, #in pixels
    "width": 480,
    "goblin_width": 460,
    "goblin_height":450,
    "monster_width": 460,
    "monster_height": 450
}

keys = {
    "right": 275,
    "left": 276,
    "up": 273,
    "down":274
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down":False
}

hero = {
    "x": 100,
    "y": 100,
    "speed": 10,
    "Points": 0,
    "HP": 500,
}

goblin = {
    "x": 100,
    "y":100,
    "speed": 1,
    "dir_y": 1, #give the gobling direction
    "dir_x": 1

}

monster = {
    "x": 200,
    "y": 200,
    "speed": 1,
    "dir_y": 1, #give monster direction
    "dir_x": 1

}

gameDisplay = pygame.display.set_mode(((screen["width"]),(screen ["height"])))



def killmessage_display(text):
    font = pygame.font.Font(None, 25)
    message_display_text = font.render(text,True, (0,0,0)) #
    pygame_screen.blit(message_display_text, [200,200])
    pygame.display.flip()
    time.sleep(1) #makes content appear for duration of 2 sec

def hpmessage_display(text):
    font = pygame.font.Font(None, 25)
    message_display_text = font.render(text,True, (0,0,0))
    pygame_screen.blit(message_display_text, [200,200])
    pygame.display.flip()
    time.sleep(1)


screen_size = (screen["height"], screen["width"]) #requires we give it
#unchanged screen size
pygame_screen = pygame.display.set_mode(screen_size) #object called display,
#has something call set mode with a tuple with screen size
pygame.display.set_caption("Goblin Chase") #methond provided by display coming
#from pygame
background_image = pygame.image.load("./images/background.png")
hero_image = pygame.image.load("./images/hero.png")
goblin_image = pygame.image.load("./images/goblin.png")
monster_image = pygame.image.load("./images/monster.png")

hero_image_scaled = pygame.transform.scale(hero_image, (99,96));
hero_image_scaled = pygame.transform.scale(hero_image, (32,32))

#add music files
# pygame.mixer.music.load('./sounds/music.wav')
# pygame.mixer.music.play (-1) #-1 means loopforever
# win_sound = pygame.mixer.Sound ('./sounds/win.wav')
# lose_sound = pygame.mixer.Sound ('./sounds/lose.wav')


# 4 Create the game loop (while 1)
game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        elif event.type == pygame.KEYDOWN:
            if event.key == keys['up']:
                keys_down['up'] = True
            if event.key == keys['down']:
                keys_down['down'] = True
            if event.key == keys['left']:
                keys_down['left'] = True
            if event.key == keys['right']:
                keys_down['right'] = True



    # the user let go of a key... and that key was the up arrow
        elif event.type == pygame.KEYUP:
            if event.key == keys['up']:
                keys_down['up'] = False
            if event.key == keys['down']:
                keys_down['down'] = False
            if event.key == keys['left']:
                keys_down['left'] = False
            if event.key == keys['right']:
                keys_down['right'] = False


    #update hero position

    if keys_down['up']:
        hero['y'] -= hero ['speed']
    elif keys_down['down']:
        hero['y'] += hero ['speed']
    if keys_down['left']:
        hero['x'] -= hero ['speed']
    elif keys_down['right']:
        hero['x'] += hero ['speed']

    #update goblin direction dep on hero


    def run (object_1, object_2): #object1 is player, object2 is goblin
        if(object_2['x'] < (object_1['x'])):
            object_2['dir_x'] = -1

        if(object_2['x'] > (object_1['x'])):
            object_2 ['dir_x'] = 1

        if(object_2['y'] < (object_1['y'])):
            object_2['dir_y'] = -1

        if(object_2['y'] < (object_1['y'])):
            object_2['dir_y'] = 1

        if(object_2['x'] == (object_1['x'])):
            object_2['dir_x'] = 0

        if(object_2['y'] == (object_1['y'])):
            object_2['dir_y'] = 0

    #update object's x and y position

    def move (o_bject):  #use speed to add to object's x and y position
        o_bject['x'] += o_bject['speed'] * o_bject['dir_x']
        o_bject ['y'] += o_bject ['speed'] * o_bject['dir_y']

        if ((o_bject['x']) > 460): #right side of square
            o_bject['x'] -= 20

        if ((o_bject['y']) > 450): #bottom of square
            o_bject['y'] -= 20

        if ((o_bject['x']) < 10): #left side of square
            o_bject['x'] += 20

        if ((o_bject['y']) < 10): #top of square
            o_bject['y'] += 20



    def chase (object_1, object_2): #object1 is player, object2 is monster
        if(object_2['x'] < (object_1['x'])):
            object_2['dir_x'] = 1

        if(object_2['x'] > (object_1['x'])):
            object_2 ['dir_x'] = -1

        if(object_2['y'] < (object_1['y'])):
            object_2['dir_y'] = 1

        if(object_2['y'] > (object_1['y'])):
            object_2['dir_y'] = -1

        if(object_2['x'] == (object_1['x']) and (object_2['y']) == (object_1['y'])):
            object_2['dir_x'] = 0
            object_2['dir_y'] = 0

    #update monster's x and y position




    #COLLISION DETECTION
    distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])

    if (distance_between < 32):
        print ("Killed a Goblin!!")
    #Generate a random X > 0, X < screen['width']
    #Generate a random Y > 0, Y < screen['height'] for the goblin
        rand_x = randint (0, screen ["goblin_width"])
        rand_y = randint (0, screen ["goblin_height"])
        goblin['x'] = rand_x
        goblin['y'] = rand_y
        #update the hero's wins
        hero['Points'] += 50

        def kill():
            killmessage_display("Killed a Goblin!") #calling message
        kill()

     # win_sound.play()
    distance_between = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])



    if (distance_between < 32):
        print ("Eaten!!")
    #Generate a random X > 0, X < screen['width']
    #Generate a random Y > 0, Y < screen['height'] for the moster
        rand_x = randint (0, screen ["monster_width"])
        rand_y = randint (0, screen ["monster_height"])
        monster['x'] = rand_x
        monster['y'] = rand_y
        #update the hero's losses
        hero['HP'] -= 5

        # def message_display(text):
        #     font = pygame.font.Font(None, 25)
        #     message_display_text = font.render("Lost HP!",True, (0,0,0))
        #     pygame_screen.blit(message_display_text, [200,200])

        def eaten():
            hpmessage_display ("Lost HP!")
        eaten()

    #make hero wrap around inside the box

    if ((hero['x']) > 460): #right side of square
        hero ['x'] -= 20

    if ((hero['y']) > 450): #bottom of square
        hero ['y'] -= 20

    if ((hero['x']) < 10): #left side of square
        hero ['x'] += 20

    if ((hero['y']) < 10): #top of square
        hero ['y'] += 20


    run(hero, goblin) #grabbing functions of monster and hero

    chase(hero, monster)

    move(monster)

    move(goblin)


    # pygame_screen.blit(losses_text, [,])



    pygame_screen.blit(background_image, [0,0])
    pygame_screen.blit(hero_image, [hero['x'], hero['y']])
    pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
    pygame_screen.blit(monster_image, [monster['x'], monster['y']])

    font = pygame.font.Font(None, 25)
    points_text = font.render("Points: %d" % (hero['Points']), True, (0,0,0))
    hp_text = font.render("HP: %d" % (hero['HP']), True, (0,0,0))

    pygame_screen.blit(points_text, [40,40])
    pygame_screen.blit(hp_text, [360,40])





    # must display wins_text before display.flip
    pygame.display.flip()






#update our boolean so pygame can escape
# print(event) #will allow you to see everything you do within the pygame window
# pygame.display.update()
# clock.tick(60)
# 5 Add a quit event (requires sys) #won't run without quit event

##we are inside the main game loop. It will run as long as game_on is true
#looping through all events that happen
#this game loop cycle
# Screen.fill (pass bg_color)
# Flip the screen and start ove4
#game loop, waiting for user input
#the user clicked on the red X to elave the game
