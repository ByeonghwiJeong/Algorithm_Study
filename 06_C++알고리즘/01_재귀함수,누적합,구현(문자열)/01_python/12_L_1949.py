'''
https://www.acmicpc.net/problem/1940
제목 : 주몽

문제
- 갑옷을 만든다
- 갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다.
- 갑옷은 두 개의 재료로 만드는데 두 재료의 고유번호를 합쳐서 M이 되면 갑옷을 만들 수 있다.
- 자신이 가지고 있는 N개의 재료와 M이 주어질 때, 몇개의 갑옷을 만들 수 있는지 구하시오.

입력
- 1 : 재료의 개수 N ~ [1, 15_000]
- 2 : 갑옷의 번호 M ~ [1, 10_000_000]
- 3 : N개의 재료 번호 ~ [1, 100_000]


---
6
9
2 7 4 1 5 3
=> 2
---
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
l, r = 0, N-1

while l < r:
    current_sum = arr[l] + arr[r]
    if current_sum == M:
        cnt += 1
        l += 1
        r -= 1
    elif current_sum < M:
        l += 1
    else:
        r -= 1

print(cnt)