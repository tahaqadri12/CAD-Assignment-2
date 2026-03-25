# simple queue program

queue = []

# enqueue (add elements)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

# dequeue (remove element)
removed = queue.pop(0)
print("Removed element:", removed)

print("Queue now:", queue)

# front element
print("Front element:", queue[0])