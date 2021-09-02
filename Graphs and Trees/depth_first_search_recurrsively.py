# The Depth-First Search is a recursive algorithm that uses the concept of backtracking.
# The only purpose of this algorithm is to visit all the vertex of the graph avoiding cycles.


# Recurrsively DSF algorithm follows as:
# lets begin from a source node and from there we will find all the adjacent node to the source node and their adjacents and so on.
# we would store all the nodes being visited in a set() visited_node;
# process if not node is not in visites node print the node;
# add the node into the visited_node;
# then check for all the neighbours of the node recurrsively...


visited_nodes = set()
starting_node = '5'
def depth_for_search(visited_nodes, graph, node):
    if node not in visited_nodes:
      print(node, end=' ')
      visited_nodes.add(node)
      for adjacents in graph[node]:
          depth_for_search(visited_nodes, graph, adjacents)

       
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
  print(depth_for_search(visited_nodes, graph, starting_node))

#The time complexity of the Depth-First Search algorithm is represented within the sort of O(N+E), where N is that the number of nodes and E is that the number of edges.
#The space complexity of the algorithm is O(N).