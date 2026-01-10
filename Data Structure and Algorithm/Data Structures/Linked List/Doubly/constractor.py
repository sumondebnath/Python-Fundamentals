
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def insertTail(head, tail, value):
    newNode = Node(value)
    if head is None:
        # head = newNode
        # tail = newNode
        return newNode, newNode
    tail.next = newNode
    newNode.prev = tail
    tail = tail.next
    return head, tail

def printList(head):
    temp = head
    while temp:
        print(temp.value, end="<==>")
        temp = temp.next


head = Node(10)
tail = head

head, tail = insertTail(head, tail, 20)
head, tail = insertTail(head, tail, 30)
head, tail = insertTail(head, tail, 40)
head, tail = insertTail(head, tail, 50)

printList(head)
