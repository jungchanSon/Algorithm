import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    minheap = []
    maxheap = []
    arr = [0 for _ in range(K)]
    for i in range(K):
        op, n = input().rstrip().split()
        n = int(n)
        
        if op == "I":
            heapq.heappush(maxheap, (-1 * n, i))
            heapq.heappush(minheap, (n, i))
        elif op == "D":
            if n == 1:
                while maxheap and arr[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    maxn = heapq.heappop(maxheap)
                    arr[maxn[1]] = 1
            elif n == -1:
                while minheap and arr[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap :
                    minn = heapq.heappop(minheap)
                    arr[minn[1]] = 1
    while maxheap and arr[maxheap[0][1]]:
        heapq.heappop(maxheap)
    while minheap and arr[minheap[0][1]]:
        heapq.heappop(minheap)
    if maxheap and minheap:
        print(heapq.heappop(maxheap)[0] * -1, heapq.heappop(minheap)[0])
    elif maxheap or minheap:
        if maxheap:
            maxn = heapq.heappop(maxheap)[0] * -1
            print(maxn, maxn)
        else :
            minn = heapq.heappop(minheap)[0]
            print(minn, minn)
    else : 
        print("EMPTY")  
        
        
#참고 : https://hongcoding.tistory.com/92