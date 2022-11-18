'''
피보나치 수
'''
a = [0] * 92
a[1] = 1
for i in range(2, 91):
    a[i] = a[i-1] + a[i-2]
print(a[int(input())])