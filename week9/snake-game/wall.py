import pygame
from game_object import GameObject 
from game_object import Point 

class Wall(GameObject):
    def __init__(self, tile_width):
        super().__init__([], tile_width)  # Initialize parent class
        self.level = 0  # Start at level 0
        self.load_level()  # Load the current level

    def load_level(self):
        """Load the wall layout from a file"""
        self.points = []  # Clear previous points
        with open(f"levels/level{self.level}.txt", "r") as f:
            for row, line in enumerate(f):
                for col, c in enumerate(line.strip()):  # Remove extra spaces
                    if c == '#':  # Wall block found
                        self.points.append(Point(col * self.tile_width, row * self.tile_width))

    def next_level(self):
        """Move to the next level or exit the game"""
        if self.level < 2:  # If not the last level
            self.level += 1
            self.load_level()  # Load the next level
        else:
            pygame.quit()  # Exit the game if it's the last level
            exit()

    def hit_wall(self, head_location):
        """Check if the worm hits the wall"""
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:  # Collision detected
                result = point
                break
        return result
