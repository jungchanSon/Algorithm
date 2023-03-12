class Node:
    def __init__(self, new_data) -> None:
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data) -> None:
        new_node = Node(data)
        if self.head: 
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            self.head = new_node
            
    def appendLeft(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, n, data) -> None:
        new_node = Node(data)
        
        cur_node = self.head
        prev_node = None
        while n:
            prev_node = cur_node
            cur_node = cur_node.next
            n -= 1
            
        prev_node.next = new_node
        new_node.next = cur_node
        
    def __str__(self) -> str:
        
        cur_node = self.head
        res = ""
        while cur_node.next != None:
            res += cur_node.data + " ➡️ "
            cur_node = cur_node.next
        res += cur_node.data
        return res
    
lk = LinkedList()
lk.append("node1")
lk.append("node2")
lk.appendLeft("head")
lk.insert(2, "insert 2")
print(lk)