class MinStack:

    def __init__(self):
        self.minStack = []
        self.res = []

    def push(self, val: int) -> None:
        self.res.append(val)
        currMin = val
        if self.minStack:
            currMin = min(currMin, self.minStack[-1])
        self.minStack.append(currMin)

    def pop(self) -> None:
        self.res.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
