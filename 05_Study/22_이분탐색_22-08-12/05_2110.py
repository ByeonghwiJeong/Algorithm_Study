'''

- 1 : 집의 개수 N~[1, 200,000], 공유기의 개수 C~[2, N]
- 2~N+1 : 집의 좌표[0, 1,000,000,000]

 1 2 4 8 9
 x   x   x   3 5
 x   x x     3 4
  1 2 4 1  >> 공유기 3개면 
0 1 3 7 8

< 풀이 >
1. 집과 집 사이의 거리 최솟값을 1 st
2. 집과 집 사이 거리 최댓값을 en
3. mid 값을 최솟값으로 정했을 때 공유기가 몇개 설치 가능한지 확인
4. C보다 작은경우
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

# 공유기 사이 거리 최솟값
st = 1
# 공유기 사이 거리 최댓값
en = house[-1] - house[0]
result = 0

while st <= en:
    mid = (st + en) // 2
    # 공유기 설치된 집의 위치
    cnt = 1 # 공유기 개수
    current = house[0]
    for x in house:
        if current + mid <= x: # 공유기 설치
            cnt += 1
            current = x
    # mid값에 따라 설치된 공유기의 개수가
    if cnt >= C: # C보다 많거나 같으면
        st = mid + 1 # 거리를 늘린다
        result = mid
    else: # C보다 작으면
        en = mid - 1 # 거리를 줄인다

print(result)
