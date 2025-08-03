class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        newnode = Node(homepage)
        self.head = newnode
        self.tail = newnode

        

    def visit(self, url: str) -> None:
        newnode = Node(url)
        self.tail.next = newnode
        newnode.prev =self.tail
        self.tail = newnode
        

        

    def back(self, steps: int) -> str:
        i = 0
        while i != steps:
            if self.tail.prev == None:
                return self.tail.val
            self.tail = self.tail.prev
            i += 1
        return self.tail.val

    def forward(self, steps: int) -> str:
        i = 0 
        while i != steps:
            if self.tail.next == None:
                return self.tail.val
            self.tail = self.tail.next
            i += 1
        return self.tail.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)