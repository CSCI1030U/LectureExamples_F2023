# 01a - Basic Data Structures

stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')

class Stack:
    def __init__(self):
        self._elements = []
    
    def top(self):
        return self._elements[-1]
    
    def pop(self):
        popped_element = self._elements[-1]
        self._elements.pop()
        return popped_element
    
    def push(self, new_element):
        self._elements.append(new_element)
    
    def is_empty(self):
        return len(self._elements) == 0

# Coding Exercise 10a.1
stack2 = Stack()
stack2.push('A')
stack2.push('B')
stack2.push('C')
print(f'{stack2.is_empty() = }')
print(f'{stack2.top() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.is_empty() = }')

queue = []
queue.append('A') # back of the queue is the end of the list
queue.append('B')
queue.append('C')
print(f'{queue.pop(0) = }') # front is the start of the list
print(f'{queue.pop(0) = }')
print(f'{queue.pop(0) = }')
