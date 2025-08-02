class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr =self.head
        i = 0
        while curr and i != index:
            curr = curr.next
            i += 1 
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        if self.head:
            self.head.prev = newnode
        self.head = newnode
        

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head=newnode
            return
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = newnode
        newnode.prev = curr
        

    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        if index == 0:
            newnode.next = self.head
            if self.head:
                self.head.prev = newnode
            self.head = newnode
            return
        
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1

        if i != index:
            return
        
        if curr is None:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = newnode
            newnode.prev = tail
        else:
            newnode.next = curr
            newnode.prev = curr.prev
            if curr.prev:
                curr.prev.next = newnode
            curr.prev = newnode
            



            
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i+= 1
        
        if not curr:
            return
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)