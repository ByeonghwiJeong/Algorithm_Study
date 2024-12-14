"""
https://www.acmicpc.net/problem/2138
제목: 전구와 스위치

문제)
- N개의 스위치와 N개의 전구
- 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태
- i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다
- ON -> OFF, OFF -> ON
- 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N
- N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때,
    그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성

입력)
3    : 전구의 개수 N ~ [2, 100_000]
000  : 현재 전구의 상태
010  : 목표 전구의 상태

출력)
3    : 최소 몇 번 눌러야 하는지 (만들 수 없으면 -1 출력)
"""

import sys
input = sys.stdin.readline

N = int(input())

now = list(map(int, input().strip()))
target = list(map(int, input().strip()))

def switch(idx, arr):
    if idx == 0:
        arr[0] = 1 - arr[0]
        arr[1] = 1 - arr[1]
    elif idx == N - 1:
        arr[N - 1] = 1 - arr[N - 1]
        arr[N - 2] = 1 - arr[N - 2]
    else:
        arr[idx] = 1 - arr[idx]
        arr[idx - 1] = 1 - arr[idx - 1]
        arr[idx + 1] = 1 - arr[idx + 1]



def check(now, target, first_switch):
    arr = now[:]
    cnt = 0

    if first_switch:  # 첫 번째 스위치 누름 여부 결정
        switch(0, arr)
        cnt += 1

    for i in range(1, N):
        if arr[i - 1] != target[i - 1]:  
            switch(i, arr)
            cnt += 1

    return cnt if arr == target else float('inf')

result = min(
    check(now, target, False),
    check(now, target, True)
)

print(result if result != float('inf') else -1)
