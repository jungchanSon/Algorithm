def solution(dots):
    answer = 0
    x1, y1 = 300, 300
    x2, y2 = -300, -300
    for i in dots:
        x1 = min(i[0], x1)
        x2 = max(i[0], x2)
        y1 = min(i[1], y1)
        y2 = max(i[1], y2)
    answer = (x2 - x1) * (y2- y1)
    return answer