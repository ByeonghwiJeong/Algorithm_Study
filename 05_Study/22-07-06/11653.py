N = int(input())
chk = [True] * (N + 1)

for i in range(2, N +1):
    if chk[i]:
        while True:
            if N % i != 0:
                break   
            N //= i
            print(i)
        for j in range(i*2 , N, i):
            chk[j] = False
