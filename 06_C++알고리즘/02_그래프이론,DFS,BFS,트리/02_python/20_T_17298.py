import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
_stack = []
ans = [-1] * N
for i in range(N):
    while _stack and (a[_stack[-1]] < a[i]):
        ans[_stack.pop()] = a[i]
    _stack.append(i)
print(*ans)