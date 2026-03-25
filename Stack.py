
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# pop element
removed = stack.pop()
print("Popped element:", removed)

print("Stack now:", stack)

# peek (top element)
print("Top element:", stack[-1])