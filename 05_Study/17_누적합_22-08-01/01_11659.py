'''
https://www.acmicpc.net/problem/11659

수 N개가 주어졌을때 i번째 ~ j번째 합

입력)
    - 첫째줄 : 수의 개수 N, 합을 구해야하는 횟수 M  
    1 <= N, M <= 100,000
    - 둘째줄 : N개의 수가 주어진다. < 1000 인 자연수
    - 셋째줄 : M개의 줄에는 합을 구해야하는 i j
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_nums = list(map(int, input().split()))
_sums = [0]
sum = 0
for i in _nums:
    sum += i
    _sums.append(sum)

# print(_sums)

for _ in range(M):
    i, j = map(int, input().split())
    print(_sums[j] - _sums[i-1])
    
    # print(sum(_nums[i-1:j]))
    # >>> 시간초과발생
'''
위 풀이 시간초과 발생!!!!!????????
???????????
>>> dynamcic 
print(sum(_nums[i-1:j]))
이방식은
'''