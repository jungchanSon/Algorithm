import sys
input = sys.stdin.readline

def count_prime_sum(n):
    # 에라토스테네스의 체 알고리즘을 사용하여 n 이하의 소수를 구함
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # 연속된 소수의 합으로 n을 나타낼 수 있는 경우를 찾음
    count = 0
    for i in range(2, n + 1):
        if primes[i]:
            total = i
            j = i + 1
            while total < n and j < len(primes):
                if primes[j]:
                    total += j
                    if total == n:
                        count += 1
                        break
                j += 1
            if total >= n:
                break

    return count

print(count_prime_sum(int(input())))