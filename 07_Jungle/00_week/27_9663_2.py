N = int(input())

ans = 0

col = [False for _ in range(N)]
d1 = [False for _ in range(2 * N)] # \ 대각선
d2 = [False for _ in range(2 * N)] # / 대각선

def bt(row):
    global ans
    
    if row == N:
        # 마지막 줄(N-1) 통과시 ans++ 후 종료
        ans += 1
        return

    for j in range(N if row else N // 2): # row == 0 일때 절반만 체크
        if not col[j] and not d1[row - j] and not d2[row + j]:
            col[j] = True
            d1[row - j] = True
            d2[row + j] = True

            bt(row + 1)

            # 이전 기록 초기화
            col[j] = False
            d1[row - j] = False
            d2[row + j] = False

if N % 2: # N이 홀수
    bt(0)
    ans *= 2

    # 가운데 줄
    j = N//2
    col[j] = d1[-j] = d2[j] = True
    bt(1)
    
else: # N이 짝수
    bt(0)
    ans *= 2

print(ans)