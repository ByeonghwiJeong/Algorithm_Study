'''
https://www.acmicpc.net/problem/2493
제목: 탑

문제
- 일직선 위에 N개의 높이 서로 다른 탑
- 모든 탑은 순서 반대방향(왼쪽)으로 레이저 신호를 발사

입력
- 1 : 탑의 수 N ~ [1 \ 500_000]
- 2 : N개의 탑의 높이 ~ [1 \ 100_000_000]
```
5
6 9 5 7 4
```

출력
- 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력
- 만약 수신한 탑이 없으면 0을 출력
```
0 0 2 2 4
```
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
dp = [0] * n

for i, v in enumerate(a):
    while stack and a[stack[-1]] < v:
        stack.pop()
    if stack: # 번호 기록 : index + 1 
        dp[i] = stack[-1] + 1
    stack.append(i)
    
print(*dp)