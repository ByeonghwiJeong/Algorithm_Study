'''
<< 회의실 문제 - 매우 자주 나옴!!!! >>

N개의 회의에 대하여
회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
각 회의가 겹치지 않게 하면서 
회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.

회의 시작시간과 끝나는 시간이 같을 수도 있다.(시작하자마자 끝)

첫째 줄에 희의의 수 
'''
import sys
input = sys.stdin.readline

N = int(input())

_table = []
for _ in range(N):
    _table.append(tuple(map(int, input().split())))

_table.sort(key=lambda x:(x[1], x[0]))
# print(_table)
ans = 0
pre_e = 0

for s, e in _table:
    if pre_e <= s:
        ans += 1
        pre_e = e

print(ans)