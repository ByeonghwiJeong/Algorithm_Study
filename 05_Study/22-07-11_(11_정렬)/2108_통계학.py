import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))

l.sort()
l_dict = {}
for i in l:
    if i in l_dict:
        l_dict[i] += 1
    else:
        l_dict[i] = 1
print(l_dict)
mode = []
for k, v in l_dict.items():
    if v == max(l_dict.values()):
        mode.append(k)

print(round(sum(l)/N))
print(l[N//2])
if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])
print(max(l)-min(l))