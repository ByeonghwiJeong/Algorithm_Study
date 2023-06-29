'''
- 당신은 복권을 사려고 합니다.
- 살수 있는 복권 여러개 그중 하나만 구입가능
- 알고있는 복권 정보
    1. 당첨자 수
    2. 구매한 사람 수
    3. 당첨 금액
- 추첨 방법
    1. 당첨자 수보다 구매한 사람 수가 같거나 적을 경우 구매한 사람 모두가 당첨
    2. 당첨사 수 < 구매자 수 : 무작위 당첨
- 당첨 확률이 가장 높은 복권을 사려고함
    - 당첨 확률이 가장 높은 복권이 여러개면 금액이 제일 높은 것 구매
- 단, 복원 당첨 금액은 모두 다름 \
    당첨 확률이 가장 높으면서 당첨금액이 가장 높은 복권은 하나만 존대
- lotteries배열 - 2차원배열
    : 각복권의 당첨자수, 구매한 사람수, 당첨 금액


'''
def cal(a, b, c):
    if a > b:
        return [1, c]
    return [a / (b+1), c]

def solution(lotteries):
    _list = []
    for i, x in enumerate(lotteries):
        tmp = cal(*x)
        tmp.append(i + 1)
        tmp2 = []
        tmp2 = tmp[:]
        _list.append(tmp2)
    _list.sort(key=lambda x: (x[0], x[1]))
    # print(_list)
    answer = _list[-1][2]
    return answer

print(solution([[100, 100, 500], [1000, 1000, 1000]]))