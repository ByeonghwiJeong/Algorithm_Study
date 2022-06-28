# Bottom Up 방식
# 추후에 Top down 방식 
'''
f(n,d) : d로 끝나고 길이 n인 계단수 
    >>>> f(n+1, d+1)와 f(n+1, d-1) 에 영향을 준다.
f(n) : 길이 n인 계단수 총 개수
조건1) 시작 0 불가
조건2-1) 끝자리가 0혹은 9인경우 1가지
    if d=0:
        f(n,0) = f(n-1, 1)
    if d=9:
        f(n,9) = f(n-1, 8)
조건2-2) 끝자리가 1~8인경우 2가지
    f(n,d) = f(n-1, d+1) + f(n-1, d-1)
f(n) = (f(n,0)+f(n,1)+f(n,2)+ ... +f(n,9))%MOD

'''
MOD = 1_000_000_000
# cache[n][d]: 길이가 n, 마지막숫자가 d인 계단수
cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j>0:
            cache[i][j] += cache[i-1][j-1]
            cache[i][j] %= MOD
        if j<9:
            cache[i][j] += cache[i-1][j+1]
            cache[i][j] %= MOD

ans = 0 
N =int(input())
for j in range(10):
    ans += cache[N][j]
    ans %= MOD

print(ans)