'''
새로운 블랙잭 규칙
1. 딜러는 N장의 카드를 모두 숫자가 보이도록 놓는다
2. 딜러가 숫자 M을 외친다.
3. 플레이어는 제한된 시간 안에 N장의 카드중에서 3장의 카드를 pick
4. 플레이어는 M을 넘지 않으면서 M과 최대한 가깝게 만든다.
'''
from itertools import combinations

N, M = map(int, input().split())
l = list(map(int, input().split()))
s = list(combinations(l,3))
ans = 0
for i in s:
    a = sum(i)
    if a <= M and ans < a:
        ans = a
print(ans)
