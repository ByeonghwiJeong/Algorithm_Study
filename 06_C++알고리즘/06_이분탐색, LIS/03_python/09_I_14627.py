'''
https://www.acmicpc.net/problem/14627
문제 : 파닭파닭

- 한 파의 양을 최대한 많이 넣으려고 한다

첫째 줄에 승균이가 시장에서 사 온 파의 개수 S(1 ≤ S ≤ 1,000,000), 그리고 주문받은 파닭의 수 C(1 ≤ C ≤ 1,000,000)가 입력된다. 파의 개수는 항상 파닭의 수를 넘지 않는다. (S ≤ C) 그 후, S 줄에 걸쳐 파의 길이 L(1 ≤ L ≤ 1,000,000,000)이 정수로 입력된다.
'''
import sys
input = sys.stdin.readline

S, C = map(int, input().split())
PA = [int(input()) for _ in range(S)]
l = 1
h = max(PA)

while l <= h:
    mid = (l + h) // 2
    cnt = sum(p // mid for p in PA) # mid 길이로 잘랐을 때 나오는 파닭 수
    if cnt >= C: # C개 이상 나오면 (더 크게 잘라도 됨)
        l = mid + 1
    else: # C개 미만으로 나오면 (더 작게 잘라야 함)
        h = mid - 1

print(sum(PA) - h * C)