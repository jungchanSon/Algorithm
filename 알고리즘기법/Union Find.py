
# 부모 찾는 함수
def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 두 부모 노드를 합치는 함수
def unionParent(parent, a, b):
    a = getParent(parent, a) 
    b = getParent(parent, b)
    if (a < b) : 
        parent[b] = a
    else : 
        parent[a] = b

# 부모가 같은지 확인
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b) 
    if (a == b):
        return True
    return False    