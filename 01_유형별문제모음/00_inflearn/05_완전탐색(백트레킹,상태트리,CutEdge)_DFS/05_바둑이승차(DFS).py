"""
트럭은 C kg넘게 태울수없다
C를 넘기 않으면서 가장 무겁게 태우고싶다.
N개의 무게가 주어질때 가장 무거운 무게

입력) C, N
무게들
출력) 가장무거운무게
"""
C, N = map(int, input().split())
w = [int(input()) for _ in range(N)]
result = 0

def dfs(L, sum):
    global result
    if sum > C:
        return
    if L == N:
        if result < sum:
            result = sum
        return    
    dfs(L + 1, sum+w[L])
    dfs(L + 1, sum)

dfs(0, 0)
print(result)