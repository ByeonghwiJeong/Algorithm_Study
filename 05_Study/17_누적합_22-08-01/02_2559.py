'''
https://www.acmicpc.net/problem/2559
아침9시에 측정한 온도가 어떤 정수의 수열로 주어졌을때 
연속적인 며칠 동안의 온도의 합이 가장 큰값을 알아보고자 한다.

입력)
    - 첫째줄 : N 온도룰 측정한 날짜의 수 , 
               K  합을 구하기 위한 연속적인 날짜의 수
    - 둘째줄 : 매일 측정한 온도 

--------------
인덱스 문제
>>> 폐구간으로 하기!!!!!! 
>>> 파이썬은 [1, n]
>>> 파이썬은 항상 폐구간으로 하자 
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
_temps = list(map(int, input().split()))
sum = 0
_sums = [0] 

for t in _temps:
    sum += t
    _sums.append(sum)

ans = float('-inf')
# ans = -987654321

for i in range(N - K + 1):
    # if i - 1 < 0:
    #     tmp = _sums[i+K-1]
    # else:
    tmp = _sums[i+K] - _sums[i]
    if tmp > ans:
        ans = tmp
print(ans)
'''
틀림 
2 <= N < 100,000
1 <= K <= N

2 2
5 7 >>  통과

온도가 전부 음수인경우 sum = 0 >> 해결해야함
0으로 초기화가아닌 for문에서 예외처리

=====================================

최대값을 구할때는 초기화를 0했을경우 
최대값이 음수인 상황에서 터진다.
>>> 항상 주의 반례를 생각하자
'''

