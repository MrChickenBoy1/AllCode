import pygame, time
from random import randint
from pygame import mixer
import os


pygame.init()fdsfsfsdfdsf
Window = pygame.display.set_mode((500, 500))

def redraw():
    Window.fill((79, 124, 196))

class Player (object):
    def __init__(self):
        self.x = 50
        self.y = 450

        self.width = 32
        self.height = 32
        self.vel = 400
        self.player = pygame.image.load(r"D:\Users\User\Documents\My python programs\Pygames\1stGame\Collect.png")
        self.PlayerRect = self.player.get_rect()



    def Draw (self, Window):
        Window.blit(self.player, (self.x, self.y))


    def PlayerUpdate(self):
         #-------Changing Player Rect Position-------
        PlayerInstance.PlayerRect.x = PlayerInstance.x
        PlayerInstance.PlayerRect.y = PlayerInstance.y

        #-------Call Functions-------
        PlayerInstance.Draw(Window)





class Apple (object):
    def __init__(self):
        self.x = 300
        self.y = 0
        self.width = 32
        self.height = 32
        self.velocity = 100
        self.Apple = pygame.image.load(os.path.join(r"D:\Users\User\Documents\My python programs\Pygames\1stGame", "Apple.png"))
        self.AppleRect = self.Apple.get_rect()
        self.CollisionFound = False
        self.Score = 0
        self.CollectSound = mixer.music.load(r"D:\Users\User\Documents\My python programs\Collect.wav")




    def Draw (self, Window):
        Window.blit(self.Apple, (self.x, self.y))
        

    def Up (self):
        if self.y > 500 or self.CollisionFound == True:
            self.y = -100
            self.x = randint(50, 450)
            self.CollisionFound = False

    def Collision (self):
        #-------Collision-------
        if self.AppleRect.colliderect(PlayerInstance.PlayerRect):

            time.sleep(0.1)
            mixer.music.play()
            self.CollisionFound = True
            self.Score += 1
    
    def AppleUpdate (self):
        #-------Collision-------
        if self.CollisionFound == False:
            AppleInstance.y += AppleInstance.velocity * dt
        
        #-------Change Apple Rect position-------
        AppleInstance.AppleRect.x = AppleInstance.x
        AppleInstance.AppleRect.y = AppleInstance.y

        #-------Call Functions-------
        AppleInstance.Collision()
        AppleInstance.Draw(Window)
        AppleInstance.Up()


class Score (object):   
    def __init__(self):
        self.Score = pygame.font.SysFont("Verdana", 36)

    def ShowText(self):
        ScoreFinal = self.Score.render("Score: " + str(AppleInstance.Score), 50, (0, 0, 0))
        Window.blit(ScoreFinal, (25, 25))







PlayerInstance = Player()
AppleInstance = Apple()
prev_time = time.time()
ScoreInstance = Score()
runnin = True

#-------EVENT LOOP-------
while runnin:


    Window.fill((141, 165, 204))
    now = time.time()
    dt = now - prev_time
    prev_time = now
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False

     #-------Input-------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and PlayerInstance.x < 500 - PlayerInstance.width:
        PlayerInstance.x += PlayerInstance.vel * dt
    if keys[pygame.K_LEFT] and PlayerInstance.x > 0:
        PlayerInstance.x -= PlayerInstance.vel * dt

    #-------Call Main Classes/Update-------
    AppleInstance.AppleUpdate()
    PlayerInstance.PlayerUpdate()
    ScoreInstance.ShowText()

    
    #-------UpdateWindow-------
    pygame.display.update()


