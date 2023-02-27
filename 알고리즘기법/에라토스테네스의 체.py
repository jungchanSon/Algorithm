"""
https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4

1. 소수를 판별할 범위의 배열만큼 생성 및 초기화
2. 2부터 시작해서 특정 수의 배수를 모두 지움
3. 남은 수를 출력
"""
arr = [i for i in range(4000000)]
for i in range(2, 101):
    cnt = 1
    while cnt*i <= 100:
        if cnt*i != i:
            arr[cnt*i] = 0
        cnt+=1
for i in arr:
    if i:
        print(i)