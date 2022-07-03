for _ in range(int(input())):
    N, str = input().split()
    ans = ''
    for i in str:
        ans += i*int(N)
    print(ans)