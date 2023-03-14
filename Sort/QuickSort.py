import random

rand_arr = [i for i in range(100)]
random.shuffle(rand_arr)
print(rand_arr)

def quick_sort(arr, left, right):
    if left > right:
        return
    
    pivot = arr[left] #배열의 가장 왼쪽값 = 피봇
    i, j = left, right
    
    while i < j:
        while pivot < arr[j]: # 피봇보다 작거나 같은 값 찾음
            j -= 1

        # 오른쪽 인덱스가 왼쪽 인덱스보다 작으면, 배열의 모든 값이 피벗보다 큼 -> 정렬 완료
        while i < j and pivot >= arr[i]:
            i += 1
            
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    arr[left] = arr[i]
    arr[i] = pivot
    pivot = i
    
    quick_sort(arr, left, pivot-1)
    quick_sort(arr, pivot+1, right)

quick_sort(rand_arr, 0, 99)    
print(rand_arr)