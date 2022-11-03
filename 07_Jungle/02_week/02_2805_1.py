'''
< 수찾기 >
https://www.acmicpc.net/problem/2805
문제)
- 절단기에 높이 H를 지정 : 톱날이 땅으로부터 H미터
    - 높이가 H보다 위인경우 잘리고 작은경우는 유지

입력)
-   1 : 나무 수 N ~ [1 \ 1,000,000], 나무 길이 M ~ [1 \ 2,000,000,000]
-   2 : 나무의 합은 항상 N보다 크거나 같다.
-   3 : M ~ [1 \ 100,000]
-   4 : M개의 수
    - 이 수들이 a안에 존재하는지?
    <예>
    - 연속해 있는 나무의 길이가 20, 15, 10. 17
    - 상근이가 높이를 15로 지정
    - 자른높이 15 15 10 15
    - 상근이는 5, 2를 가지고 간다 : 총 7미터 GET
출력)
- 절단기에 설정할 수 있는 높이의 최댓값
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))

def binary_search(st, en, t):
    mid = (st + en) // 2
    if st > en: return mid
    hight_sum = sum(i - mid for i in a if i > mid)
    if hight_sum == t: return mid
    elif hight_sum < t:
        return binary_search(st, mid - 1, t)
    elif hight_sum > t:
        return binary_search(mid + 1, en, t)

print(binary_search(0, max(a), m))

'''
mid를 올릴수록(절단기높이) 가지고가는 나무(hight_sum)는 줄어든다!
반대방향
- hight_sum < target : hight_sum를 올리기위해서 낮은범위 탐색
'''