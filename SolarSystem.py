# Here we are making a solar system that is orbiting the sun.
# We make it using pygame which is very helpful

import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Constants
SUN_POS = (WIDTH // 2, HEIGHT // 2)
SUN_RADIUS = 30
PLANET_RADIUS = 10

# Planet data: (distance from sun, color, orbital speed, initial angle)
PLANETS = [
    (100, BLUE, 0.01, 0),
    (150, RED, 0.008, 0),
    (200, GREEN, 0.006, 0),
    (250, WHITE, 0.004, 0)
]

def draw_planet(pos, color):
    pygame.draw.circle(WIN, color, pos, PLANET_RADIUS)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        WIN.fill(BLACK)
        
        # Draw the sun
        pygame.draw.circle(WIN, YELLOW, SUN_POS, SUN_RADIUS)
        
        for i, (distance, color, speed, angle) in enumerate(PLANETS):
            # Calculate planet position
            angle += speed
            x = SUN_POS[0] + distance * math.cos(angle)
            y = SUN_POS[1] + distance * math.sin(angle)
            PLANETS[i] = (distance, color, speed, angle)  # Update angle

            # Draw the planet
            draw_planet((int(x), int(y)), color)
        
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()