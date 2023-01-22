import sys
import heapq
input = sys.stdin.readline

N = int(input())
minHeap = []
# minHeap = [-1]
# def happend(num):
    
#     minHeap.append(num)
#     i = len(minHeap) -1
    
#     while i > 1:
#         parentIndex = i//2
#         if abs(minHeap[i]) < abs(minHeap[parentIndex]):
#             temp = minHeap[parentIndex]
#             minHeap[parentIndex] = minHeap[i]
#             minHeap[i] = temp
            
#         elif abs(minHeap[i]) == abs(minHeap[parentIndex]) and minHeap[i] < minHeap[parentIndex]:
#             temp = minHeap[parentIndex]
#             minHeap[parentIndex] = minHeap[i]
#             minHeap[i] = temp
#         i //= 2
        
    
# def hpop():
    
#     minNum = minHeap[1]
#     lastNode = minHeap.pop()
#     lastIndex = len(minHeap) -1
#     minIndex = 1
    
#     while minIndex < lastIndex:
#         child1 = minIndex*2
#         child2 = minIndex*2 +1
        
#         if child2 <= lastIndex:
#             if abs(minHeap[child2]) < abs(minHeap[child1]) and abs(minHeap[child2]) < abs(lastNode):
#                 minHeap[minIndex] = minHeap[child2]
#                 minIndex = child2 
#             elif abs(minHeap[child1]) < abs(minHeap[child2]) and abs(minHeap[child1]) < abs(lastNode):
#                 minHeap[minIndex] = minHeap[child1]
#                 minIndex = child1
#             elif minHeap[child2] < minHeap[child1] and minHeap[child2] < lastNode:
#                 minHeap[minIndex] = minHeap[child2]
#                 minIndex = child2 
#             elif minHeap[child1] < minHeap[child2] and minHeap[child1] < lastNode:
#                 minHeap[minIndex] = minHeap[child1]
#                 minIndex = child1
                
#         elif child1 <= lastIndex:
#             if abs(minHeap[child1]) < abs(lastNode):
#                 minHeap[minIndex] = minHeap[child1]
#                 minIndex = child1
#             elif minHeap[child1] < lastNode:
#                 minHeap[minIndex] = minHeap[child1]
#                 minIndex = child1
#         else:
#             minHeap[minIndex] = lastNode
        
#     return minNum

for _ in range(N):
    num = int(input())
    if num:
        # happend(num)
        heapq.heappush(minHeap, (abs(num), num))
    else:
        if len(minHeap) == 0:
            print(0)
        else:
            print(heapq.heappop(minHeap)[1])
            # print(hpop())