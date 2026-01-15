from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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



def build_tree_level_order():
    values = list(map(int, input().split()))
    if not values or values[0] == -1:
        return None

    root = Node(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if values[i] != -1:
            current.left = Node(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != -1:
            current.right = Node(values[i])
            queue.append(current.right)
        i += 1

    return root



root = build_tree_level_order()

levelOrderTraversal(root)