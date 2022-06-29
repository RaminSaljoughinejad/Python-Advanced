from collections import deque

class CStack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        if len(self.container):
            return self.container.pop()
        else:
            return ""
    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return f"{self.container}"

    def isempty(self):
        if len(self.container):
            return False
        else:
            return True

    def atfront(self):
        return self.container[-1]