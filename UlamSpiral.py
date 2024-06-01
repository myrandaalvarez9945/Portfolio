# We are making UlamSpiral, of course you can change the numbers to dots.
# If you don't know what the UlamSpiral is, please look it up.
# It works the way that I want it to so that is pretty cool.

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SIZE = 600  # Size of the window
GRID_SIZE = 30  # Size of each grid cell
NUM_CELLS = SIZE // GRID_SIZE  # Number of cells per row/column
CENTER = NUM_CELLS // 2  # Center of the grid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT_SIZE = 20
DELAY = 100  # Delay in milliseconds between drawing numbers

# Set up the display
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Ulam Spiral")

# Set up the font
font = pygame.font.SysFont(None, FONT_SIZE)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate the Ulam Spiral
def generate_ulam_spiral(max_num):
    spiral = [[0] * NUM_CELLS for _ in range(NUM_CELLS)]
    x, y = CENTER, CENTER
    spiral[y][x] = 1  # Here we are going to start at the center
    num = 2
    steps = 1

    while num <= max_num:
        for _ in range(steps):
            x += 1
            if num > max_num:
                return spiral
            spiral[y][x] = num
            num += 1
        for _ in range(steps):
            y -= 1
            if num > max_num:
                return spiral
            spiral[y][x] = num
            num += 1
        steps += 1
        for _ in range(steps):
            x -= 1
            if num > max_num:
                return spiral
            spiral[y][x] = num
            num += 1
        for _ in range(steps):
            y += 1
            if num > max_num:
                return spiral
            spiral[y][x] = num
            num += 1
        steps += 1
    return spiral

# Function to draw the Ulam Spiral with numbers
def draw_ulam_spiral(spiral, max_num):
    screen.fill(BLACK)
    for y in range(NUM_CELLS):
        for x in range(NUM_CELLS):
            num = spiral[y][x]
            if num != 0 and num <= max_num:
                color = RED if is_prime(num) else WHITE
                text = font.render(str(num), True, color)
                screen.blit(text, (x * GRID_SIZE + (GRID_SIZE - text.get_width()) // 2, 
                                   y * GRID_SIZE + (GRID_SIZE - text.get_height()) // 2))
    pygame.display.flip()

def main():
    max_num = 50  # You can change this number if you want to
    spiral = generate_ulam_spiral(max_num)
    num = 1

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if num <= max_num:
            draw_ulam_spiral(spiral, num)
            num += 1
            pygame.time.delay(DELAY)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()