# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
    element = []

    def size(self):
        elem = 0
        for i in self.element:
            elem += 1
        return elem

    def push(self, listN):
        self.element += [listN]

    def pop(self):
        newL = []
        sizes = self.size()
        x = 0
        last = self.element[-1]
        while x <= sizes-2:
            newL += [self.element[x]]
            x += 1
        self.element = newL
        return last

stack = Stack()
stack.push(5)
stack.push(5)
stack.push(3)
print(stack.element)
print(stack.pop())
print(stack.element)
