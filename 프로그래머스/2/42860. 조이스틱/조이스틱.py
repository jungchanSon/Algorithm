def solution(name):
    answer = 0
    l = len(name)
    s = 'A' * l
    cursor = 0
    
    a_index = name.find("A")
    cnt = 0
    w = 1
    a_index = -1
    ans = 0
    for i in name:
        ans += min(ord(i) - 65, 91 - ord(i))
    left = -1
    right = -1
    for i in range(20, 0, -1):
        left = name.find('A'*i)
        if left > -1:
            print('A'*i)
            right = left+i
            break
    if left == 0 and right == l:
        return 0
    m = l-1
    for i in range(l-1, 0, -1):
        if name[i] == 'A':
            m -= 1
        else:
            break
    if left > -1:
        m = min((left-1)*2 + l-right, (l-right)*2 + left-1, m)

    return ans + m