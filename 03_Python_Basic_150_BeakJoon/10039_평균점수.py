sum = 0
for _ in range(5):
    s = int(input())
    sum += 40 if s < 40 else s
print(sum//5)