import pprint
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

   cache = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

   for i in range(len(s1)+1):
      cache[i][0] = i
   
   for j in range(len(s2)):
      cache[0][j] = j

   for i in range(1, len(s1)+1):
      for j in range(1, len(s2)+1):
         if s1[i-1] == s2[j-1]:
            cache[i][j] = cache[i - 1][j - 1]
         else:
            cache[i][j] = 1 + min(cache[i-1][j],  # remove letter
                                 cache[i][j-1],   # add letter
                                 cache[i-1][j-1]  # replace letter
                              )
   
   return cache[len(s1)][len(s2)]

print(dp("foo", "bar"))
print(dp("apple", "dapple"))
print(dp("apple", "le"))
print(dp("sky", "dye"))
print(dp("", "b"))
print(dp("a", ""))
print(dp("", ""))
print(dp("kitten", "sitting"))
print(dp("sunday", "saturday"))