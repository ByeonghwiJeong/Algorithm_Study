import sys
input = sys.stdin.readline
s = input().strip()
a = input().strip()
stack = []
for i in s:
    stack.append(i)
    if len(stack) < len(a): continue
    if i != a[-1]: continue
    if ''.join(stack[-len(a):]) == a:
        for _ in range(len(a)):
            stack.pop()
if stack: print(*stack, sep='')
else: print('FRULA')
