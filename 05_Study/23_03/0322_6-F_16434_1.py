'''
< 드래곤 앤 던전 >
https://www.acmicpc.net/problem/16434
문제)
- 용사는 공주를 구하기위해 던전으로 감
- 용사의 능력치
    - MaxHP : 용사의 최대 생명력
    - CurHP : 용사의 현재 생명력
    - ATK   : 용사의 공격력
- 던전은 총 N개의 방
    - i번째 방을 통해서만 i+1번째 방으로 이동 할 수 있음(순서바꿀수없음)
    - 방에는 포션 or 몬스터
    - N번째 방에는 공주 and 용 
- 몬스터가 있는 방
    1. 용사의 공격력만큼 몬스터 생명력
    2. 몬스터의 생명력이 0이하인경우 전투 종료 다음방이동
    3. 몬스터의 공격력만큼 현재 생명력 깍습니다.
    4. 용사 생명력 0이하 사망
    5. 1 ~ 4반복
- 포션있는방
    - 현재 생명력 일정량 회복
        - 최대생명력보다 높을수 없음
    - 공력력 일정량 증가
- N번 방에 있는 용을 쓰러트리기 위한 최소의 HP

입력)
- 1     :  방의 개수 N ~ [1 \ 123,456] 초기공격력 ~ [1 \ 1,000,000]
- 2[N]   
    - 몬스터 t=1 : 공격력 a, 생명력h인 몬스터 
    - 포션 t=2 : 공력력 a증가, 생명력 h회복
출력)
- 1     : 
'''
import sys
input = sys.stdin.readline

N, atk = map(int, input().split())
init_lo = 1
T = []
A = []
H = []
for _ in range(N):
    t, a, h = map(int, input().split())
    T.append(t)
    A.append(a)
    H.append(h)

def check(x):
    init_hp = x
    init_atk = atk
    for i in range(N):
        if T[i] == 2:
            x = min(init_hp, x + H[i])
            init_atk += A[i]
        else:
            div = H[i] // init_atk + (1 if H[i] % init_atk else 0)
            atk_cnt = div - 1
            x -= atk_cnt * A[i]
        if x <= 0: return False
    return True

lo = 1
# hi = 987654321 
# 안됨 ㅠ
# hi = 1e18
# 이것도 안됨 ㅠ 
hi = sys.maxsize
ret = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid - 1
        ret = mid
    else: lo = mid + 1

print(ret)

'''
이분 탐색은 longlong 범위로 탐색하자!!!
파이썬은 sys.maxsize
hi = 1e18으로하면 오류발생(소수점)
'''