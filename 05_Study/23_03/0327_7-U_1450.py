'''
< 냅색문제 > 
https://www.acmicpc.net/problem/1450
문제)
- N개의 물건
- 최대 C만큼의 무게를 넣을 수 있는 가방 하나
- N개의 물건을 가방에 넣는 방법의 수
입력)
- 1     : N ~ [1 \ 30], C ~ [0 \ 10^9]
- 2     : N개의 무게
출력)
- 1     : 가방에 넣는 방법의 수
'''
import sys, bisect
input = sys.stdin.readline

N, C = map(int, input().split())
a = list(map(int, input().split()))

v1, v2 = [], []

def go(here, _n, v, _sum):
    if _sum > C: return 
    if here > _n: 
        v.append(_sum)
        return 
    go(here + 1, _n, v, _sum + a[here])
    go(here + 1, _n, v, _sum)
    return

go(0, N // 2 - 1, v1, 0)
go(N // 2, N - 1, v2, 0)

v2.sort()

ret = 0
for i in v1:
    if C - i >= 0:
        ret += bisect.bisect_right(v2, C - i)
print(ret)
'''

### 접근법
경우의수 : 2의30승 -> 10억!!! -> DFS로 풀이 불가능!
DP로 상태값 저장하기힘듬
새로운개념 Meet in the Middle
1. 완탐이 될까 ??? 
2. DP로 해볼까 ???
-> 지금문제는 위와같이 접근하면안됨

### <Meet in the Middle>
N이 커서 N/2으로 반으로 쪼개서 완탐으로하는기법
- 2의30승 >>> 2의15승 = 32000

### bisect.bisect_right
- 정렬된 그값 오른쪽 idx
'''