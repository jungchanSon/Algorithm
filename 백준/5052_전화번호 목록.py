import sys
input = sys.stdin.readline

class Trie:
    def __init__(self) -> None:
        self.root = Node(None)

    def add_data(self, data) -> None:
        cur_node = self.root
        while data:
            check = False
            cur = data.pop(0) 
            for i in cur_node.child:
                if i == cur:
                    check = True
                    cur_node = i
            if not check:
                cur_node.append(cur)
                     
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.child = []
    
    

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = []
    for i in range(N):
        numbers.append(input().rsplit())
    
    print(numbers)
    
"""
   9    
1   7
1   6
"""