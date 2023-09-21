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

def find_empty(board):
   for row in range(9):
      for col in range(9):
         if board[row][col] == 0 :
            return row,col
   return None


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