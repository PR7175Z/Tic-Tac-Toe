import pygame
import time
pygame.init()

WIDTH, HEIGHT = 600,600
GRIDSIZE = 3
SQSIZE = WIDTH // GRIDSIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Tic-tac-toe')

font = pygame.font.Font(None, 36)

arr = [[None] * GRIDSIZE for _ in range(GRIDSIZE)]
running = True

winner = 0

playerturn = 0
player = ''
ch = 0
def drawgrid():
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            pygame.draw.rect(screen, 'black', (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE), 2)
       
def throwturn():
    if(playerturn%2 == 0):
        ch = 'X'
    else:
        ch = 'O'
    return ch

def welscreen():
    screen.fill((255,255,255))
    weltext = font.render('Play Tic-tac-toe', True, 'black')
    weltext_rect = weltext.get_rect(center = (300,200))
    screen.blit(weltext, weltext_rect)
    presstext = font.render('Press Space to Start...', True, 'black')
    presstext_rect = presstext.get_rect(center = (300, 400))
    screen.blit(presstext, presstext_rect)

def showwin():
    screen.fill((255,255,255))
    ch = throwturn()
    winnertext = font.render(f'{ch} wins', True, 'black')
    winnertext_rect = winnertext.get_rect(center = (300,200))
    screen.blit(winnertext, winnertext_rect)
    presstext = font.render('Press Space to Play Again', True, 'black')
    presstext_rect = presstext.get_rect(center = (300, 400))
    screen.blit(presstext, presstext_rect)

def hasvalerror():
    hasvaltext = font.render('Has Value', True, 'Red')
    hasval_surf = pygame.Surface(hasvaltext.get_size())
    hasval_surf.fill((255,100,100))
    hasval_surf.blit(hasvaltext, (300,300))
    screen.blit(hasval_surf, (300,300))

firstload = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if firstload == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    firstload = 1
        else:
            if winner ==1:
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        winner = 0
                        arr = [[None] * GRIDSIZE for _ in range(GRIDSIZE)]
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // SQSIZE
                    row = y // SQSIZE
                    if arr[row][col] is not None:
                        print('Already occupied!')
                    else:
                        playerturn+=1
                        player = throwturn()
                        arr[row][col] = player
    
    if firstload == 0:
        welscreen()
        # firstload = 1
    else:
        screen.fill('White')

        drawgrid()

        for row in range(GRIDSIZE):
            for col in range(GRIDSIZE):
                if arr[row][col] is not None:
                    text = font.render(arr[row][col], True, 'black')
                    text_rect = text.get_rect(center=(col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2))
                    screen.blit(text, text_rect)

        for h in range(0, 3):
            if(arr[h][0]==arr[h][1]==arr[h][2]=='X' or arr[h][0]==arr[h][1]==arr[h][2]=='O'):
                showwin()
                winner = 1
                break
            elif(arr[0][h]==arr[1][h]==arr[2][h]=='X' or arr[0][h]==arr[1][h]==arr[2][h]=='O'):
                showwin()
                winner = 1
                break
            elif(arr[0][0]==arr[1][1]==arr[2][2]=='X' or arr[0][0]==arr[1][1]==arr[2][2]=='O'):
                showwin()
                winner = 1
                break
            elif(arr[0][2]==arr[1][1]==arr[2][0]=='X' or arr[0][2]==arr[1][1]==arr[2][0]=='O'):
                showwin()
                winner = 1
                break
            else:
                continue

    pygame.display.update()
    clock.tick(60)

pygame.quit()