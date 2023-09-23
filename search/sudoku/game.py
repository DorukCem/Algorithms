import pygame
from solver import *
from sys import exit
import time

NUM_SQUARES = 9
SQUARE_SIZE = 60
BIG_SQUARE_SIZE = SQUARE_SIZE * 3
WIDTH = HEIGHT = NUM_SQUARES * SQUARE_SIZE

pygame.init()
screen = pygame.display.set_mode(( WIDTH ,  HEIGHT ))
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)

def draw_lines(screen):
   for x in range(0, WIDTH, SQUARE_SIZE):
      for y in range(0, HEIGHT, SQUARE_SIZE):
         rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
         pygame.draw.rect(screen, BLACK, rect, 1)

   for x in range(0, WIDTH, BIG_SQUARE_SIZE):
      for y in range(0, HEIGHT, BIG_SQUARE_SIZE):
         rect = pygame.Rect(x, y, BIG_SQUARE_SIZE, BIG_SQUARE_SIZE)
         pygame.draw.rect(screen, BLACK, rect, 2)

FONT = pygame.font.Font(None, 45)
def draw_board(screen, board):
   for x in range(0, NUM_SQUARES):
      for y in range(0, NUM_SQUARES):
         text = str(board[y][x]) if board[y][x] else ""
         position = (x*SQUARE_SIZE + SQUARE_SIZE//2 , y*SQUARE_SIZE + SQUARE_SIZE//2)
         text_obj = FONT.render(text, True, BLACK)
         text_rect = text_obj.get_rect(center=position)
         screen.blit(text_obj, text_rect)

board = [
   [0,0,0, 0,0,0, 0,1,2],
   [0,0,0, 0,3,5, 0,0,0],
   [0,0,0, 6,0,0, 0,7,0],

   [7,0,0, 0,0,0, 3,0,0],
   [0,0,0, 4,0,0, 8,0,0],
   [1,0,0, 0,0,0, 0,0,0],

   [0,0,0, 1,2,0, 0,0,0],
   [0,8,0, 0,0,0, 0,4,0],
   [0,5,0, 0,0,0, 6,0,0],
]

start = time.time()
 
solve_with_cache(board)
 
# record end time
end = time.time()
print("The time of execution of above program is :",
   (end-start) , "seconds")

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()

   screen.fill( WHITE )
   draw_lines(screen)
   draw_board(screen, board)

   pygame.display.update()
