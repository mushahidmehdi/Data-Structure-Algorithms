# The Depth-First Search is a recursive algorithm that uses the concept of backtracking.
# The only purpose of this algorithm is to visit all the vertex of the graph avoiding cycles.


# The DSF algorithm follows as:
# 1) We will start by putting any one of the graph's vertex on top of the stack.
# 2) After that, take the top item of the stack and add it to the visited list.
# 3) Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.
# 4) Lastly, keep repeating steps 2 and 3 until the stack is empty.

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited_nodes = set()
starting_node = '5'
def depth_for_search(visited_nodes, graph, node):
    if node not in visited_nodes:
      print(node, end=' ')
      visited_nodes.add(node)
      for adjacents in graph[node]:
        depth_for_search(visited_nodes, graph, adjacents)

print('Depth for Search')
print(depth_for_search(visited_nodes, graph, starting_node))

#Time Complexity
#The time complexity of the Depth-First Search algorithm is represented within the sort of O(N+E), where N is that the number of nodes and E is that the number of edges.
#The space complexity of the algorithm is O(N).