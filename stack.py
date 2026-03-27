class stack:

    def __init__(self, length):
        self.top = -1
        self.length = length
        self.body = []

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
            self.body.append(data)
            self.top +=1
            print(f'{data} Pushed')

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            data = self.body.pop()
            self.top -= 1
            print(f'{data} Popped')
            return data

    def peak(self, pos):
        if self.isEmpty():
            return None
        if pos > self.top + 1:
            print("Position out of Stack!")
            return None
        return self.body[self.top - pos + 1]
