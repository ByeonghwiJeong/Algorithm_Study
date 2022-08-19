'''
소설가는 여러장으로 나뉘어진 소설을 합치려고한다.
예)
C1, C2, C3, C4
40  30  30  50
    x   x
x   x   x
x   x   x   x

2 + 3 >>> 30 + 30 = 60
1 + 23 >>> 40 + 60 = 100
123 + 4 >>> 100 + 50 = 150
60 + 100 + 150 = 310

x   x
        x   x
x   x   x   x
1 + 2 >>> 40 + 30 = 70
3 + 4 >>> 30 + 50 = 80
12 + 34 >>> 70 + 80 = 150
70 + 80 + 150 = 300

입력)
    1      : 테스트 케이스의 수 T 
    2~3 x T - 장의 수 K [3, 500] 
            - 각장의 비용
            
출력) 최소 비용 출력
K = 5
(0, 0) (1, 1) (2, 2) (3, 3) (4, 4)
dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + sum(num[i:j+1])

dp[j][j + i] = min(dp[j + 1][j + i], dp[j][j + i - 1]) + sums[j + i + 1] - sums[j]

=== 

dp[j][j] + dp[j + 1][j + i], 
dp[j][j + 1] + dp[j + 2][j + i]
..
dp[j][j + i - 1] + dp[j + i][j + i]

dp[j][j + k] + dp[j + k + 1][j + i]


(0, 1) (1, 2) (2, 3) (3, 4)
(0, 2) (1, 3) (2, 4) 
(0, 3) (1, 4) 
(0, 4)
----------------------
    a   b   c   d   e
a   0                            
b       0               
c           0       
d               0       
e                   0
---------------------
Tip
- 어떤 함수가 존재하면 편할까??? - DP, 분할정복
- 2개에서 생각해보고!!
- 3개에서 생각해본다!!
- 비용을 생각을 해본다

- 입력에 K가 500이다 500^3까지 가능하다!!!
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    nums = list(map(int, input().split()))
    dp = [[0] * K for _ in range(K)]
    sums = [0]
    s = 0
    for i in range(K):
        s += nums[i]
        sums.append(s)
    for i in range(1, K):
        for j in range(K - i):
            _min = 987654321
            for k in range(i):
                _min = min(_min, dp[j][j + k] + dp[j + k + 1][j + i])
            dp[j][j + i] = _min + sums[j + i + 1] - sums[j]
        
    print(dp[0][K - 1])
        
'''
---------------
40  30  30  50
0   70
    0   60
        0   80
            0
---------------
'''