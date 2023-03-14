from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.childen = []
    
class Tree:
    def __init__(self, data) -> None:
        self.root = Node(data)
    
    def add_node(self, target_data, new_data, ) -> None:
        q = deque()
        q.append(self.root)
        while q:
            current_node = q.popleft()
            if current_node.data == target_data:
                current_node.childen.append(Node(new_data))        
                break
            
            for i in current_node.childen:
                q.append(i)
    
tree = Tree("A")
tree.add_node("A", "B")
tree.add_node("A", "C")
tree.add_node("B", "D")
tree.add_node("C", "F")

print("A의 자식 :", end=" ")
for i in tree.root.childen:
    print(i.data, end=" ")
print("\nB의 자식 :", end=" ")
for i in tree.root.childen[0].childen:
    print(i.data, end=" ")    
print("\nC의 자식 :", end=" ")
for i in tree.root.childen[1].childen:
    print(i.data, end=" ")
