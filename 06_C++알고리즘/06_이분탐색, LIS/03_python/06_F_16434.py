'''
https://www.acmicpc.net/problem/16434
문제 : 드래곤 앤 던전

- 용사에게는 세 종류 능력치
    - 최대 생명력
    - 현재 생명력 
    - 공격력
- 던전은 총 N개의 방으로 이루어져 있음
    - i방을 통해서만 i+1방으로 이동 가능
    - 방에는 몬스터 or 포션
    - N번째 방 : 공주 & 드래곤
- 몬스터 방
    1. 용사의 공격력 만큼 몬스터의 생명력 감소
    2. 몬스터 생명력 0이하 전투 종료 & 다음 방으로 이동
    3. 몬스터 공격력 만큼 용사의 생명력 감소
    4. 용사의 생명력 0이하 전투 종료
    5. 다시 1번부터 반복
- 포션 방
    1. 용사의 생명력 회복
    2. 용사의 공격력 증가
    3. 최대 생명력 초과 회복 불가
- N번째 방에 있는 용을 쓰러트리기 위한 최소의 HP

입력)
- 1 : 방의 개수 N ~ [1 \ 123,456], 용사의 초기 공격력 ATK ~ [1 \ 1,000,000]
- 2 ~ N+1 (N줄): t, a, h 
    - t : 방의 종류 (1: 몬스터, 2: 포션)
    - a : 몬스터의 공격력 or 포션의 공격력 증가량
    - h : 몬스터의 생명력 or 포션의 회복량
출력)
- N번째 방에 있는 용을 쓰러트리기 위한 최소의 HP
'''
import sys
import math

input = sys.stdin.readline

N, atk = map(int, input().split())
current_hp = 0  # 현재 필요한 HP
max_hp = 0  # 지금까지 필요했던 최대 HP

for _ in range(N):
    t, a, h = map(int, input().split())
    if t == 1:  # 몬스터 방
        # 용사가 받는 총 데미지 계산
        damage = a * math.ceil(h / atk - 1)
        if current_hp < damage:
            # 현재 HP가 부족하면 max_hp를 증가
            max_hp += damage - current_hp
            current_hp = 0 # 현재 HP는 0
        else:
            current_hp -= damage # 현재 HP에서 데미지만큼 감소
    else:  # 포션 방
        atk += a  # 공격력 증가
        # HP 회복, 단 max_hp를 초과하지 않도록
        current_hp = min(current_hp + h, max_hp)

print(max_hp + 1)  # 최소 1의 HP가 필요하므로 1을 더함