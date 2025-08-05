from collections import deque
class MyStack:

    def __init__(self):
        self.de = deque()
        

    def push(self, x: int) -> None:
        self.de.append(x)
        for _ in range(len(self.de)-1):
            self.de.append(self.de.popleft())

    def pop(self) -> int:
        return self.de.popleft()

    def top(self) -> int:
        return self.de[0]

    def empty(self) -> bool:
        return len(self.de)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()