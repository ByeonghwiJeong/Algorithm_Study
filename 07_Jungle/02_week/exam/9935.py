'''

'''
import sys
input = sys.stdin.readline

s = input().rstrip()
a = input().rstrip()
stack = []

for i in s:
    stack.append(i)
    if len(stack) >= len(a) and i == a[-1]:
        if ''.join(stack[-len(a):]) == a:
            for _ in range(len(a)):
                stack.pop()
if stack: print(*stack, sep='')
else: print("FRULA")