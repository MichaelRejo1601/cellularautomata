import pygame

def initGrid(SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT, BLOCKSIZE, COLOR):
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, COLOR, rect, 1)