'''
< 탑 >
https://www.acmicpc.net/problem/2493
문제)
- N개의 높이가 서로 다른 탑을 \
    수평 직선의 왼쪽부터 오른쪽방향으로 차례로 세운다.
- 모든탑의 송신기는 지표면과 평행하게 왼쪽 방향으로 발사한다.
- 예)
6  9  5  7  4 >>> 
입력)
- 
출력)
- 
'''
import sys
input = sys.stdin.readline

n = int(input())
a = [0]
a += list(map(int, input().split()))
stack = [0]
dp = [0] * n

for i in range(1, n+1):
    if a[stack[-1]] < a[i]:
        while a[stack[-1]] < a[i]:
            stack.pop()
            if not stack: break
        if stack:
            dp[i - 1] = stack[-1]
            stack.append(i)
        else:
            stack.append(i)
    else:
        dp[i - 1] = stack[-1]
        stack.append(i)
print(*dp)

