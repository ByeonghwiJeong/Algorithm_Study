'''
https://www.acmicpc.net/problem/1644
제목: 소수의 연속합

문제
- 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.
    - 3 = 3 (1가지)
    - 41 = 2 + 3 + 5 + 7 + 11 + 13 = 11 + 13 + 17 = 41 (3가지)
- 20 같은 경우는 연속된 소수의 합으로 나타낼 수 없다. 7 + 13 = 20 이지만 연속된 소수가 아니다.

입력
- 자연수 N ~ [1 \ 4,000,000]
'''
import sys
input = sys.stdin.readline


def check_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [x for x in range(2, n+1) if is_prime[x]]

def count_prime_sums(n):
    primes = check_primes(n)
    print(primes)
    count = 0
    left = 0
    sum = 0
    for right in range(len(primes)): # right 포인터를 오른쪽으로 이동
        sum += primes[right] # right 포인터를 이동시키면서 sum을 계산
        while sum > n and left <= right: # sum이 n보다 크면 left 포인터를 이동시키면서 sum을 계산
            sum -= primes[left]
            left += 1
        if sum == n:
            count += 1
    
    return count

N = int(input())
print(count_prime_sums(N))
