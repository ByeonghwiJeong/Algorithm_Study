"""
https://www.acmicpc.net/problem/1515
제목 : 수 이어 쓰기

1부터 N까지의 수를 이어서 썼다.
그 이후에 임의로 몇개 숫자들을 지웠다.

지운 결과 값이 주어질때 N의 최소값

입력1)
1234 (1부터 N까지의 수를 이어서 썼을때 지운 결과 값)
출력1)
4
입력2)
234092
출력2)
20
"""
import sys
input = sys.stdin.readline

N = input().strip()

now_number = 1
idx = 0

while idx < len(N):
    for char in str(now_number):
        if idx < len(N) and char == N[idx]: # 조건체크
            idx += 1
    now_number += 1

print(now_number-1)

