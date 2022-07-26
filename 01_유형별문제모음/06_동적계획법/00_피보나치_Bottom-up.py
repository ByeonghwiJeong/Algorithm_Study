'''
이코테 피보나치
n1 = 1 n2 = 1 인 피보나치
Bottom-up
'''
# dp table
d = [0] * 100

d[1] = 1
d[2] = 1
n = 5

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])           