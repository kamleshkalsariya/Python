from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()
new_s = Stack()
string = input()
for char in string:
    s.push(char)
for i in range(s.size()):
    new_s.push(s.pop())
print(''.join(new_s.container))