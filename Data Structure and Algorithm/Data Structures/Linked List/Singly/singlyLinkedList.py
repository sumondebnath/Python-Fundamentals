class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1


    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else: 
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if  self.length == 0:
            self.tail = None

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set_value(self, index, value):
        temp = self.get_value(index)

        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        newNode = Node(value)
        temp = self.get_value(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        prev = self.get_value(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print("\n")



myList = LinkedList(0)

myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)

myList.printList()

print(myList.pop())
print(myList.pop())
print(myList.pop())

myList.printList()

myList.prepend(100)

myList.printList()

print(myList.get_value(2).value)

myList.set_value(1, 200)

myList.printList()

myList.insert(2, 300)

myList.printList()

myList.remove(2)

myList.printList()