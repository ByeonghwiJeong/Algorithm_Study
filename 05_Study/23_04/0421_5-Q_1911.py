"""
< 흙길 보수하기 >
https://www.acmicpc.net/problem/1911
문제)
- 캠프장소 ~ 월드본원
- N개의 물웅덩이
- 물웅덩이를 덮을수 있는 길이 L의 널빤지
- 널빤지로 다리를 만들어 물웅덩이들을 덮으려고 한다.
- 위치와 크기가 주어질때 널빤지 최소 갯수
입력)
- 1     : N, L
- 2[N]  : 시작위치 끝위치
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(N)]
# a.sort(key=lambda x: (x[0], x[1]))
a.sort()
pos = 0
ret = 0
for l, r in a:
    if r <= pos: continue
    if pos < l:
        tmp = (r - l) // K
        if (r - l) % K: tmp += 1
        pos = l + tmp * K
    else:
        tmp = (r - pos) // K
        if (r - pos) % K: tmp += 1
        pos = pos + tmp * K
    ret += tmp
print(ret)