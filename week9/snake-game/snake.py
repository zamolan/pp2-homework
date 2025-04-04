import pygame
from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall


def create_background(screen, width, height):
    screen.fill((224, 238, 205))
    tile_width = 50
    y = -1
    while y < height:
        x = -1
        while x < width:
            row = y // tile_width
            col = x // tile_width
            # Draw grid tiles for the background
            pygame.draw.rect(screen, (95, 95, 95), pygame.Rect(x, y, 3, 3))
            x += tile_width
        y += tile_width

def draw_score(screen, score):
    text = font.render(f"Score:{score}", True, (231, 71, 113))
    screen.blit(text, (615, 10))

done = False

pygame.init()
pygame.font.init()
font = pygame.font.Font("fonts/GameBoy.ttf", 20)
font1 = pygame.font.Font("fonts/GameBoy.ttf", 36)
font0 = pygame.font.Font("fonts/GameBoy.ttf", 21)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
clock_time = 3

# Initialize game objects
worm = Worm(50)
food = Food(50)
wall = Wall(50)

while not done:
    # Event filtering to prevent unwanted events
    filtered_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)

    worm.process_input(filtered_events)
    worm.move()

    # Check if worm hits the wall and restart if so
    pos = wall.hit_wall(worm.points[0])
    if pos != None:
        text = font1.render("Restarting...", True, (231, 71, 113))
        screen.blit(text, (200, 250))
        pygame.display.flip()  # Update the screen before delay
        pygame.time.delay(1000)  # Wait for 1 second before restarting
        worm.start_position()

    # Check if worm eats food and update score
    pos = food.can_eat(worm.points[0])
    if pos != None:
        worm.score += [10, 20, 50][food.food_type]  # Add score based on food type
        worm.increase(pos)  # Increase the worm's length
        if worm.score >= 150:
            done = True  # End the game if score is 150
        elif worm.score >= 100 and wall.level == 1:
            text = font1.render("Next level", True, (231, 71, 113))
            screen.blit(text, (250, 250))
            pygame.display.flip()  # Update screen to show text

            pygame.time.delay(2000)  # Wait for 2 seconds

            wall.next_level()  # Move to the next level
            worm.score = 0  # Reset score
            clock_time += 0.5  # Increase game speed
            worm.start_position()

        elif worm.score >= 50 and wall.level == 0:
            text = font1.render("Next level", True, (231, 71, 113))
            screen.blit(text, (250, 250))
            pygame.display.flip()  # Update screen to show text

            pygame.time.delay(2000)  # Wait for 2 seconds

            wall.next_level()  # Move to the next level
            worm.score = 0  # Reset score
            clock_time += 0.5  # Increase game speed
            worm.start_position()

        food.new_food(worm, wall)  # Spawn new food

    # Add logic for timed food
    food.spawn_time_food(worm, wall)  # Spawn timed food every 20 seconds
    food.check_time_food_expiration()  # Remove timed food after 10 seconds
    food.check_time_food_eaten(worm)  # Check if worm eats the timed food

    create_background(screen, 800, 600)  # Draw the game background
    
    # Draw game objects (worm, food, walls)
    worm.draw_worm(screen)
    food.draw_food(screen)
    wall.draw_wall(screen)

    food.draw_time_food(screen)  # Draw the timed food if active

    draw_score(screen, worm.score)  # Draw the score on the screen

    pygame.display.flip()  # Update the screen
    clock.tick(clock_time)  # Control game speed