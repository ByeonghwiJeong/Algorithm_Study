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

prefix_sum = [0]
for i in range(1, n + 1):
    prefix_sum.append(a[i-1] + prefix_sum[i-1])

ans = 10 ** 5
def two_pointer(target):
    global ans
    st, en = 0, 1 # 왼쪽부터 시작
    while st < n: # st < en ❌
        S = prefix_sum[en] - prefix_sum[st]
        # S가 target보다 클때 point 좁히기
        if S >= target:
            ans = min(ans, en - st)
            st += 1
        else:
            if en < n: en += 1
            else: st += 1
    return ans

two_pointer(s)
if ans == 10**5: print(0)
else: print(ans)

'''
PrefixSum
'''