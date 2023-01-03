'''
< 알바생 강호 >
https://www.acmicpc.net/problem/1758
문제)
- 8시가 될 때 까지 줄스고 되는순간 손님들은 모두 입구에서 커피를 하나씩 받고, 자리로 간다.
- 강호는 입구에서 커피를 하나씩 준다.
- 각 손님은 강호에게 팁을 준다
    ( 원래 주려고 생각했던 돈 ) - (받은 등수 - 1)
    - 음수면 받지 못한다
'''
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
ans = 0
for i in range(n):
    if a[i] - i > 0: ans += a[i] - i
print(ans)