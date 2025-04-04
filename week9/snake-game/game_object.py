import pygame
import random
import time

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        
class GameObject:
    def __init__(self, points, tile_width):
        self.wall_image = pygame.image.load("pictures/wall.png")
        self.wormh_image = pygame.image.load("pictures/head.png")
        self.wormt_image = pygame.image.load("pictures/tail.png")
        self.food_images = [
            pygame.image.load("pictures/food10.png"),
            pygame.image.load("pictures/food20.png"),
            pygame.image.load("pictures/food50.png")]
        
        self.food_type = random.randint(0, 2)

        self.food_time = pygame.image.load("pictures/food30.png")
        self.time_food_active = False
        self.time_food_start = 0
        self.food_time_position = None
        self.last_time_food_spawn = time.time()

        self.points = points
        self.tile_width = tile_width
   
    def draw_wall(self, screen):
        for point in self.points:
            screen.blit(self.wall_image, (int(point.X) - 2, int(point.Y) - 8))

    def draw_worm(self, screen):
        for i, point in enumerate(self.points):
            if i == 0:
                screen.blit(self.wormh_image, (point.X, point.Y))
            else:
                screen.blit(self.wormt_image, (point.X, point.Y))

    def draw_food(self, screen):
        for point in self.points:
            screen.blit(self.food_images[self.food_type], (point.X, point.Y))

    def new_food(self, worm, wall):
        while True:
            x = random.randint(0, 15) * self.tile_width
            y = random.randint(0, 11) * self.tile_width

            # Make sure food doesn't spawn on the wall or the snake
            if all(p.X != x or p.Y != y for p in wall.points) and \
               all(p.X != x or p.Y != y for p in worm.points):
                self.points = [Point(x, y)]
                self.food_type = random.randint(0, 2)
                break

    def spawn_time_food(self, worm, wall):
        current_time = time.time()

        # Spawn timed food every 20 seconds if not already active
        if not self.time_food_active and current_time - self.last_time_food_spawn >= 20:
            while True:
                x = random.randint(0, 15) * self.tile_width
                y = random.randint(0, 11) * self.tile_width

                if all(p.X != x or p.Y != y for p in wall.points) and \
                   all(p.X != x or p.Y != y for p in worm.points):
                    self.food_time_position = Point(x, y)
                    self.time_food_start = current_time
                    self.time_food_active = True
                    self.last_time_food_spawn = current_time
                    break

    def draw_time_food(self, screen):
        if self.time_food_active and self.food_time_position:
            screen.blit(self.food_time, (self.food_time_position.X, self.food_time_position.Y))

    def check_time_food_expiration(self):
        # Remove timed food if 10 seconds have passed
        if self.time_food_active and time.time() - self.time_food_start >= 10:
            self.time_food_active = False

    def check_time_food_eaten(self, worm):
        # Check if the snake eats the timed food
        if self.time_food_active and \
           worm.points[0].X == self.food_time_position.X and \
           worm.points[0].Y == self.food_time_position.Y:
            worm.score += 30
            self.time_food_active = False
