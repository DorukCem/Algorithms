# is num a passable answer for the given row and column  
def is_valid(board, num, row, col):
   for y in range(len(board)):
      if board[row][y] == num:
         return False
      
   for x in range(len(board)):
      if board[x][col] == num:
         return False
      
      row_blocK_start = (row//3) * 3
      col_block_start = (col//3) * 3

      for i in range(row_blocK_start, row_blocK_start+3):
         for j in range(col_block_start, col_block_start+3):
            if board[i][j] == num:
               return False
   
   return True

# find the next empty tile
def find_empty(board):
   for row in range(9):
      for col in range(9):
         if board[row][col] == 0 :
            return row,col
   return None

def allowed_values(board, row, col):

   row_values = set( board[row] )
   col_values = set([ board[i][col] for i in range(9)])

   row_blocK_start = (row//3) * 3
   col_block_start = (col//3) * 3
   
   block_values = { board[i][j] for i in range(row_blocK_start, row_blocK_start + 3) for j in range(col_block_start, col_block_start + 3)}
    
   all_values = row_values | col_values | block_values
   return [num for num in range(1, 10) if num not in all_values]
 

def cache_valid_values(board):
   cache = dict()

   for i in range(9):
      for j in range(9):
         if board[i][j] == 0:
            cache[ (i, j) ] = allowed_values(board, i, j)
   return cache

def ordered_valid_valus(board, cache):
   pass

def solve(board):
   empty_tile = find_empty(board)
   if empty_tile == None:
      return True
   else:
      row, col = empty_tile

   for num in range(1, 10):
      if is_valid(board, num, row, col):
         board[row][col] = num

         if solve(board):
            return True
          
         # If this num is not the answer we erase it
         board[row][col] = 0
   
   return False

def solve_with_cache(board, cache):
   empty_tile = find_empty(board)
   if empty_tile == None:
      return True
   else:
      row, col = empty_tile

   for num in cache[(row,col)]:
      if is_valid(board, num, row, col):
         board[row][col] = num

         if solve_with_cache(board, cache):
            return True
          
         # If this num is not the answer we erase it
         board[row][col] = 0
   
   return False