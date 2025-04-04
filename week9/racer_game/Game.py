# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Set up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen and game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create game window
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

COINS_COLLECTED = 0

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin class with random weights and colors
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10
        self.weight = random.choice([1, 2, 5])
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        if self.weight == 1:
            color = (255, 215, 0)   # Standard gold
        elif self.weight == 2:
            color = (255, 165, 0)   # Darker gold
        else:
            color = (255, 255, 0)   # Lighter gold

        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT // 2))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_pos()

    def reset_pos(self):
        self.weight = random.choice([1, 2, 5])
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        if self.weight == 1:
            color = (255, 215, 0)
        elif self.weight == 2:
            color = (255, 165, 0)
        else:
            color = (255, 255, 0)

        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)

# Create player and enemy
P1 = Player()
E1 = Enemy()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Create coin and add to groups
coin = Coin()
coins = pygame.sprite.Group()
coins.add(coin)
all_sprites.add(coin)

# Timer event to gradually increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Show score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Update and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check coin collection
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COINS_COLLECTED += coin.weight
            pygame.mixer.Sound('coin.wav').play()
            coin.reset_pos()

            # Increase speed every 5 coins
            if COINS_COLLECTED % 5 == 0:
                SPEED += 1

    # Display collected coins
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Check collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
