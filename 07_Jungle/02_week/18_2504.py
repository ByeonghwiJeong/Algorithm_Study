'''
< 괄호의 값 >
https://www.acmicpc.net/problem/2504
문제)
- 괄호 '(' ')' '[' ']'
- 
입력)

출력)

(()[[]])([])

'''
import sys
input = sys.stdin.readline

def go(x):
    stack = []
    ans = 0
    tmp = 1
    prev = 0
    for s in S:
        if s == '(':
            tmp *= 2
            stack.append(s)
        elif s == '[':
            tmp *= 3
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(': return 0
            if prev == '(': ans += tmp
            tmp //= 2
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[': return 0
            if prev == '[': ans += tmp
            tmp //= 3
            stack.pop()
        prev = s
    return 0 if stack else ans

S = input().rstrip()
print(go(S))