'''
< 곱셈 >
https://www.acmicpc.net/problem/1629
문제)
- 자연수 A를 B번 곱한 수
- 매우 커질수 있으므로 C로 나눈 나머지값출력
입력)
- A, B, C ~ int형 범위 21억
출력)
- 
'''
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def recur(n, x): # n을 x번 곱하기
    if x == 1: return a % c
    r = recur(n, x // 2)
    if x % 2:
        return r ** 2 * n % c
    else: return r ** 2 % c

print(recur(a, b))

'''

'''