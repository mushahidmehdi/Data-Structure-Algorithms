# https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal.htm

# DFS employs the following rules.
# Rule 1 − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Push it in a stack.
# Rule 2 − If no adjacent vertex is found, pop up a vertex from the stack. (It will pop up all the vertices from the stack, which do not have adjacent vertices.)
# Rule 3 − Repeat Rule 1 and Rule 2 until the stack is empty. 


# recurrsive version

def dfs(graph, node, visited=set()):
    if node not in visited:
      visited.add(node)
      print(node, end=' ')
      for adjacents in graph[node]:
          dfs(graph, adjacents, visited)

def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
      return "Invalid input"
    visited = []
    stack = [source]
    while stack:
      s = stack.pop() # Last out
      if s not in visited: # add into path
          visited.append(s)
      if s not in graph:
          #leaf node
          continue
      for neighbor in graph[s]:
          stack.append(neighbor)
    return " ".join(visited)
       
if __name__ == '__main__':
  graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
  }
  print('Depth for Search')
  print(dfs(graph,'5'))
  print(dfs_non_recursive(graph,'5'))

# The time complexity of the Depth-First Search algorithm is represented within the sort of O(N+E), where N is that the number of nodes and E is that the number of edges.
# The space complexity of the algorithm is O(N).