'''
< 부분합 >
https://www.acmicpc.net/problem/1806
문제)
- 10,000 이하의 자연수로 이루어진 길이 N 수열
- 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 
    - 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오
입력)
- 1     : 수열의 크기 N ~ [10 \ 100,000], 판단 기준 S ~ [0 \ 100,000,000]
- 2     : 각 수열의 원소
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 10 ** 5
def two_pointer(target):
    global ans
    st, en, cur = 0, 0, 0 # 왼쪽부터 시작
    while True: 
        if cur >= s:
            ans = min(ans, en - st)
            cur -= a[st]
            st += 1
        elif en == n:
            break
        else:
            cur += a[en]
            en += 1
    return ans

two_pointer(s)
if ans == 10**5: print(0)
else: print(ans)

'''
Two_pointer(누적합X)
'''