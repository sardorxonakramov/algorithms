class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)
        return True

    def pop(self):
        if self.IsEmpty():
            return "Bu bo'sh stack"
        else:
            return self.data.pop()

    def IsEmpty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[-1]

    def sorted(self):
        digit = []
        vovel = []
        for i in self.data:
            if isinstance(i, int) or isinstance(i, float):  
                digit.append(i)
            else:
                vovel.append(i)
        self.data = sorted(digit) + sorted(vovel)
        return self.data
    
    def size(self):
        return len(self.data)