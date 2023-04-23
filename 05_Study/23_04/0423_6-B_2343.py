"""
< 기타 레슨 >
https://www.acmicpc.net/problem/2343
문제)
- 강의 동영상을 블루레이로 만들어 판매
- 블루레이에는 N개의 강의가 들어감
- 블루레이 녹화시 강의의 순서가 바뀌면 안 된다.
- 순서가 바뀌는 경우, 학생들이 혼란에 빠짐
- i번강의와 j번강의를 같은 블루레이에 넣으려면
    i와 j사이의 강의도 같은 블루레이에 녹화해야한다.
- M개의 블루레이에 모든 동영상을 녹화하기로 했다.
- 블루레이의 크기를 최소로 하려고 한다.
- 단, M개의 블루레이는 모두 같은 크기이어야한다.
- 각 강의읭 길이가 분 단위(자연수)로 주어진다.
입력)
- 1     : N ~ [1 \ 100,000], M ~ [1, N]
- 2     : 강의의 길이가 강의 순서대로 분 단위로 주어진다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
l = 0
h = sum(a)
mx = max(a)
ret = 0

def check(mid):
    if mx > mid: return False # 최소 한개는 담아야하므로
    tmp = mid
    cnt = 0
    for i in a:
        if mid - i < 0:
            cnt += 1
            mid = tmp # 다시 블루레이 Count 
        mid -= i
    if mid != tmp: cnt += 1# mid가 tmp인경우 위에서 이미 Counting
    return cnt <= M # 강의를 담을 수 있는경우 True


while (l <= h):
    mid = (l + h) // 2
    if check(mid): # 담을 수있다!!!!
        h = mid - 1
        ret = mid
    else: # 못해 ㅠ 좀더 키우자
        l = mid + 1
print(ret)
"""
< 매개 변수 탐색 >
블루레이 크기가 XX일때 강의를 모두 담을수 있지 않을까?
- check함수 구현법
"""