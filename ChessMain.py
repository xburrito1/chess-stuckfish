"""
This is our main driver file. It will be responsive for handling user input and displaying the current GameState object.
"""

import pygame as p
import ChessEngine

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
COLORS = [p.Color("#F0D9B5"), p.Color("#946f51")]

"""
Initialize a global dictionary of images. This will be called exactly once in the main
"""
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

"""
Handle user input and updating the graphics
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    cloack = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        cloack.tick(MAX_FPS)
        p.display.flip()


"""
Responsible for all the graphics within a current game state.
"""
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

"""
Draw the squares of the board, always call drawBoard() before draw pieces or will overlap.
The top left square is always light.
"""
def drawBoard(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = COLORS[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            



"""
Draw the pieces on the board using the current GameState.board
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    

if __name__ == "__main__":
    main()