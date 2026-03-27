class linearQueue:

    def __init__(self, length):
        self.length = length
        self.body = [None] * length
        self.front = -1
        self.back = -1

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def isFull(self):
        if self.back == self.length - 1:
            return True
        return False

    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0

        self.back += 1
        self.body[self.back] = data
        print(f'{data} Enqueued')

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        data = self.body[self.front]
        self.body[self.front] = None
        self.front += 1
        print(f'{data} Dequeued')

        if self.front > self.back:
            self.front = -1
            self.back = -1
        return data

    def peek(self, position):
        if self.isEmpty():
            return None
        if position <= 0 or position > (self.back - self.front + 1):
            print("Position out of Queue")
            return
        return self.body[self.front + position - 1]


class circularQueue:

    def __init__(self, length):
        self.length = length
        self.body = [None] * length
        self.front = -1
        self.back = -1

    def isFull(self):
        if (self.back - self.front) % self.length == 0:
            return True
        return False

    def isEmpty(self):

