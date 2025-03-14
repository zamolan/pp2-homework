import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

x = 25
y = 25

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - 20 >= 25: y -= 20
        elif pressed[pygame.K_DOWN] and y + 20 <= 300 - 25: y += 20
        elif pressed[pygame.K_LEFT] and x - 20 >= 25: x -= 20
        elif pressed[pygame.K_RIGHT] and x + 20 <= 400 - 25: x += 20

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255,0,0), (x, y), 25)
        
        pygame.display.flip()

        clock.tick(40)