'''
https://www.acmicpc.net/problem/2512
제목 : 예산


'''
N = int(input()) # 지방수
requests = list(map(int, input().split()))
M = int(input()) # 총예산

# 이진 탐색 범위
lo, hi = 0, max(requests)
ans = 0

# 특정 상한액으로 에산 배정이 가능한지 확인하는 함수
def is_possible(limit):
    # 요청 금액과 상한액 중 작은 값을 더해서 총합이 M이하인지 확인
    return sum(min(request, limit) for request in requests) <= M

while lo <= hi:
    mid = (lo + hi) // 2

    if is_possible(mid):
        ans = mid # 가능한경우 갱신
        lo = mid + 1 # 더 큰 값 선택
    else:
        hi = mid - 1 # 더 작은 값 선택

print(ans)

