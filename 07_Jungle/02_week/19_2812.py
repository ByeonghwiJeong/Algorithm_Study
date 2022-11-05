'''
< 크게만들기 >
https://www.acmicpc.net/problem/2812
문제)
- N자리 숫자가 주어졌을 때, 
- 여기서 K개를 지워서 얻을 수 있는 가장 큰 수
입력)
-
출력)
-
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().rstrip()))

stack = []
for i in a:
    while k > 0 and stack and stack[-1] < i:
        stack.pop()
        k -= 1
    stack.append(i)

if k > 0: print(*stack[:-k], sep="") # 핵심조건
else: print(*stack, sep="")