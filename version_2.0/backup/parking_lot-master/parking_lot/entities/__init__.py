class Queue:
    """
    QUEUE implemented using python list data structure
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
