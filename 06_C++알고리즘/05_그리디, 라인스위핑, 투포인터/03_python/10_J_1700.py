'''
https://www.acmicpc.net/problem/1700
제목: 멀티탭 스케줄링

문제
- 멀티탭에 여러개의 전기용품을 꽂아 사용하려고 한다.
- 멀티탭은 여러개의 구멍이 있고, 한 구멍에는 하나의 전기용품을 꽂을 수 있다.
- 자기가 사용하는 전기용품의 사용 순서를 알아냈다.
- 이를 기반으로 멀티탭을 뽑았다가 다시 꽂는 횟수를 최소화하라.

입력
- 1 : 구멍의 개수 N, 전기용품의 총 사용횟수 K ~ [1 \ 100]
- 2 : 전기용품의 사용 순서 ~ [1 \ K]

출력
- 멀티탭을 빼는 횟수의 최솟값을 출력하라.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))

plugs = set()  # 멀티탭에 꽂혀있는 전기용품
cnt = 0  # 뽑는 횟수

for i in range(K):
    item = order[i]
    
    if item in plugs:  # 이미 꽂혀있는 경우
        continue

    if len(plugs) < N:  # 멀티탭에 빈 구멍이 있는 경우
        plugs.add(item)
        continue

    # 멀티탭이 꽉 차있는 경우
    last_use = -1 # 가장 나중에 사용되는 전기용품의 인덱스
    item_to_remove = -1 # 뽑을 전기용품
    
    for plug in plugs:
        # 앞으로 더 사용되지 않는 전기용품을 우선적으로 찾는다.
        if plug not in order[i+1:]: # 더 이상 사용되지 않는 전기용품
            item_to_remove = plug # 뽑을 전기용품
            break
        else: # 사용되는 전기용품
            # 가장 나중에 사용되는 전기용품을 찾는다.
            next_use = order[i+1:].index(plug) 
            if next_use > last_use:
                last_use = next_use
                item_to_remove = plug

    plugs.remove(item_to_remove)
    plugs.add(item)
    cnt += 1

print(cnt)