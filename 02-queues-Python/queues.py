"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]        


    def enqueue(self, new_element):
        self.storage.append(new_element)
        return self.storage
        

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        top=self.storage[0]
        self.storage.remove(top)
        return top

# queues = Queue(5)
# print(queues.enqueue(1))
# print(queues.dequeue())
# print(queues.peek())