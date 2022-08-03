'''
<< 중요 >>

2 <= M <= 1000 조건 주의 
1000이하인 이유가 있다!!! 10^9이 아닌 이유가 있다.

1 <= N <= 10^6
2 <= M <= 10^3
0 <= Ai <= 10^9

N개의 수가 주어진다. 
연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수

------------------------------------------------
입력)
    - 1 : N과 M이 주어진다.
    - 2 : N개의 수가 주어진다.

아이디어)
    - 부분합 list선언
    - M에대한 부분합의 나머지 list
    - 나머지 같은 것끼리 Combination
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_list = list(map(int, input().split()))
_remainders = [0]
sum = 0

for i in _list:
    sum += i
    tmp = sum % M
    _remainders.append(tmp)

_dict = dict()
for i in _remainders:
    if i in _dict:
        _dict[i] += 1
    else:
        _dict[i] = 1

ans = 0
for i in _dict.values():
    ans += i * (i - 1) // 2

print(ans)   