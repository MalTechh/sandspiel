class Node:
    def __init__(self, val, next = None, prev = None ):
        self.val = val 
        self.next = next
        self.prev = prev
class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        newNode = Node(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode
    
    def printList(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next
    
    def printListReversed(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.val)
            current = current.prev


Linked = LinkedList()
Linked.addNode("A")
Linked.addNode("B")
Linked.addNode("C")
Linked.addNode("D")
Linked.addNode("E")
Linked.addNode("F")
Linked.addNode("G")
Linked.addNode("H")
Linked.addNode("I")
Linked.addNode("J")
Linked.addNode("K")
Linked.addNode("L")
Linked.addNode("M")
Linked.addNode("N")
Linked.addNode("O")
Linked.addNode("P")
Linked.addNode("Q")
Linked.addNode("R")
Linked.addNode("S")
Linked.addNode("T")
Linked.addNode("U")
Linked.addNode("V")
Linked.addNode("W")
Linked.addNode("X")
Linked.addNode("Y")
Linked.addNode("Z")
Linked.printList()
Linked.printListReversed()