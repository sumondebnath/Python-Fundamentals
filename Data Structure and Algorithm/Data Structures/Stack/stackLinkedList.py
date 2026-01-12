
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self._size +=1
    
    def pop(self):
        if self.isEmpty():
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self._size -= 1
        return temp.value
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.value
    
    def isEmpty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.pop()

top = stack.peek()
sz = stack.size()
print(top)
print(sz)
print(stack.isEmpty())

while(stack.isEmpty() != True):
    print(stack.peek(), end=" ")
    stack.pop()