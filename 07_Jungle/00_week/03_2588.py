a = int(input())
b = input()
result = 0
for i in range(2, -1, -1):
    r = a * int(b[i]) 
    print(r)
    result += r * 10**(2 - i)
print(result)

