import pygame
from game_object import GameObject 
from game_object import Point 
from wall import Wall
import random

# Create a Wall object with level 50 (not used in this file directly)
wall = Wall(50)

class Food(GameObject):
    def __init__(self, tile_width):
        # Set initial position of the food
        x, y = 250, 400
        super().__init__([Point(x, y)], tile_width)
    
    def can_eat(self, head_location):
        # Check if the head position matches food position
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
