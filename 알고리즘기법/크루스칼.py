"""
최소 신장 트리를 찾는 알고리즘
기본 베이스 : union Find
              최소신장트리의 간선 수 = 노드 - 1
              * 가중치가 적은 것부터 사이클 없이 뽑아낸다! *
              
1. 간선 정보를 가중치에 따라 정렬
2. 가중치가 적은 순으로 간선 data pop
3. 해당 간선의 두 노드를 Find() -> 부모 노드가 같다면, 사이클 발생 -> 해당 간선은 제외
4. 두 노드의 find()값이 다르다 -> 부모 노드가 다르다 -> 사이클 X
5. 사이클이 없는 간선 데이터의 가중치를 합산하며, 두 노드를 Union
"""
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