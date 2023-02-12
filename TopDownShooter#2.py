#import libraly
import pygame
import math
import random
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
PlayerScale=50
BulletVel = 20
B_radius = 5

#Load Texture
Flower1 = pygame.image.load('flowers/064.png')
Flower1 = pygame.transform.scale(Flower1,(FlowerScale,FlowerScale))

Flower2 = pygame.image.load('flowers/065.png')
Flower2 = pygame.transform.scale(Flower2,(FlowerScale,FlowerScale))

Flower3 = pygame.image.load('flowers/066.png')
Flower3 = pygame.transform.scale(Flower3,(FlowerScale,FlowerScale))

player_run_right = [pygame.image.load('Character\RUN1.png'),pygame.image.load('Character\RUN2.png'),pygame.image.load('Character\RUN3.png'),pygame.image.load('Character\RUN4.png')]
player_run_right = [pygame.transform.scale(sprite,(70,70)) for sprite in player_run_right]

player_run_left = [pygame.image.load('Character\RUN1.png'),pygame.image.load('Character\RUN2.png'),pygame.image.load('Character\RUN3.png'),pygame.image.load('Character\RUN4.png')]
player_run_left = [pygame.transform.scale(sprite,(70,70)) for sprite in player_run_left]
player_run_left = [pygame.transform.flip(sprite,True,False) for sprite in player_run_left]

player_idle = pygame.image.load('Character\IDLE.png')
player_idle = pygame.transform.scale(player_idle,(70,70))

player_weapon = pygame.image.load('Gun.png').convert()
player_weapon = pygame.transform.scale(player_weapon,(30,30))
player_weapon.set_colorkey((0,0,0))

#Player Class
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_left = False
        self.moving_right = False
        self.moving_Y = False
        self.Player_idle = True
    def handle_weapon(self,display):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y =mouse_x - player.x , mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_y)

        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)

        display.blit(player_weapon_copy,(self.x+15-int(player_weapon_copy.get_width()/2), self.y + 25 - int(player_weapon_copy.get_height()/2)))

    def main(self, display):
        if self.animation_count +1 >= 16:
            self.animation_count = 0

        self.animation_count += 1
        
        if player.moving_left == True:
            display.blit(player_run_left[self.animation_count//4], (self.x,self.y))
        elif player.moving_right == True:
            display.blit(player_run_right[self.animation_count//4], (self.x,self.y))
        elif player.moving_Y == True:
            if player.moving_left == True:
                display.blit(player_run_left[self.animation_count//4], (self.x,self.y))
            elif player.moving_right == True:
                display.blit(player_run_right[self.animation_count//4], (self.x,self.y))
        elif player.Player_idle == True:
            display.blit(player_idle,(self.x,self.y))

        self.handle_weapon(display)

        #pygame.draw.rect(display , (255,255,255) , (self.x, self.y, self.width, self.height))

#BulletClass
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

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_image = [pygame.image.load('Character\RUN1.png'),pygame.image.load('Character\RUN2.png'),pygame.image.load('Character\RUN3.png'),pygame.image.load('Character\RUN4.png')]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-300,300)
        self.offset_y = random.randrange(-300,300)
    def main(self,display):
        if self.animation_count +1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-300,300)
            self.offset_y = random.randrange(-300,300)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1

        if player.x + self.offset_x > self.x - display_scroll[0]:
            self.x += 1
        elif player.x + self.offset_x < self.x - display_scroll[0]:
            self.x -= 1

        if player.x + self.offset_y > self.y - display_scroll[1]:
            self.y += 1
        elif player.y + self.offset_x < self.y - display_scroll[1]:
            self.y -= 1

        display.blit(pygame.transform.scale(self.animation_image[self.animation_count//4], (32,30)), (self.x-display_scroll[0], self.y-display_scroll[1]))

enemies = [Enemy(400,300)]

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
                pygame.time.delay(100)

    #Background object that will move when u walk
    display.blit(Flower1,(100-display_scroll[0],100-display_scroll[1]))
    display.blit(Flower2,(213-display_scroll[0],310-display_scroll[1]))
    display.blit(Flower3,(500-display_scroll[0],20-display_scroll[1]))
    
    
    #Controller
    if keys[pygame.K_a]:
        display_scroll[0] -= speed
        player.moving_left = True
        player.moving_right = False
        player.moving_Y = False
        player.Player_idle = False
        for bullet in player_bullets:
            bullet.x += speed
    if keys[pygame.K_d]:
        display_scroll[0] += speed
        player.moving_right = True
        player.moving_left = False
        player.moving_Y = False
        player.Player_idle = False
        for bullet in player_bullets:
            bullet.x -= speed
    if keys[pygame.K_w]:
        display_scroll[1] -= speed
        player.moving_Y = True
        player.Player_idle = False
        for bullet in player_bullets:
            bullet.y += speed
    if keys[pygame.K_s]:
        display_scroll[1] += speed
        player.moving_Y = True
        player.Player_idle = False
        for bullet in player_bullets:
            bullet.y -= speed
            
    player.main(display)

    for bullets in player_bullets:
        bullets.main(display)

    for enemy in enemies:
        enemy.main(display)
    #print(event)
    clock.tick(FPS)
    pygame.display.update()

pygame.quit