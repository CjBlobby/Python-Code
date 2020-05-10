import pygame

pygame.init()



white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((1000, 800))

pixellist = pygame.PixelArray(screen)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(black)
    #DRAWING SHAPES

    #pixellist[x][y] = (colour)
    pixellist[10][10] = (green)
    #pygame.draw.line(screen, colour, startcoord, endcoord, thickness)
    pygame.draw.line(screen, green, (100, 100), (200, 200), 10)
    #pygame.draw.rect(screen, colour, (x, y, width, height))
    pygame.draw.rect(screen, green, (500, 600, 30, 60))
    #pygame.draw.circle(screen, colour, centre, radius)
    pygame.draw.circle(screen, green, (200, 400), 30)
    #pygame.draw.polygon(screen, colour, (coords of points))
    pygame.draw.polygon(screen, green, ((13, 400), (47, 500), (800, 700), (0, 450)))

    
    pygame.display.update()
    
