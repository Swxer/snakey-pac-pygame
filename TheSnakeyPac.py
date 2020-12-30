import pygame
import time
import random

pygame.init()
yummy = pygame.mixer.Sound("yummy.wav")

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
neon = (57,255,20)
yellow = (255,255,0)
orange = (255,195,77)
lightpink = (255,113,181)
lightpurple = (209,178,234)
lightcyan = (164,231,223)
lightred = (246,70,91)
mediumgray = (134,136,138)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Snakey Pac')

clock = pygame.time.Clock()

img = pygame.image.load('pac1.png')
bodyimg = pygame.image.load('pacbody.png')
johnimg = pygame.image.load('bacteria.png')

icon = pygame.image.load('zipzap.png')
pygame.display.set_icon(icon)

AppleThickness = 30

block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 75)

def pause():

    paused = True
    message_to_screen("Paused", lightred, -50, size="large")
    message_to_screen("Press C to resume or Q to rage quit.", lightcyan, 25,'small')
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, neon)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX, randAppleY               

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                
        gameDisplay.fill(black)
        message_to_screen("Welcome to The Snakey Pac!", lightpink, -100,"medium")
        message_to_screen("You are in a strange arcade universe...", lightpurple, -50, "small")
        message_to_screen("There is a strange species lying around inside this window...", lightpurple, -25, "small")
        message_to_screen("Eat them so you can grow strong and to survive.", lightpurple, 0, "small")
        message_to_screen("Eat yourself and you will lose.", lightpurple, 25, "small")
        message_to_screen("Touch the edge of the window and you lose aswell.", lightpurple, 50, "small")
        message_to_screen("Press C to start, P to pause, or Q to rage quit immediately.", lightcyan, 95, "small")
        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):

    if direction == "right":
        head  = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        gameDisplay.blit(bodyimg, (XnY[0],XnY[1]))
        #pygame.draw.rect(gameDisplay, yellow, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg, color, y_displace=0, size = 'small'):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:

        if gameOver == True:
            message_to_screen("Your snakey Pacman ate himself!",lightred, -50, size="medium")
            message_to_screen("Press C to play again or Q to rage quit.", lightcyan, 50, size = "small")
            pygame.display.update()
        while gameOver == True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit   = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEXIT = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change= 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)

        
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(johnimg, (randAppleX, randAppleY))

    #(X, Y, Breadth, Height (the height goes down as a positive direction))

            
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
                del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                
        snake (block_size, snakeList)
            
        snake(block_size, snakeList)


        score(snakeLength-1)
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                pygame.mixer.Sound.play(yummy)

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                pygame.mixer.Sound.play(yummy)

            

        clock.tick(FPS)

    pygame.quit()
    quit()
    
game_intro()
gameLoop()
