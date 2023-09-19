# This is the heaps algorithm
def permutate(arr : list):
   if len(arr) == 1:
      return [arr[:]]

   res = []
   for _ in arr:
      head, *tail = arr
      perms = permutate(tail)
      
      for p in perms: 
         p.append(head)

      res.extend(perms)
      arr = tail + [head]
   
   return res

# Every element gets to be the head once 
# After determining the head; we find the permutations of the tail
# We then prepend the head to every permutation of the tail 

# permutate( [a,b] )
# ---
# [a, b]
# head a, tail b
# [[b]] 
# a->[b]
# res = [[a,b]]
# head b, tail a
# [[a]]
# b->[a]
# res = [[a,b], [b,a]]
# -- end


print(
   sorted(
      permutate(["A", "B", "C"])
      )
   )