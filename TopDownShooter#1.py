import pygame
import math
pygame.init()

#set Display res
display = pygame.display.set_mode((800,600))
#Set clock
clock = pygame.time.Clock()

#Set Variable
FPS = 60
Running = True
speed = 5
FlowerScale=50
BulletVel = 20
B_radius = 5

#Load Texture
Flower1 = pygame.image.load('flowers/064.png')
Flower1 = pygame.transform.scale(Flower1,(FlowerScale,FlowerScale))

Flower2 = pygame.image.load('flowers/065.png')
Flower2 = pygame.transform.scale(Flower2,(FlowerScale,FlowerScale))

#Display Player Class
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display , (255,255,255) , (self.x, self.y, self.width, self.height))

class PlayerBullet:
    def __init__(self,x,y,mouse_x,mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = BulletVel
        self.ange = math.atan2(y-mouse_y,x-mouse_x)
        self.x_vel = math.cos(self.ange) * BulletVel
        self.y_vel = math.sin(self.ange) * BulletVel
    def main(self,display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, (207, 252, 3), (self.x,self.y) , B_radius)

player = Player(400,300,20,20)

display_scroll = [0,0]

player_bullets = []

while Running:
    #Fill background colour
    display.fill((68, 199, 118))
    mouse_x,mouse_y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("EXIT")
            Running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x,player.y,mouse_x ,mouse_y))

    #Background object that will move when u walk
    display.blit(Flower1,(100-display_scroll[0],100-display_scroll[1]))
    display.blit(Flower2,(213-display_scroll[0],310-display_scroll[1]))
    #pygame.draw.rect(display, (27, 168, 81), (100-display_scroll[0], 100-display_scroll[1], 16,16))
    #pygame.draw.rect(display, (27, 168, 81), (200-display_scroll[0], 230-display_scroll[1], 16,16))
    
    
    #Controller
    if keys[pygame.K_a]:
        display_scroll[0] -= speed
        for bullet in player_bullets:
            bullet.x += speed
    if keys[pygame.K_d]:
        display_scroll[0] += speed
        for bullet in player_bullets:
            bullet.x -= speed
    if keys[pygame.K_w]:
        display_scroll[1] -= speed
        for bullet in player_bullets:
            bullet.y += speed
    if keys[pygame.K_s]:
        display_scroll[1] += speed
        for bullet in player_bullets:
            bullet.y -= speed

    player.main(display)

    for bullets in player_bullets:
        bullets.main(display)

    clock.tick(FPS)
    pygame.display.update()

pygame.quit