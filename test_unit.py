# li = [1,24,5,6,767,8]
# print(li)
# print(li[-1])

# x = isinstance(False, bool)
# print(x)

# class Graph:
#     # Constructor
#     def __init__(self, edges, N):
#         # A list of lists to represent an adjacency list
#         self.adjList = [[] for _ in range(N)]
#  
#         # add edges to the undirected graph
#         for (src, dest) in edges:
#             self.adjList[src].append(dest)
#             self.adjList[dest].append(src)
# 
# 
# if __name__ == '__main__':
# 	# List of graph edges as per the above diagram
# 
# 	edges = [# Notice that node 0 is unconnected
# 	(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
# 	(3, 5), (8, 9), (8, 12), (9, 10), (9, 11)]
# 
# 	# total number of nodes in the graph (0–12)
# 	N = 13
# 
# 	# build a graph from the given edges
# 	graph = Graph(edges, N)
# 	


#graph = {'A': ['B', 'C'],
#             'B': ['C', 'D'],
#             'C': ['D'],
#             'D': ['C'],
#             'E': ['F'],
#             'F': ['C']}
#
##  Code by Eryk Kopczyński
#from collections import deque
#
#def find_shortest_path(graph, start, end):
#        dist = {start: [start]}
#        q = deque(start)
#        while len(q):
#            at = q.popleft()
#            for next in graph[at]:
#                if next not in dist:
#                    dist[next] = [dist[at], next]
#                    q.append(next)
#        return dist.get(end)
#print(find_shortest_path(graph, 'A', 'D'))
# import numpy as np
#print(np.zeros((9,9)))
# Python program to find the inorder successor in a BST

# Python program to find the inorder successor in a BST

#strg = "  A binary tree node  " 
#str = strg.strip()

#def bidirectional_search(src, des):
#	def backtrack(node):
#		path = []
#		copy = node
#		while copy:
#			path.append(copy.data)
#			copy = copy.right
#		while node:
#			path.append(node.data)
#			node = node.left
#		path.reverse()
#		del path[-1]
#		return path
#
#	queue = []
#	queue.append(src)
#	queue.append(des)
#	src.visit_left = True
#	des.visit_right = True
#
#	while len(queue) > 0:
#		node = queue.pop()
#
#		if node.visit_right and node.visit_left:
#			return backtrack(node)
#
#		for neighbor in node.neighbors:
#			if node.visit_right and not neighbor.visit_right:
#				neighbor.right = node
#				neighbor.visit_right = True
#				queue.append(neighbor)
#			if node.visit_left == True and not neighbor.visit_left:
#				neighbor.left = node
#				neighbor.visit_left = True
#				queue.append(neighbor)
#	return False
	

# if __name__ == '__main__':
# 	n1 = Node(1)
# 	n2 = Node(2)
# 	n3 = Node(3)
# 	n4 = Node(4)
# 	n5 = Node(5)
# 	n6 = Node(6)
# 	n7 = Node(7)
# 	n8 = Node(8)
# 	n9 = Node(9)
# 	n10 = Node(10)
# 	n1.neighbors = [n3, n5]
# 	n2.neighbors = [n6, n7]
# 	n3.neighbors = [n2, n8]
# 	# n5.neighbors = [n4, n6]
# 	n4.neighbors = [n5, n6, n4]
# 	n6.neighbors = [n7, n9]
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import rabin_karp
import numpy as np
from os.path import dirname, join


class PlagiarismChecker:
    def __init__(self, file_a, file_b):
        self.file_a = file_a
        self.file_b = file_b
        self.hash_table = {"a": [], "b": []}
        self.k_gram = 5
        content_a = self.get_file_content(self.file_a)
        content_b = self.get_file_content(self.file_b)
        self.calculate_hash(content_a, "a")
        self.calculate_hash(content_b, "b")
        
    # calaculate hash value of the file content
    # and add it to the document type hash table 
    def calculate_hash(self, content, doc_type):
        text = self.prepare_content(content)
        text = "".join(text)

        text = rabin_karp.rolling_hash(text, self.k_gram)
        for _ in range(len(content) - self.k_gram + 1):
            self.hash_table[doc_type].append(text.hash)
            if text.next_window() == False:
                break
 
    def get_rate(self):
        return self.calaculate_plagiarism_rate(self.hash_table)
      
    # calculate the plagiarism rate using the plagiarism rate formula
    def calaculate_plagiarism_rate(self, hash_table):
        th_a = len(hash_table["a"])
        th_b = len(hash_table["b"])
        a = hash_table["a"]
        b = hash_table["b"]
        sh = len(np.intersect1d(a, b))
        print(sh, a, b)

        # Formular for plagiarism rate
        # P = (2 * SH / THA * THB ) 100%
        p = (float(2 * sh)/(th_a + th_b)) * 100
        return p
      
    # get content from file
    def get_file_content(self, filename):
        file = open(filename, 'r+', encoding="utf-8")
        return file.read()
      
    # Prepare content by removing stopwords, steemming and tokenizing 
    def prepare_content(self, content):
        # STOP WORDS
        stop_words = set(stopwords.words('english'))
        # TOKENIZE
        word_tokens = word_tokenize(content)
        filtered_content = []
        # STEMMING
        porter = PorterStemmer()
        for w in word_tokens:
            if w not in stop_words:
                w = w.lower()
                word = porter.stem(w)
                filtered_content.append(word)

        return filtered_content


current_dir = dirname(__file__)
checker = PlagiarismChecker(
    join(current_dir, "./document_a.txt"),
    join(current_dir, "./document_b.txt")
)
print('The percentage of plagiarism held by both documents is  {0}%'.format(
    checker.get_rate()))