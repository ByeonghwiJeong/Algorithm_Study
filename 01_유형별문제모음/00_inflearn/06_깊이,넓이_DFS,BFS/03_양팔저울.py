'''
무게가 서로 다른 K개의 추와 빈그릇이 있다.
모두 추의 무게는 정수이고,
그릇무게는 0이다
주어진 모든추 무게의 합을 S라 하자

입력)
- 1 : 자연수K [3, 13]
- 2[K] : 각추의 무게
출력)
- 불가능한 가지수 
'''
def dfs(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        dfs(L + 1, sum + G[L])
        dfs(L + 1, sum - G[L])
        dfs(L + 1, sum)

n = int(input())
G = list(map(int, input().split()))
res = set()
s = sum(G)
dfs(0, 0)
print(s - len(res))