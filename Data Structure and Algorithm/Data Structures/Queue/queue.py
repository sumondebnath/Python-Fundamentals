from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

queue.popleft()

print(queue[0])

print(queue)