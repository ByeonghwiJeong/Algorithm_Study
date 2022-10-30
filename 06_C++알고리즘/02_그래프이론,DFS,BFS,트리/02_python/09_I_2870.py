import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    s = input().rstrip()
    ret = ""    
    for i in s:
        if i.isdigit(): ret += i
        elif ret: 
            l.append(int(ret))
            ret = ""
    if ret: l.append(int(ret))
print(*sorted(l), sep="\n")
