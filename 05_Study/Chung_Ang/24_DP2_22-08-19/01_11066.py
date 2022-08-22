'''
소설가는 여러장으로 나뉘어진 소설을 합치려고한다.
예)
0번째
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

12 + 34 >>> 70 + 80 = 150 <<<< 1번 ~ 4번 총합 sums[4] - sums[0]
70 + 80 + 150 = 300

[0, 40, 70, 100, 150, 190] # 

0부터 
dp[i][j] : i번째부터 j번째 까지 누적합의 최소값
    [0 0 0 0][0] / [0 0 0][0 0] [0 0 0 0][0] [0 0 0 0 0]

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
-----------------------------------
dp[j][j + k] + dp[j + k + 1][j + i]

(r, c)
(0, 1) (1, 2) (2, 3) (3, 4)
(0, 2) (1, 3) (2, 4) 
(0, 3) (1, 4) 
(0, 4)
3 * 3  = ab + c / a + bc
4 * 4  = abc + d / ab + cd / a + bcd
5 * 5  = 4번!!!
----------------------
a ~ d = a ~ c + d / a ~ b + c ~ d
    a   b   c   d   e
a   0   0   x1                   
b       0       x2        
c           0       
d               0       
e                   0
---------------------
    a   b   c   d   e
a   x1  x2  x3                   
b       0       y3        
c           0   y2    
d               y1       
e                   0
---------------------
min(x3 + y1, x2 + y2, x1 + y3)
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
        sums.append(s) # K = 5 
    for i in range(1, K): # 간격 1, 2, 3, 4 
        # 숫자가 3개주어지면 K = 3 / K - 1  / i = 2
        for j in range(K - i): # 5 - 1 = 4
            _min = 987654321 # C ++ 기준 int 21억  -1000000000 +100000000
            _min = float('inf')
            _max = float('-inf')
            for k in range(i):  #                        987654321
                _min = min(_min, dp[j][j + k] + dp[j + k + 1][j + i])
            dp[j][j + i] = _min + sums[j + i + 1] - sums[j]

            # j ~ j + i 까지 1
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