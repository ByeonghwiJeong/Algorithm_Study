'''
베르트랑 공준 
임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다
'''

while True:
    n = int(input())
    if n == 0:
        break
    chk = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        if chk[i]:
            for j in range(i * 2, 2 * n + 1, i):
                chk[j] = 0
    print(sum(chk[n+1:2*n+1]))
    