ans = ''
for s in input():
    if s.isdigit():
        ans += s
ans = int(ans)
cnt = 0
for i in range(1, ans+1):
    if ans % i == 0:
        cnt += 1
print(ans)
print(cnt)