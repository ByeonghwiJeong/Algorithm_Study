cnt = 1
for _ in range(int(input())):
    s = input()
    s = s.lower()
    ans = 'YES' if s == s[::-1] else 'NO'
    print(f"#{cnt} {ans}")
    cnt += 1

