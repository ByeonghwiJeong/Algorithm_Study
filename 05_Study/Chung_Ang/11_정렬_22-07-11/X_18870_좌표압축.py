'''
수직선 위에 좌표 X1, X2 ... Xn
Xi를 좌표 압축한 결과 X'i값
    - Xi > Xj를 만족하는 서로다른 좌표의 개수
1 <= n <= 1,000,000
-10^9 <= Xi <= +10^9

시간초과 시간초과 시간초과 시간초과
>>>> dictionary 이용!!!!
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))
# for n in nums:
#     ans = 0
#     for i in sorted_nums:
#         if n <= i:
#             break
#         ans += 1
#     print(ans, end=' ')
check = dict()
for i, v in enumerate(sorted_nums):
    check[v] = i
for i in nums:
    print(check[i], end=' ')