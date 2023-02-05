'''
< 가르침 >
https://www.acmicpc.net/problem/1062
문제)
- K개의 글자만 안다.
- 남극의 단어는 "anta"으로 시작 ~ "tica"로 끝난다.
- 남극언어에 단어는 N개 밖에 없다고 가정
- 학생들이 읽을 수 있는 단어의 최댓값?
입력)
- 1     : 단어의 개수N 아는 글자K
- 2[N]  : N개의 남극단어
출력)
K개의 글자를 알때 읽을수 있는 단어 개수의 최댓값?
'''
import sys
N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

if K < 5: print(0); exit()
elif K == 26: print(N); exit()

dp = [0] * 26

# 남극 단어 이므로 a c i n t 는 배웠다고 가정
for c in ('a', 'c', 'i', 'n', 't'):
    dp[ord(c) - ord('a')] = 1

ans = 0
def dfs(idx, cnt):
    global ans
    if cnt == K - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not dp[ord(w) - ord('a')]:
                    check = False
                    break
            if check: readcnt += 1
        ans = max(ans, readcnt)
        return
    
    for i in range(idx, 26):
        if dp[i]: continue
        dp[i] = True
        dfs(i, cnt + 1)
        dp[i] = False

dfs(0, 0)
print(ans)

'''
pypy ⭕️
python ❌
'''