'''
https://www.acmicpc.net/problem/14658
제목 : 하늘에서 별똥별이 떨어진다

문제)
- 지표면에 떨어지는 별똥별의 수를 최소화
- L * L 크기의 트램펄린 준비
- 별똥별이 어디에 떨어질지 이미 알고 있음
- 이 트램펄린으로 별똥별을 막을 예정
- 최대한 많은 별똥별을 막을 수 있도록 배치
- 모서리에 맞춰도 튕겨 나간다

입력)
- 1 : N, M, L, K 
    - N : 별똥별 떨어지는 구역의 가로 길이 ~ [1, 500_000]
    - M : 별똥별 떨어지는 구역의 세로 길이 ~ [1, 500_000]
    - L : 트램펄린의 가로 세로 길이 ~ [1, 100_000]
    - K : 별똥별의 수 ~ [1, 100]
- 2 : (K lines) 별똥별의 x, y 좌표 ~ [0, N], [0, M]
    
출력)
- 트램펄린을 적절히 배치해서 최대한 많은 별똥별을 튕겨낼 때, 지구에 부딪히는 별똥별의 개수를 출력
'''

import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())

stars = [list(map(int, input().split())) for _ in range(K)]

answer = 0

def process(x, y):
    global answer
    cnt = 0
    for i in range(K):
        if x <= stars[i][0] <= x + L and y <= stars[i][1] <= y + L:
            cnt += 1
    answer = max(answer, cnt)


for i in range(K):
    for j in range(K):
        process(stars[i][0], stars[j][1])

print(K - answer)