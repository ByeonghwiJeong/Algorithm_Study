'''
< 다이어트 >
https://www.acmicpc.net/problem/19942
문제)
- 식재료 N개 중에서 몇 개를 선택
- 단백질, 탄수화물, 지방, 비타민 : 일정이상이 되어야함
- 각 영양소가 각각 일정 기준을 만족할때 최소비용
입력)
- 1     : 식재료 개수 N ~ [3 \ 15]
- 2     : 최소 기준 영양소 수치 ~ mp, mf, ms, mv \
                단백질, 지방, 탄수화물, 비타민
- 3[N]  : p, f, s, v, c ( c가격 )
출력)
- 최소비용 출력
- 최소 비용 식재료의 번호를 공백으로 구분 오른차순 출력
'''
import sys
input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ret = 987654321
ret_array = []
def recur(p, f, s, v, idx, cost, tmp):
    global ret, ret_array
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if cost < ret:
            ret = cost
            ret_array = tmp[:]
        return
    if idx == N: return
    visited[idx] = 1
    recur(p + a[idx][0], f  + a[idx][1], s + a[idx][2], v + a[idx][3], idx + 1, cost + a[idx][4], tmp + [idx+1])
    visited[idx] = 0
    recur(p, f, s, v, idx + 1, cost, tmp)

recur(0, 0, 0, 0, 0, 0, [])
if ret == 987654321: print(-1); exit()
print(ret)
print(*ret_array)

'''
문제좀 잘읽자!!!!!!!!!!!!
'''