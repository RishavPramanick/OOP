class Stack:

    def __init__(self, length):
        self.top = -1
        self.length = length
        self.body = [None] * length

    def isFull(self):
        if self.top == self.length - 1:
            return True
        return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.top +=1
            self.body[self.top] = data
            print(f'{data} Pushed')

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            data = self.body[self.top]
            self.body[self.top] = None
            self.top -= 1
            print(f'{data} Popped')
            return data

    def peek(self, pos):
        if self.isEmpty():
            return None
        if pos > self.top + 1:
            print("Position out of Stack!")
            return None
        return self.body[self.top - pos + 1]
