# https://leetcode.com/discuss/general-discussion/1078072/introduction-to-topological-sort

# applications: https://leetcode.com/tag/topological-sort/

# Topological order is a graph which allowed us to find all the subnotes in a given tree based on neighbour nodes. For instance in a given graph. all the nodes below 30 is topological order of 30.
"""
		30
	   /  \
	 20    40
	 /  \   \
   10  	25    50
"""
# implementing DFS
def topological_order_dfs(graph):
    # check for indegree of each nodes in the graph;
    indegree = { node : 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # the nodes with no indegree;
    nodes_with_no_indegree = []
    for node in indegree:
        if indegree[node] == 0:
            nodes_with_no_indegree.append(node)

    # start from the root node and move down its subtree
    topological_order = []
    while len(nodes_with_no_indegree) > 0:
        node = nodes_with_no_indegree.pop()
        topological_order.append(node)

    # at each level remove the indegree;
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                nodes_with_no_indegree.append(neighbor)
    
    if len(graph) == len(topological_order):
        return topological_order
    else:
        raise Exception('Order of cyclic tree cann\'t be determine ')






if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': [],
             'E': ['F'],
             'F': []
			}
    graph2 = {
            30 : [20, 40],
            20 : [10, 25],
            40 : [50],
            10 : [],
            25 : [],
            50 : []
            }
    print(topological_order_dfs(graph))
    print(topological_order_dfs(graph2))
       



