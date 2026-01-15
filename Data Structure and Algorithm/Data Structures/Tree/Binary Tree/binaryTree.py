from collections import deque 


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrderTraversal(root):
    if root is None:
        return
    print(root.value, end=", ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.value, end=", ")
    inOrderTraversal(root.right)


def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value, end=", ")


def levelOrderTraversal(root):
    if root is None:
        return 
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.value, end=", ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



root = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)
node6 = Node(70)
node7 = Node(80)
node8 = Node(90)
node9 = Node(99)

root.left = node1
root.right = node2

node1.left = node3
node2.right = node4

node3.left = node5
node4.right = node6

node5.left = node7
node6.right = node8

node7.left = node9


print("Pre-Order Traversal : ")
preOrderTraversal(root)

print("\nIn-Order Traversal : ")
inOrderTraversal(root)

print("\nPost-Order Traversal : ")
postOrderTraversal(root)

print("\nLevel-Order Traversal : ")
levelOrderTraversal(root)