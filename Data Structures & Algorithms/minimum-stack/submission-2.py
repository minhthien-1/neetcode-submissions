class MinStack:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, val: int) -> None:
        self.a.append(val)
        if not self.b:
            self.b.append(val)
        else:
            self.b.append(min(val,self.b[-1]))

    def pop(self) -> None:
        self.a.pop()
        self.b.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.b[-1]
