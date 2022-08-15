'''
골드바흐의 추측 - 정수론
2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
'''
chk = [True] * 10001
for i in range(2, 10001):
    if chk[i]:
        for j in range(i * 2 , 10001, i):
            chk[j] = False

for _ in range(int(input())):
    n = int(input())
    for i in reversed(range(2, n//2 +1)):
        if chk[i]:
            if chk[n-i]:
                print(i, n-i)
                break

'''
10은 3 7 / 5 5 인데 왜 5 5???
'''