'''
https://www.acmicpc.net/problem/2776
문제 : 암기왕

- 수첩1 : 실제 본 숫자들
- 수첩2 : 봤다고 주장하는 숫자들
    - 수첩1에 있으면 1, 없으면 0 출력
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    note1 = set(map(int, input().split()))
    M = int(input())
    for n in map(int, input().split()):
        print(1 if n in note1 else 0)

