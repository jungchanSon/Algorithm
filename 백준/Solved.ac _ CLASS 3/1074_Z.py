import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())
# arr = [[0 for _ in range(2**N)] for _ in range(2**N)]

# cnt = 0
# def dac(start,end, length):
#     global cnt
    
#     if length == 2:
#         arr[start[1]][start[0]] = cnt; cnt +=1
#         arr[start[1]][start[0]+1] = cnt; cnt +=1
#         arr[start[1]+1][start[0]] = cnt; cnt +=1
#         arr[start[1]+1][start[0]+1] = cnt; cnt +=1

#     else :
#         middleX = ((start[0] + end[0]) // 2) +1
#         middleY = ((start[1] + end[1]) // 2) +1

#         dac(start, [middleX, middleY], length//2)
#         dac([middleX, start[1]], [end[0], middleY], length//2)
#         dac([start[0], middleY], [middleX, end[1]], length//2)
#         dac([middleX, middleY], end, length//2)
        
# start = [0, 0]
# end = [2**N -1, 2**N -1]
# dac(start, end, 2**(N))

# print(arr[r][c])
length = 2**N

def dac(x1,y1, x2, y2, v1, v2):
    midX = (x2+x1+1)//2
    midY = (y2+y1+1)//2
    if v1==v2:
        return v1
    area = (v2+1 - v1)//4
    if c < midX and r < midY:
        return dac(x1, y1, midX, midY, v1, v1+area)
    elif c >= midX and r < midY:
        return dac(midX, y1, x2, midY, v1+area, v1+ area*2)
    elif c < midX and r >= midY:
        return dac(x1, midY, midX, y2, v1+area*2, v1+ area*3)
    elif c >= midX and r >= midY:
        return dac(midX, midY, x2, y2, v1+area*3, v2)
    
print(dac(0, 0, length-1, length-1, 0, length**2-1))