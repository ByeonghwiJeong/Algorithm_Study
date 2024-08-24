'''
https://www.acmicpc.net/problem/20922

제목 : 겹치는 건 싫어

문제)
- 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다
- 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이
- 100000이하 양의 정수로 이루어진 길이가 N인 수열
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

ret = 0
num_dict = defaultdict(int)

while end < N:
    if num_dict[arr[end]] < K: 
        # 현재 end가 가리키는 값이 K개 미만이면 (end + 1)
        num_dict[arr[end]] += 1
        end += 1
        ret = max(ret, end-start)
    else: # 현재 end가 가리키는 값이 K개 이상이면 (start + 1)
        num_dict[arr[start]] -= 1
        start += 1

print(ret)