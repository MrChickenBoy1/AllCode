import pygame
from pygame import *

pygame.init()

WIN = pygame.display.set_mode((500, 500))

Grid = [["_"]*4 for i in range (4)]
print (Grid)

class X():
    def __init__(self) -> None:
        self.image = pygame.image.load("X.png")
        
    def draw ():
        WIN.blit(self.image, )

class GridStuff():
    def __init__(self, grid):
        self.grid = grid
        self.dist = 85
        self.ofest = 180
#Makes the grid
    def initialise (self):
        pygame.draw.rect(WIN, (0, 0, 0), (self.num2 * self.dist + 37.5 - 5, self.num1 * self.dist + 37.5 - 5, 50, 50))
        for i in range (3): 
            for j in range (3):
                pygame.draw.rect(WIN, (0, 0, 0), (self.dist * j + self.ofest, WIN.get_width() / 2 - 150, 5, 320))
                pygame.draw.rect(WIN, (0, 0, 0), (WIN.get_height() / 2 - 150, self.dist * j + self.ofest, 320, 5))
                


    def input (self):
        #x
        self.num1 = int(input("num 1"))
        self.num2 = int(input("num 2"))
        self.grid[self.num1 - 1][self.num2 - 1] = "x"
        

        print (self.grid)


run = True

GridInstance = GridStuff(Grid)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    WIN.fill((255, 255, 255))
    

    GridInstance.input()
    GridInstance.initialise()
    pygame.display.update()