import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLACK
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax

mainClock = pygame.time.Clock()
FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Damas')

title = pygame.font.SysFont(None, 40)
font = pygame.font.SysFont(None, 30)


def getPosMouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj, textrect)




def menu():
    
    

    click = False
    menu = True
    while menu:

        WIN.fill((0,0,0))
        draw_text('Menu Principal', title, (255,255,255), WIN, 300, 50)

        mx, my = pygame.mouse.get_pos()

        two_players = pygame.Rect(300, 200, 200, 50)
        easy = pygame.Rect(300, 300, 200, 50)
        medium = pygame.Rect(300, 400, 200, 50)
        hard = pygame.Rect(300, 500, 200, 50)
        

        pygame.draw.rect(WIN, (135,135,135), two_players)
        pygame.draw.rect(WIN, (135,135,135), easy)
        pygame.draw.rect(WIN, (135,135,135), medium)
        pygame.draw.rect(WIN, (135,135,135), hard)

        draw_text('Dois Jogadores', font, (255,255,255), WIN, 325, 218)
        draw_text('Fácil', font, (255,255,255), WIN, 375, 318)
        draw_text('Médio', font, (255,255,255), WIN, 373, 418)
        draw_text('Difícil', font, (255,255,255), WIN, 373, 518)

        if two_players.collidepoint((mx,my)):
            if click:
                main(0)

        if easy.collidepoint((mx,my)):
            if click:
                main(2)

        if medium.collidepoint((mx,my)):
            if click:
                main(3)

        if hard.collidepoint((mx,my)):
            if click:
                main(4)

        click = False

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(FPS)


def main(game_mode):
    
    
    run = True    
    game = Game(WIN)
    
    while run:
        mainClock.tick(FPS)




        if game_mode != 0:
            if game.turn == BLACK:
                value, new_board = minimax(game.get_board(), game_mode, BLACK, game)
                game.ai_move(new_board)
        



        if game.winner() != None:
            WIN.fill((0,0,0))
            draw_text(game.winner(), title, (255,255,255), WIN, 400, 400)
            pygame.time.delay(2000)
            run = False
            



        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getPosMouse(pos)
                game.select(row,col)
                

        game.update()
  
    
    

menu()