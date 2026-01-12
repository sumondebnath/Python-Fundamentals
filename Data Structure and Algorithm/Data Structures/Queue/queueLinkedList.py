
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def push(self, value):
        newNode = Node(value)
        if self.rear is None:
            self.front = self.rear = newNode
            self._size += 1
            return
        self.rear.next = newNode
        self.rear = newNode
        self._size += 1

    def peek(self):
        if self.isEmpty():
            return None
        return self.front.value

    def pop(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = self.front.next
        self._size -= 1
        if self.front is None:
            self.rear = None
        return temp.value

    def isEmpty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    

queue = Queue()

queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
queue.push(50)

queue.pop()

print(queue.peek())
print(queue.isEmpty())
print(queue.size())