'''
< 카드 놓기 >
문제)
- 기술 3가지
1. 제일 위의 카드 1장을 바닥에 내려 놓는다.
2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일때
3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일때
- N장의 카드 (1번 ~ N번) 
- 기술을 N번 사용해서 카드를 다 내려놓았을때 위에서 부터
    1, 2, 3, ..., N
- 처음의 카드 배치?
입력)
- 1     : N [1 \ 10^6]
- 2     : 기술 list
출력)
초기 카드의 상태를 위에서 부터 순서대로 출력
'''
from collections import deque

n = int(input())
skills = list(map(int, input().split()))
# skill 뒤에서 부터 
hand = deque()

for i in range(1, n + 1):
    skill = skills[-i]
    if skill == 1: hand.appendleft(i)
    elif skill == 2:
        tmp = hand.popleft()
        hand.appendleft(i)
        hand.appendleft(tmp)
    else:
        hand.append(i)

print(*hand)
