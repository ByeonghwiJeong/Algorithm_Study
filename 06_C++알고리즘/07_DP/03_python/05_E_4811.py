"""
https://www.acmicpc.net/problem/4811
백준 4811. 알약, G5
- 알약 N개
- 첫째 날 : 알약 하나 꺼내서 반으로 쪼개서 먹음
- 그 다음 날 : 
    - 얄약을 꺼내서 반이면 그냥먹고, 
    - 온전한 약이면 반으로 쪼개서 먹음
- 한 조각을 꺼낸날 : W
- 반 조각을 꺼낸날 : H
- 2N일이 지나는경우 길이가 2N인 문자열을 만들 수 있는 방법의 수
- 서로다른 문자열 수

"""
import sys
input = sys.stdin.readline

arr = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    arr[0][i] = 1
for i in range(1, 31):
    for j in range(i, 31):
        arr[i][j] += arr[i-1][j] + arr[i][j-1]
while True:
    N = int(input())
    if N == 0:
        break
    print(arr[N][N])