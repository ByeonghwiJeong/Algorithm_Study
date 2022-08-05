def exchange(S):
    n = len(S)
    for i in range(n-1):
        for j in range(i+1, n):
            if (S[i] > S[j]):
                S[i], S[j] = S[j], S[i]
        print('step',i, S)

S = [-1, 10, 7, 11, 5, 13, 8]
print('Before = ', S)
exchange(S)
print('After =',S)
# [-1, 5, 7, 8, 10, 11, 13]