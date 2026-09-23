class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = 2e31
        self.minStackLen = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(val <= self.minVal):
            self.minStack.append(val)
            self.minVal = self.minStack[-1]
            self.minStackLen +=1

    def pop(self) -> None:
        val = self.stack.pop()
        if(val == self.minVal):
            self.minStack.pop()
            self.minStackLen -=1
            if(self.minStackLen > 0):
                self.minVal = self.minStack[-1]
            else:
                self.minVal = 2e31

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
