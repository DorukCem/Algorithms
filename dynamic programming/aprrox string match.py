#Levenshtein distance
def recursive(s1, s2):
   if s1 == "":
      return len(s2)
   if s2 == "":
      return len(s1)
   
   if s1[0] == s2[0]: 
      return recursive(s1[1:], s2[1:])         # heads match, just move forward
   
   # Heads do not match, we need to edit 
   return 1 + min( recursive( s1[1:], s2    ), # remove letter
                   recursive( s1,     s2[1:]), # add letter
                   recursive( s1[1:], s2[1:])  # replace letter
                  )
# The recursive approach can be easlily improved by caching the results

# This approach is very similar to the recursive approach.
# Instead of removing parts of the string with each step,
# we simply maintain pointers to track our progress.
def pointers(s1, s2, p1 = None, p2 = None):
   if p1 == None: p1, p2 = len(s1), len(s2) 

   if p1 == 0: return p2
   if p2 == 0: return p1

   if s1[p1-1] == s2[p2-1]:
      return pointers(s1, s2, p1-1, p2-1)
   
   return 1 + min( pointers( s1, s2, p1-1, p2),   # remove letter
                   pointers( s1, s2, p1,   p2-1), # add letter
                   pointers( s1, s2, p1-1, p2-1)  # replace letter
                  )

# dynamic programming approach
def dp(s1, s2):
   if s1 == "": return len(s2)
   if s2 == "": return len(s1)

   p1, p2 = len(s1), len(s2)
   cache = [[0]*p2 for _ in range(p1)]

   for i in range(p1):
      cache[i][0] = i
   
   for j in range(p2):
      cache[0][j] = j
   
   for j in range(p2):
      for i in range(p1):
         if s1[i] == s2[j]:
            continue

         cache[i][j] = 1 + min(cache[i-1][j],
                               cache[i][j-1],
                               cache[i-1][j-1])
   return cache[p1-1][p2-1]

print(dp("foo", "bar"))
print(dp("apple", "dapple"))
print(dp("apple", "le"))
print(dp("sky", "dye"))
print(dp("", "b"))
print(dp("a", ""))
print(dp("", ""))
