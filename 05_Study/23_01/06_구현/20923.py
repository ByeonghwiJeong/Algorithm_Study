'''
< 숫자 할리갈리 게임 > 
- 카드 덱과 그라운드의 카드를 관리하기위해 덱사용
1. 차례가 되면, 상단카드를 그라운드에 놓는다.
2. 누군가의 카드 덱이 비는 즉시 게임종료
3. 종을 치면, 상대방의 그라운드 카드를 뒤집어서 카드 더미 
'''
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

cards = [deque]


def move_cards(card, ground):
    # index 에러 방지 -1 제거
    ground.popleft()

    # deque.extendleft(arr): arr에 있는 값을 하나씩 배써 왼쪽 삽입
    card.extendleft(ground)
    ground.clear()
    ground.append(-1) # 인덱스 방지 -1 다시 추가
    return 

def play_game(cards, ground):
    player = 0
    
    ground[0].append(-1) # index 에러 방지
    ground[1].append(-1)

    for _ in range(m):