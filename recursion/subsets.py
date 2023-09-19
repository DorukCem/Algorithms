
def find_subsets(arr : list):
   output = [[]]
   
   for element in arr:
      output.extend( [curr + [element] for curr in output] ) 
   
   return output

"""
[[]]                                                                             -> start
[[], ['A']]                                                                      -> add A to every copy previous subsets
[[], ['A'], ['B'], ['A', 'B']]                                                   -> add B to every copy previous subsets
[[], ['A'], ['B'], ['A', 'B'], ['C'], ['A', 'C'], ['B', 'C'], ['A', 'B', 'C']]   -> add C to every copy previous subsets
"""

print(
   sorted( 
      find_subsets(["A", "B", "C"]), key = lambda x: len(x))
   )