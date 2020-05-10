import pygame, random

class Snake():

    x = 10
    y = 10
    size = 1
    bodylist = [(10, 10)]
    head = bodylist[0]
    eaten = False

    def __init__(self, scrsize, gridsize):
        self.scrsize = scrsize
        self.gridsize = gridsize

        
    def grow(self):
        self.size += 1
        self.eaten = True


    def move(self, direction):
        if direction == "Left":
            self.x -= 1
        if direction == "Right":
            self.x += 1
        if direction == "Up":
            self.y -= 1
        if direction == "Down":
            self.y += 1

        self.bodylist.insert(0, (self.x, self.y))

        if not self.eaten:
            del(self.bodylist[-1])
        self.eaten = False


    def dead(self):
        if self.x >= self.scrsize / self.gridsize:
            return True
        if self.x < 0:
            return True
        if self.y >= self.scrsize / self.gridsize:
            return True       
        if self.y < 0:
            return True

        for item in self.bodylist[1::]:
            if item[0] == self.x and item[1] == self.y:
                return True
        return False
    
            
        
        


def grid_draw(screen, colour, scrsize, gridsize, coord):
    x = coord[0] * gridsize
    y = coord[1] * gridsize

    pygame.draw.rect(screen, colour, (x, y, gridsize - 1, gridsize - 1))


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

snake = Snake(800, 20)
direction = "Right"
applex = 30
appley = 30


while snake.dead() == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "Left"
            if event.key == pygame.K_RIGHT:
                direction = "Right"
            if event.key == pygame.K_UP:
                direction = "Up"
            if event.key == pygame.K_DOWN:
                direction = "Down"
            
    snake.dead()

    screen.fill(black)

    snake.move(direction)
    for item in snake.bodylist:
        grid_draw(screen, green, 800, 20, item)

    grid_draw(screen, red, 800, 20, (applex, appley))

    if snake.x == applex and snake.y == appley:
        snake.grow()
        applex = random.randint(0, 39)
        appley = random.randint(0, 39)
     
    pygame.display.update()
    clock.tick(12)
    
print(f'\n\n\n\n\nGame over, you had a score of {snake.size}')

















    
