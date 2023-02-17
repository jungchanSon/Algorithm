import sys
input = sys.stdin.readline

N = int(input())
in_order = list(map(int, input().rstrip().split()))
post_order = list(map(int, input().rstrip().split()))

position = [0 for _ in range(N+1)]
for i in range(N):
    position[in_order[i]] = i

def preOder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end :
        return None
    
    
    root = post_order[post_end]
    root_index = position[root]
    
    left = root_index - in_start
    right = in_end - root_index
    
    print(post_order[post_end])
    
    preOder(in_start, in_start + left -1, post_start, post_start+ left - 1)
    preOder(in_end - right + 1, in_end, post_end-right, post_end-1)
preOder(0, N-1, 0, N-1)
    
    
# https://velog.io/@bae_mung/Python-BOJ-2263-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C
# https://ku-hug.tistory.com/135?category=978336