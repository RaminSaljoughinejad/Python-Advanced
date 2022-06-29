from collections import deque

class CQueue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        if len(self.container):
            return self.container.pop()
        else:
            return ""
    
    def __len__(self):
        return len(self.container)

    def isempty(self):
        if len(self.container):
            return False
        else:
            return True

    def __repr__(self):
        return f"{self.container}"

    def atfront(self):
        return self.container[-1]