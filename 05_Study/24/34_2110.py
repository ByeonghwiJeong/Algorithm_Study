'''
https://www.acmicpc.net/problem/2110
제목 : 공유기 설치

문제)
- 도현이 집에 N개의 수직선 위에 있다.
- 각각의 집의 좌표는 x1, ..., xn 이고 집 여러개가 같은 좌표를 가지는 일은 없다.
- 공유기를 C개를 설치하려고한다.
- 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에,
    가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
- C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성
- 출력 : 인저뷰한 두 공유기 사이의 최대 거리를 출력
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
pos_data = sorted([int(input()) for _ in range(N)]) # 집 좌표 오름차순

def count_router(distance):
    cnt = 1 # 첫 번째 공유기 -> 첫 번째 집
    last_pos = pos_data[0] # 첫 번째 집에 설치한 공유기의 위치
     
    for i in range(1, N): # 두 번째 집부터 
        # distance 체크
        if pos_data[i] - last_pos >= distance:
            cnt += 1 # 공유기 설치
            last_pos = pos_data[i]

    return cnt

# 최대 거리 찾기
def binary_search():
    st = 1
    en = pos_data[-1] - pos_data[0]
    result = 0 

    while st <= en:
        mid = (st + en) // 2
        tmp_cnt = count_router(mid)

        if tmp_cnt >= C: # 설치 가능 갯수가 C이상 (가능함)
            result = mid
            st = mid + 1 # 거리 증가
        else: # 불가능
            en = mid - 1 # 거리 감소

    return result

print(binary_search())
