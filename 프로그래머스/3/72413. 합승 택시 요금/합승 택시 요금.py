import heapq

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    d = [1e6 for _ in range(n+1)]
    for start, e, c in fares:
        graph[start].append([e, c])
        graph[e].append([start, c])
    
    def dij(s, e):
        q = []
        heapq.heappush(q, (0, s)) 
        d = [1e6 for _ in range(n+1)]
        d[s] = 0
        while q:
            dist, now = heapq.heappop(q)
            if d[now] < dist:
                continue
            for nxt in graph[now]:
                cost = d[now] + nxt[1]
                if cost < d[nxt[0]]:
                    d[nxt[0]] = cost
                    heapq.heappush(q, (cost, nxt[0])) 
        return d[e]
    
    answer = dij(s, a) + dij(s, b)

    for i in range(1, n+1):
        answer = min(answer, dij(s, i) + dij(i, a) + dij(i, b))
    return answer
