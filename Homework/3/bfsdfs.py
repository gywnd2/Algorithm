from collections import deque
# Define Node & Tree class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.visited = False

class Tree:
    def __init__(self):
        self.root = None

    def makeTree(self, rootNode, nodeL, nodeR):
        if self.root == None:
            self.root = rootNode
        rootNode.left = nodeL
        rootNode.right = nodeR

# Define node with list before make tree
nodes = [Node(10), Node(4), Node(9), Node(3), Node(1),
         Node(2), Node(7), Node(5), Node(6)]

# Assign Tree class variable
myTree = Tree()

# Make tree relation with node list
for i in range(int(len(nodes)/2)):
    # As i varies
    # : 15-> 3, 4 / 3->2,7 / 4->6, 10 ,...
    # same as given diagram "My tree" at first
    myTree.makeTree(nodes[i], nodes[i*2+1], nodes[i*2+2])

def bfs(start):
    # Assign queue variable using deque library
    queue = deque([start])
    # Run until queue is empty
    while queue:
        # Pop a node from left
        node = queue.popleft()
        # Print value of node
        print(node.val, end=' ')
        # If there are children at each direction 
        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)
        # If node have only child at left
        elif node.left:
            queue.append(node.left)
        # If node have only child at right
        elif node.right:
            queue.append(node.right)
        # No child -> pass to make queue empty
        else: pass

def dfs(start):
    # Assign stack variable using list
    stack = [start]
    # Run until stack is empty
    while stack:
        # Pop a node from stack
        node = stack.pop()
        # Print value of node
        print(node.val, end=' ')
        # If there are children at each direction
        if node.left and node.right:
            children = (node.right, node.left)
            stack.extend(children)
        # If node have only child at left
        elif node.left:
            stack.append(node.left)
        # If node have only child at right
        elif node.right:
            stack.append(node.right)
        # No child -> pass to make queue empty
        else: pass

print("BFS : ", end='')
bfs(myTree.root)
print()
print("DFS : ", end='')
dfs(myTree.root)