'''
3 >
9 >
27 >
'''
def draw_star(n):
    global check
    if n == 3:
        check[0][:3] = check[2][:3] = ['*']*3
        check[1][:3] = ['*',' ','*']
        return
    a = n // 3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                check[a*i+k][a*j:a*(j+1)] = check[k][:a]
                # 핵심아이디어

N = int(input())
check = [[' '] * N for _ in range(N)]
draw_star(N)
for c in check:
    print(''.join(c))