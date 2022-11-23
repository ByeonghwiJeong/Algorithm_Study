'''
< LCS >
https://www.acmicpc.net/problem/9251
문제)
- LCS(Longest Common Subsequence) 최장 공통 부분 수열
- 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
- 예시) ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력)
- 1     : 첫번째 수열
- 2     : 두번째 수열 ~ 최대1000글자
출력)
'''
r = input().rstrip() 
c = input().rstrip()
R = len(r)
C = len(c)

dp = [[0] * (C + 1) for _ in range(R + 1)]

for i in range(1, R + 1):
    for j in range(1, C + 1):
        if r[i-1] == c[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[R][C])

'''
초기값을 처음에 미리 설정해줬었는데 그럴필요가없었다 
최대 값을 뽑는 dp라서 초기값이 0인 dp를 (R+1) x (C+1) 으로 선언

< 틀린경우 > 
    C  A  P  C  A  K
 A [0, 1, 1, 1, 1, 1]
 C [1, 1, 1, 2, 2, 2]
 A [1, 2, 2, 2, 3, 3]
 Y [1, 2, 2, 2, 3, 3]
 K [1, 2, 2, 2, 3, 4]
 P [1, 2, 3, 3, 3, 4]
 < 적어보자자 > 
    C  A  P  C  A  K
 A [0, 1, 1, 1, 1, 1]
 C [1, 1, 1, , , ]
 A [1, , , , , ]
 Y [1, , , , , ]
 K [1, , , , , ]
 P [1, , , , , ]
 같은 경우 처리 방법
'''