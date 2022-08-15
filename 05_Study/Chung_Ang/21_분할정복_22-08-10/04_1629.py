'''
홀수 인경우  분기를 2가지로 나누지말고
짝수인경우에서 a값을 곱해서 함수를 1개만 선언!
'''

import sys
input = sys.stdin.readline

def recur(a, b, c):
    if b == 1:
        return a % c
    
    if b % 2: # 1  홀수
        # return recur(a, b//2, c) * recur(a, b//2 + 1, c) % c
        return recur(a, b//2, c) ** 2 * a % c
    else:
        return recur(a, b//2 ,c) ** 2  % c



A, B, C = map(int, input().split())
print(recur(A, B, C))