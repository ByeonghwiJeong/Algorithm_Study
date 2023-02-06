N = int(input())
times = list(map(int, input().split()))
times.sort()
ans = 0
for i in range(1, N+1):
    ans += sum(times[:i])
print(ans)