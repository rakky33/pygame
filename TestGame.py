import pygame
pygame.init()

#WindowWidth = 
Display = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 450
y = 450
width = 40
height = 40
vel = 5

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if not x <= 0:
            x -= vel

    if keys[pygame.K_d]:
        if x <= 455: #X-50
            x += vel


    if keys[pygame.K_s]:
        if y <= 455: #Y-5
            y += vel

    if y < 460: #Y-40
        y += vel
    elif keys[pygame.K_w]:
        if not y <= 0:
                y -= 150
    
    print(f"x: {x},y: {y}")
    Display.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(Display, (255,197,60), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()