# 01a - Basic Data Structures

# the start of the list is the "top" of the stack
stack = []
stack.insert(0, 'A') # push()
stack.insert(0, 'B')
stack.insert(0, 'C')
print(f'{stack.pop(0) = }') # pop()
print(f'{stack.pop(0) = }')
print(f'{stack.pop(0) = }')

class Stack:
    def __init__(self):
        self._elements = []

    def top(self):
        return self._elements[-1]
    
    def pop(self):
        top_element = self._elements[-1]
        self._elements.pop()
        return top_element
    
    def push(self, new_element):
        self._elements.append(new_element)
    
    def is_empty(self):
        return len(self._elements) == 0
    
    def print(self):
        for i in range(len(self._elements) - 1, -1, -1):
            print(self._elements[i])

stack2 = Stack()
stack2.push('A')
stack2.push('B')
stack2.push('C')
stack2.print()
print(f'{stack2.is_empty() = }')
print(f'{stack2.top() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.is_empty() = }')
