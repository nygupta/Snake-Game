import pygame
import random
pygame.init()

#colour
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

#creating window
ScreenWidth = 400
ScreenHeight = 300
gameWindow = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()


ExitGame = False
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

Multiple = []
for i in range (10, 50000,7):
    
    Multiple.append(i)

def textScreen(text, colour, x, y):
    screenText = font.render(text, True, colour)
    gameWindow.blit(screenText, [x, y])

def plotsnake(gameWindow, colour, snakeList, snakeSize):
    for x, y in snakeList:
        pygame.draw.rect(gameWindow, colour, [x, y, snakeSize, snakeSize])


def gameLoop():

    #game specific avriables
    with open("highscore.txt", "r") as f:
        hiscore = f.read()
    ExitGame = False
    GameOver = False
    velocityX = 0
    velocityY = 0
    initVelocity = 1
    snakeX = ScreenWidth / 2
    snakeY = ScreenHeight / 2
    snakeSize = 5
    fps = 30
    foodX = random.randrange(100, ScreenWidth / 2)
    foodY = random.randrange(50, ScreenHeight / 2)
    score = 0

    snakeList= []
    snakeLength = 1

    while not ExitGame:
        if GameOver:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            textScreen("Game Over", red, 100, 100)
            textScreen("   Score: " + str(score), red, 100, 150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ExitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ExitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocityY = initVelocity 
                        velocityX = 0
                    if event.key == pygame.K_UP:
                        velocityY = -initVelocity 
                        velocityX = 0
                    if event.key == pygame.K_RIGHT:
                        velocityX = initVelocity 
                        velocityY = 0
                    if event.key == pygame.K_LEFT:
                        velocityX = -initVelocity 
                        velocityY = 0
                    if event.key == pygame.K_q:
                        GameOver = True

            snakeX += velocityX
            snakeY += velocityY

            if abs(snakeX - foodX) < 6 and abs(snakeY - foodY) < 6:
                if score in Multiple:
                    score += 2
                else:
                    score += 1
                initVelocity += 0.1
                foodX = random.randrange(50, ScreenWidth - 10)
                foodY = random.randrange(55, ScreenHeight - 10)
                snakeLength += 5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(black)
            textScreen("Score: " + str(score) + "     Hiscore: " + str(hiscore), red, 5, 5)
            textScreen("------------------------------------", red, 0, 25); 
            if score in Multiple:
                pygame.draw.circle(gameWindow, red, [foodX, foodY], snakeSize * 2)
            else:
                pygame.draw.rect(gameWindow, red, [foodX, foodY, snakeSize, snakeSize])

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)

            if len(snakeList) > snakeLength:
                del snakeList[0]

            if head in snakeList[0: -1]:
                GameOver = True

            if snakeX < 0 or snakeX > ScreenWidth or snakeY < 52 or snakeY > ScreenHeight:
                GameOver = True

            plotsnake(gameWindow, green, snakeList, snakeSize)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameLoop()
