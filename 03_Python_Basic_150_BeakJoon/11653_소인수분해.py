'''
시간초과발생 
'''

import sys
int = sys.stdin.readline
N = int(input())
def is_prime(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True

for i in range(2, N//2+1):
    if is_prime(i):
        while N % i == 0:
            N //= i
            print(i)
            if N == 1:
                break
            