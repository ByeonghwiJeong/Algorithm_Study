import sys, re
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    # s = input().rstrip()
    # ret = ""    
    # for i in s:
    #     if i.isdigit(): ret += i
    #     elif ret: 
    #         l.append(int(ret))
    #         ret = ""
    # if ret: l.append(int(ret))
    l.extend(map(int, re.findall("\d+", input().rstrip())))

print(*sorted(l), sep="\n")
