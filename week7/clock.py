import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock Simulation")

background = pygame.image.load('clock.png')
im_min = pygame.image.load('min_hand.png')
im_sec = pygame.image.load('sec_hand.png')

current_time = 0  
start_ticks = pygame.time.get_ticks()

def blitRotate(surf, image, pos, originPos, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, rotated_rect.topleft)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_time += 60
            elif event.key == pygame.K_DOWN:
                current_time -= 60
            elif event.key == pygame.K_RIGHT:
                current_time += 1
            elif event.key == pygame.K_LEFT:
                current_time -= 1

    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
    total_time = current_time + elapsed_time

    seconds = total_time % 60
    minutes = (total_time // 60) % 60

    sec_angle = (seconds / 60) * 360
    min_angle = (minutes / 60) * 360

    screen.blit(background, (0, 0))

    pos = (screen.get_width() / 2, screen.get_height() / 2)

    blitRotate(screen, im_min, pos, (im_min.get_width() / 2, im_min.get_height() / 2), min_angle)
    blitRotate(screen, im_sec, pos, (im_sec.get_width() / 2, im_sec.get_height() / 2), sec_angle)

    pygame.display.flip()

pygame.quit()
