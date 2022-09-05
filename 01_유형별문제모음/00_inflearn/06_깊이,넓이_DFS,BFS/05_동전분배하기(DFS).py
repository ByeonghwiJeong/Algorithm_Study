'''
N개의 동전을 A, B, C에게 나누어 주려고 합니다.
세 명에게 동전을 적절히 나누어 주어,
세 명이 받은 각각의 총액을 계산해,
총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
단 세 사람의 총액은 서로 달라야 합니다.
입력)
- 1 : 동전의 개수 N [3 \ 12]
- 2[N] : N줄에 걸쳐 각 동전의 금액이 주어집니다.
7
8
9
11
12
23
15
17
출력)
- 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.
5
'''
def dfs(L):
    global res
    if L == N:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            dfs(L + 1)
            money[i] -= coin[L]

N = int(input())
coin = []
money = [0] * 3
res = 2147000000
for _ in range(N):
    coin.append((int(input())))
dfs(0)
print(res)
'''
dfs는 상태트리를 그리자!!!
몇번째 동전을 누구한테 줄지를 정해야한다.
L을 넘기면서 L-1번째(0, 1, ... , L-1) 동전을 어디에(0, 1, 2) 넘길지 정한다.
dfs로 트리형태로 들어갔다가 다시 백할때
기존에 더한 값을 빼줘야한다.

세사람의 총액의 서로 달라야한다 >>> set() 자료구조 활용
>>> set()을 했을때 길이가 3으로 유지가 된경우에 다르다!!!
'''