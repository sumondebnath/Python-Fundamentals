
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

def insertHead(head, tail, value):
    newNode = Node(value)
    if head is None:
        return newNode, newNode
    newNode.next = head
    head.prev = newNode
    head = newNode
    return head, tail

def insertAtPosition(head, tail, pos, value):
    if pos == 1:
        head, tail = insertHead(head, tail, value)
        return head, tail
    
    newNode = Node(value)
    temp = head
    for _ in range(1, pos-1):
        if temp is None:
            return head
        temp = temp.next

    newNode.prev = temp
    newNode.next = temp.next
    temp.next = newNode
    if newNode.next is not None:
        newNode.next.prev = newNode
    return head, tail


def deleteTail(head, tail):
    if head is None:
        return None, None
    
    if head.next is None:
        return None, None
    temp = tail
    tail = tail.prev
    tail.next = None
    temp.prev = None
    return head, tail

def deleteHead(head, tail):
    if head is None:
        return None, None
    if head.next is None:
        return None, None
    temp = head
    head = head.next
    head.prev = None
    temp.next = None
    return head, tail


def deleteAtPositions(head, tail, pos):
    if head is None:
        return None, None
    curr = head
    for i in range(1, pos):
        if curr is None:
            return head, tail
        curr = curr.next

    if curr is None:
        return head, tail
    
    if curr.prev is not None:
        curr.prev.next = curr.next

    if curr.next is not None:
        curr.next.prev = curr.prev

    if head == curr:
        head = curr.next

    return head, tail 


def printList(head):
    temp = head
    while temp:
        print(temp.value, end=" <==> ")
        temp = temp.next
    print()

def printReverse(tail):
    temp = tail
    while temp:
        print(temp.value, end=" <==> ")
        temp = temp.prev
    print()


head = Node(10)
tail = head

head, tail = insertTail(head, tail, 20)
head, tail = insertTail(head, tail, 30)
head, tail = insertTail(head, tail, 40)
head, tail = insertTail(head, tail, 50)

head, tail = deleteTail(head, tail)
head, tail = deleteTail(head, tail)

head, tail = insertHead(head, tail, 60)
head, tail = insertHead(head, tail, 70)

head, tail = deleteHead(head, tail)
head, tail = deleteHead(head, tail)

head, tail = insertAtPosition(head, tail, 2, 100)
head, tail = insertAtPosition(head, tail, 4, 200)
head, tail = insertAtPosition(head, tail, 1, 200)

head, tail = deleteAtPositions(head, tail, 5)

printList(head)
printReverse(tail)
