import pygame
from game_object import GameObject 
from game_object import Point 

class Worm(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(0, 0)], tile_width)  # Initialize the worm at (0, 0)
        self.start_position()  # Set worm to the starting position

    def start_position(self):
        """Set the worm to its initial state"""
        self.points = [Point(0, 0)]  # Start with a single segment
        self.DX = 0  # No horizontal movement
        self.DY = 0  # No vertical movement
        self.score = 0  # Score starts at 0

    def move(self):
        """Move the worm based on its direction"""
        # Move all segments to the position of the segment in front of them
        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        # Move the head of the worm based on direction
        self.points[0].X += self.DX * self.tile_width
        self.points[0].Y += self.DY * self.tile_width

    def increase(self, pos):
        """Add a new segment to the worm at the given position"""
        self.points.append(Point(pos.X, pos.Y))

    def process_input(self, events):
        """Process player input for movement"""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.DX = 0
                    self.DY = -1  # Move up
                elif event.key == pygame.K_DOWN:
                    self.DX = 0
                    self.DY = 1  # Move down
                elif event.key == pygame.K_RIGHT:
                    self.DX = 1
                    self.DY = 0  # Move right
                elif event.key == pygame.K_LEFT:
                    self.DX = -1
                    self.DY = 0  # Move left
                
        # Handle screen boundaries (wrap the worm around the screen)
        if self.points[0].X >= 800:
            self.points[0].X = 0  # Wrap around to the left
        if self.points[0].Y >= 600:
            self.points[0].Y = 0  # Wrap around to the top
        if self.points[0].X < 0:
            self.points[0].X = 800  # Wrap around to the right
        if self.points[0].Y < 0:
            self.points[0].Y = 600  # Wrap around to the bottom
