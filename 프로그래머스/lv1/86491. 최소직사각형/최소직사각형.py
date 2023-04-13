def solution(sizes):
    big = []
    small = []
    for i in sizes:
        big.append(max(i[0], i[1]))
        small.append(min(i[0], i[1]))
    
    return max(big)*max(small)