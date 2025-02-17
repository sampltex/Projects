import pygame
from pygame.locals import *
import math
import numpy as np
import random
# from random import randint

pygame.init()
screenHeight = 720
screenWidth = 1280
cellSize = 10 # 40 size is 32 by 18 grid  
updateInterval = 5

screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

edge = Rect((0,0), (screenWidth,screenHeight))

gameBoard = np.zeros((int(screenHeight/cellSize),int(screenWidth/cellSize)))

def drawGrid():
    drawPos = 0
    for i in range(int(screenHeight/cellSize)*2):
        pygame.draw.line(screen, "dimgray", (drawPos, 0), (drawPos, screenHeight))
        pygame.draw.line(screen, "dimgray", (0, drawPos), (screenWidth,drawPos))
        drawPos += cellSize 
    pygame.draw.rect(screen, "dimgray", edge, 1)

def drawCell(CellX: int, CellY: int):
    pixelX = CellX * cellSize
    pixelY = CellY * cellSize
    cell = Rect((pixelX-cellSize,pixelY-cellSize),(cellSize,cellSize))
    pygame.draw.rect(screen, "white", cell, 0)
    if CellX > 0 and CellX < (screenWidth/cellSize)+1 and CellY > 0 and CellY < (screenHeight/cellSize)+1:
        gameBoard[CellY-1][CellX-1] = 1
        # print(gameBoard[CellY-1][CellX-1])

def removeCell(CellX: int, CellY: int):
    if CellX > 0 and CellX < (screenWidth/cellSize)+1 and CellY > 0 and CellY < (screenHeight/cellSize)+1:
        gameBoard[CellY-1][CellX-1] = 0
        # print(gameBoard[CellY-1][CellX-1])

def calcMouseCellPos() -> list:
        mousePosX,mousePosY = pygame.mouse.get_pos()
        mousePosX = math.ceil(mousePosX / cellSize) * cellSize
        mousePosY = math.ceil(mousePosY / cellSize) * cellSize
        return [mousePosX,mousePosY]

def drawMouseCell(): 
    currentCell = Rect((calcMouseCellPos()[0]-cellSize,calcMouseCellPos()[1]-cellSize),(cellSize,cellSize))
    pygame.draw.rect(screen, "azure4", currentCell, 0)

def checkCellStatus(CellX: int, CellY: int) -> int:
    # try: 
        return int(gameBoard[CellY-1][CellX-1])
    # except:
    #     IndexError
    # return 0

def updateBoard():
    # current cell is at int(gameBoard[CellY-1][CellX-1])
    nextBoard = gameBoard.copy()
    for CellY in range(int(screenHeight/cellSize)):
        for CellX in range(int(screenWidth/cellSize)):
            countAlive = 0
            CheckCells = [checkCellStatus(CellX-1,CellY-1),checkCellStatus(CellX-1,CellY),checkCellStatus(CellX-1,CellY+1),
            checkCellStatus(CellX,CellY-1),checkCellStatus(CellX,CellY+1),checkCellStatus(CellX+1,CellY-1),
            checkCellStatus(CellX+1,CellY),checkCellStatus(CellX+1,CellY+1)]
            countAlive += sum(CheckCells)
            if bool(int(gameBoard[CellY-1][CellX-1])):
                if countAlive < 2 or countAlive > 3:
                    nextBoard[CellY-1][CellX-1] = 0
            else:
                if countAlive == 3:
                    nextBoard[CellY-1][CellX-1] = 1
    # print(f"gameboard:\n{gameBoard}")
    # print(f"nextboard:\n{nextBoard}")
    gameBoard[:] = nextBoard[:]
        

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                updateBoard()   
            if event.key == pygame.K_UP:
                updateInterval *= 2
            if event.key == pygame.K_DOWN:
                updateInterval /= 2
            if event.key == pygame.K_BACKSPACE: # reset board   
                gameBoard = np.zeros((int(screenHeight/cellSize),int(screenWidth/cellSize)))
    if event.type == pygame.KEYDOWN: # taking this out of the for loop makes it check every frame so you can hold down the key
        if event.key == pygame.K_RIGHT:
            updateBoard()
            pygame.time.delay(int(1000/updateInterval))

    screen.fill("black")
 
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        drawCell(int(calcMouseCellPos()[0]/cellSize),int(calcMouseCellPos()[1]/cellSize))

    elif pygame.mouse.get_pressed(num_buttons=3)[2]:
        removeCell(int(calcMouseCellPos()[0]/cellSize),int(calcMouseCellPos()[1]/cellSize))
    
    drawMouseCell()

    county = 1
    for y in gameBoard:
        countx = 1  # Reset per row
        for x in y:
            if x == 1:
                drawCell(countx, county)  # Use countx BEFORE incrementing
            countx += 1  # Increment after using it
        county += 1  # Move to next row after finishing a row
    
    drawGrid()

    pygame.display.update()

    clock.tick(60)