class node:

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def display(self):
        prev_addr = hex(id(self.previous)) if self.previous else "NULL"
        next_addr = hex(id(self.next)) if self.next else "NULL"
        print(f'[{prev_addr}| {self.data} |{next_addr}]', end="")

###--- Doubly Linked List
class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        temp = self.head
        print("[ ",end="")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("]")

    def displayGUI(self):
        temp = self.head
        while temp is not None:
            temp.display()
            temp = temp.next
            if temp is not None:
                print("<->", end="")

    def insert_front(self, data):
        newNode = node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

    def insert_back(self, data):
        newNode = node(data)

        if self.tail == None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def remove_front(self):

        temp = self.head

        if temp is None:
            return

        if self.head.next is not None:
            self.head = self.head.next
            temp.next = None
            self.head.previous = None
        else:
            self.head = None
            self.tail = None

        del temp

    def remove_back(self):
        temp = self.tail

        if temp is None:
            return

        if self.tail.previous is not None:
            self.tail = self.tail.previous
            temp.previous = None
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

        del temp
