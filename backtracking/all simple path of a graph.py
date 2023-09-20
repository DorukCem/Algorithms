# A simple path betweeon two nodes:
#  - No cycles
#  - All permuations of the roads that connect two nodes

graph = {'A' : ['B', 'C'],
         'B' : ['C', 'D'],
         'C' : ['D', 'E'],
         'D' : ['E'],
         'E' : ['D']
         }

def find_paths(graph, start, end):
   result = []
   def dfs(graph, current, current_path):
      if current == end:
         result.append(current_path)
      
      else:
         neighbors = graph[current]
         for n in neighbors:
            if n in current_path:
               continue
            dfs(graph, n, current_path + [n])
   
   dfs(graph, start, [start])
   return result

print(*find_paths(graph, 'A', 'D'))