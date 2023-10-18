def solution(triangle):
    answer = 0
    max_depth = len(triangle)

    for depth in range(1, max_depth):
        triangle[depth][0] += triangle[depth-1][0]
        triangle[depth][len(triangle[depth])-1] += triangle[depth-1][len(triangle[depth])-2]
    
    if max_depth < 3:
        return max(triangle[max_depth-1])
    for depth in range(2, max_depth):
        for pos in range(1, len(triangle[depth])-1):
            triangle[depth][pos] += max(triangle[depth-1][pos], triangle[depth-1][pos-1])
    answer = max(triangle[max_depth-1])
    return answer