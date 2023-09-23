from collections import Counter

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


# Sort the lists in the cache 
# ordering the lists of legitimate values for each cell by chance of prevelance, thus the numbers 
# with lower frequency of appearance in the row cells will be more likely to be the correct options
# -----
# For example: 
#  We can put 6 in two squares validly, 1 in four squares, and 7 in ten squares.
#  In that case 6 is more likely to be the correct option for a square that has the options [7, 6, 1]
#  In tha case we must order the list of valid values for that square as : [ 6, 1, 7 ] 
def ordered_valid_valus(board, cache):
   
   # Create dictionaries to store the frequency of values in rows, columns, and blocks
   global_frequencies = {}
   row_frequencies = [Counter() for _ in range(9)]
   col_frequencies = [Counter() for _ in range(9)]
   block_frequencies = [Counter() for _ in range(9)]
   
   # Iterate through rows and columns to count the appearance of values
   for row in range(9):
      for col in range(9):
         if (row, col) in cache:
            for value in cache[(row, col)]:
               # Update row, column, and block frequencies
               global_frequencies[value] = global_frequencies.get(value, 0) + 1
               row_frequencies[row][value] = row_frequencies[row].get(value, 0) + 1
               col_frequencies[col][value] = col_frequencies[col].get(value, 0) + 1
               block_id = (row // 3) * 3 + (col // 3)
               block_frequencies[block_id][value] = block_frequencies[block_id].get(value, 0) + 1


   # Reorder the values in each cell based on their frequency
   for (row, col) in cache:
      cache[(row, col)] = sorted(cache[(row, col)], key=lambda x: global_frequencies.get(x, 0))

   # If there is only one possible place where the value can be put, put it there 
   for (row, col) in cache:
      block_id = (row // 3) * 3 + (col // 3)
      for value in cache[(row, col)]:
         if row_frequencies[row][value] == 1 or col_frequencies[col][value] == 1 or block_frequencies[block_id][value] == 1:
            board[row][col] = value

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