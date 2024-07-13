import sys, re
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    l.extend(map(int, re.split("[a-z]", input().rstrip())))

print(*sorted(l), sep="\n")
