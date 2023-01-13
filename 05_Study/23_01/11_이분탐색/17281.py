'''
< 야구 >
문제)
- 1 ~ 9 번 선수를 기준으로 어떤 결과를 얻는지 미리 알고 있다.
    - 0 : 아웃
    - 1 : 안타
    - 2 : 2루타
    - 3 : 3루타
    - 4 : 홈런
- 1번 선수를 4번 타자로 미리결정
입력)
- 1     : 이닝 수 N ~ [2 \ 50]
- 2[N]  : 각 이닝에서 1 ~ 9번선수의 결과
'''
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def cal_score(order):
    player = 0
    score = 0

    # result의 한 행이 inning이 되고, 
    for inning in result:
        out = 0
        base1 = base2 = base3 = 0
        while out < 3:
            p = inning[order[player]]
            if p == 0:
                out += 1
            elif p == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif p == 2:
                score += base3 + base2
                base3 = base1
                base2 = 1
                base1 = 0
            elif p == 3:
                score += base3 + base2 + base1
                base3 = 1
                base2 = base1 = 0
            else:
                score += base3 + base2 + base1 + 1
                base3 = base2 = base1 = 1
            # 다음 타자로 바꿔 줌
            player = (player + 1) % 9
    return score

# 가능한 모든 배치를 구하되, 1번타가(0번 인덱스)는 고정~주의
for order in permutations(range(1, 9), 8):
    order = list(order)
    order.insert(3, 0)
    # 최댓값 갱신
    ans = max(ans, cal_score(order))

print(ans)
