'''
문자열에서 특정 알파벳이 몇 번 나타나는 지 알아봐서 
자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 
실용적인지 확인할 수 있을 것이다.
----------
승재를 도와 특정 문자열 S

특정 알파벳 a와

문자열 구간[l, r]

문자열은 0번째 부터 세며
S의 l번째 문자부터 r번째 문자 사이에 
a가 몇 번 나타나는지 구하는 프로그램


같은 문자열을 두고 질문을 q번 할 것
---------
입력) 
    - 1 : 문자열S 길이 200,000 이하, 소문자
    - 2 : 질문의 수 q 1<= q <= 200,000
    - 3 ~ (q+2) : 질문 - 소문자 a와 0<=l<=r<S
'''
import sys
input = sys.stdin.readline

S = list(map(lambda x:ord(x) - 97, list(input().rstrip())))
# print(S)
q = int(input().rstrip())
N = len(S)
dp = [[0] * (N + 1) for _ in range(26)]
_sums = [0] * 27

# for i, v in enumerate(S):
for i in range(len(S)):
    # _sums[v] += 1
    _sums[S[i]] += 1
    for j in range(26):
        dp[j][i+1] = _sums[j]

# for d in dp:
#     print(*d, sep=' ')

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    a = ord(a) - ord('a')
    # print(a, r, l, dp[a][r+1], dp[a][l])
    print(dp[a][r+1] - dp[a][l])

'''
- 50점 >>> 100점 pypy적용
- 누적으로 합해야함 for loop 26번
'''