import sys
import pygame
from settings import Settings
from cell import Cell
import util

def run_game():
 # Initialize game and create a screen object.
    pygame.init()
    
    clock = pygame.time.Clock() 
    
    all_sprites_list = pygame.sprite.Group()
    settings = Settings()
    
    arr = [ [ 0 for i in range(settings.HEIGHT) ] for j in range(settings.WIDTH) ]
    x = round(settings.WIDTH/2)
    y = round(settings.HEIGHT/2)
    # arr[x-1][y] = 1
    # arr[x+1][y] = 1
    # arr[x][y-1] = 1
    # arr[x][y+1] = 1
    # arr[x][y] = 1

    print("Starting")
        
    screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    
    pygame.display.set_caption("Cellular")
    
    cell = Cell(screen)
    all_sprites_list.add(cell)
    play = False
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    print("Pause") if play else print("Resume")
                    play = not play
            # Make the most recently drawn screen visible.
        if play:
            screen.fill(settings.WHITE)
            util.initGrid(screen, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.BLOCKSIZE, settings.BLACK)
            new_arr = [ [ None for i in range(settings.HEIGHT) ] for j in range(settings.WIDTH) ]
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    moore = [-1]*8
                    von = [-1]*4
                    top_edge = j <= 0 
                    bottom_edge = j >= settings.HEIGHT - 1
                    left_edge = i <= 0 
                    right_edge = i >= settings.WIDTH - 1
                    # print(top_edge)
                    # print(bottom_edge)
                    # print(left_edge)
                    # print(right_edge)
                    # print(i)
                    # print(j)
                    moore[0] = arr[i-1 if not left_edge else settings.WIDTH-1][j-1 if not top_edge else settings.HEIGHT-1]
                    moore[1] = von[0] = arr[i][j-1 if not top_edge else settings.HEIGHT-1]
                    moore[2] = arr[i+1 if not right_edge else 0][j-1 if not top_edge else settings.HEIGHT-1]
                    moore[3] = von[1] = arr[i-1 if not left_edge else settings.WIDTH-1][j]
                    moore[4] = von[2] = arr[i+1 if not right_edge else 0][j]
                    moore[5] = arr[i-1 if not left_edge else settings.WIDTH-1][j+1 if not bottom_edge else 0]
                    moore[6] = von[3] = arr[i][j+1 if not bottom_edge else 0]
                    moore[7] = arr[i+1 if not right_edge else 0][j+1 if not bottom_edge else 0]
                    # print(moore)
                    # print(von)
                    total = sum(moore)
                    rule1 = total >= 2 and total <= 4
                    new_arr[i][j] = 1 if rule1 else 0
                        
            
            for i in range(len(new_arr)):
                for j in range(len(new_arr[i])):
                    if new_arr[i][j] == 1:
                        pygame.draw.rect(screen, settings.REDS[39], pygame.Rect(i*settings.BLOCKSIZE, j*settings.BLOCKSIZE, settings.BLOCKSIZE, settings.BLOCKSIZE))
            
            arr = new_arr
            
            pygame.display.flip()
            clock.tick(4)
run_game()
