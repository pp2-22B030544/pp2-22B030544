import pygame 

pygame.init()

height , width = 500 , 500

screen = pygame.display.set_mode((height, width))

run =True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()