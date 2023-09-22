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
   numbers = []
   
   for num in range(1, 10):
      found = False
      
      # Check if all row elements include this number
      for j in range(9):
         if board[row][j] == num:
            found = True
            break
      # Check if all column elements include this number
      if found == True:
         continue
      else:
         for i in range(9):
            if board[i][col] == num:
               found = True
               break

      # Check if the number is already included in the block
      if found == True:
            continue
      else:
         row_blocK_start = (row//3) * 3
         col_block_start = (col//3) * 3

         for i in range(row_blocK_start, row_blocK_start+3):
            for j in range(col_block_start, col_block_start+3):
               if board[i][j] == num:
                  found = True
                  break
      
      if found == False:
            numbers.append(num)

   return numbers
    

def cache_valid_values(board):
   cache = dict()

   for i in range(9):
      for j in range(9):
         if board[i][j] == 0:
            cache[ (i, j) ] = allowed_values(board, i, j)
   return cache

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