

class Queue:
    def __init__(self):
        self.elements = []

    def enque(self, element):
        self.elements.append(element)
    def deque(self):
        return self.elements.pop()
    def size(self):
        return len(self.elements)

queue = Queue()
print('Actual:', queue.size(), '')

queue.enque('Alisa')
print('Actual:', queue.deque(), '0')
print('Actual:', queue.size(), '1')


