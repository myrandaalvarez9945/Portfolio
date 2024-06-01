# This one is pretty simple and good for intermediate projects.
# I did this because I want to see the levels of the sound that
# I am listening to. It does show a visualization which is cool.

import pygame
import numpy as np
import pyaudio
import struct
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BAR_WIDTH = 10
NUM_BARS = WIDTH // BAR_WIDTH
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Visualizer")
clock = pygame.time.Clock()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def get_audio_data():
    data = stream.read(CHUNK, exception_on_overflow=False)
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    data_np = np.array(data_int, dtype='b')[::2] + 128
    return data_np - 128

def draw_bars(screen, data):
    screen.fill(BLACK)
    bar_height = np.abs(data) // 4
    for i in range(NUM_BARS):
        color = (int(bar_height[i] * 2), 255 - int(bar_height[i] * 2), 100)
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT // 2 - bar_height[i], BAR_WIDTH, bar_height[i] * 2))
    pygame.display.flip()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        audio_data = get_audio_data()
        draw_bars(screen, audio_data)
        clock.tick(FPS)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()