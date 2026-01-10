
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Linked Nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

curr = head

while curr:
    print(curr.value, end='->')
    curr = curr.next

print("None.")