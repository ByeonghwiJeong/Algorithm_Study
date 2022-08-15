'''
1 ~ N번까지 N명이 원을 이루면서 앉아있고
양의 정수 K가 주어진다.
순서대로 K번째 사람을 제거 될 때까지 계속된다.

1 2 3 4 5 6 7
1 2 4 5 6 7

'''
from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
x = deque([i for i in range(1, N + 1)])
ans = []
while len(x) > 0:
    x.rotate(-(K-1))
    ans.append(x.popleft())

print('<', end='')
print(*ans, sep=', ', end='>')
'''
출력 방식????
'''