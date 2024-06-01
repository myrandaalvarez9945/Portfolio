# This one took a minute because it takes a lot. I did use chatGPT for
# some explanations, not going to lie, because look at the A* algorithm. 
# But, anyways, you can press the spacebar to see how the maze is working.


import pygame
import random
import heapq
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (192, 192, 192)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")

# Maze generation using Recursive Backtracking
def generate_maze(rows, cols):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    stack = []
    visited = set()

    def visit_cell(x, y):
        stack.append((x, y))
        visited.add((x, y))

    def get_neighbors(x, y):
        neighbors = []
        if x > 0: neighbors.append((x - 1, y))
        if x < cols - 1: neighbors.append((x + 1, y))
        if y > 0: neighbors.append((x, y - 1))
        if y < rows - 1: neighbors.append((x, y + 1))
        return neighbors

    def remove_wall(x1, y1, x2, y2):
        if x1 == x2:
            maze[max(y1, y2)][x1] = 1
        if y1 == y2:
            maze[y1][max(x1, x2)] = 1

    start_x, start_y = 0, 0
    visit_cell(start_x, start_y)

    while stack:
        x, y = stack[-1]
        neighbors = [n for n in get_neighbors(x, y) if n not in visited]
        if neighbors:
            next_x, next_y = random.choice(neighbors)
            visit_cell(next_x, next_y)
            remove_wall(x, y, next_x, next_y)
        else:
            stack.pop()

    return maze

# Pathfinding using A* Algorithm
def astar(maze, start, end):
    def h(pos):
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h(start)}
    open_set_hash = {start}

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        _, current = heapq.heappop(open_set)
        open_set_hash.remove(current)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < COLS and 0 <= neighbor[1] < ROWS and maze[neighbor[1]][neighbor[0]] == 1:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + h(neighbor)
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)

        # Draw current state
        draw_maze(maze, path=[], open_set_hash=open_set_hash, current=current)
        pygame.display.update()
        pygame.time.delay(50)

    return []

# Draw the maze
def draw_maze(maze, path=None, open_set_hash=None, current=None):
    screen.fill(BLACK)
    for y in range(ROWS):
        for x in range(COLS):
            color = WHITE if maze[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GREY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    if open_set_hash:
        for node in open_set_hash:
            pygame.draw.rect(screen, BLUE, (node[0] * CELL_SIZE, node[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if current:
        pygame.draw.rect(screen, RED, (current[0] * CELL_SIZE, current[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if path:
        for x, y in path:
            pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()

def main():
    maze = generate_maze(ROWS, COLS)
    start = (0, 0)
    end = (COLS - 1, ROWS - 1)

    running = True
    solving = False
    path = []
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving = True

        if solving:
            path = astar(maze, start, end)
            solving = False

        draw_maze(maze, path)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()