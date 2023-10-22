import copy
import heapq

def solution(n, s, a, b, fares):
    board = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    for start, end, w in fares:
        board[start].append((end, w))
        board[end].append((start, w))
        
    def dijstra(start, end):
        dist = [1e9 for _ in range(n+1)]
        
        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0
        while q:
            d, nn = heapq.heappop(q)
            if dist[nn] < d:
                continue
            for next in board[nn]:
                cost = dist[nn] + next[1]
                if cost < dist[next[0]]:
                    dist[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))
        return dist[end]
    
    ans = 1e9
    for i in range(1, n+1):
        ans = min(ans, dijstra(s, i) + dijstra(i, a) + dijstra(i, b))
    
    return ans