import sys
input = sys.stdin.readline

def check(X):
    l = []
    for i in X:
        if i == '(': l.append(i)
        else:
            # if l: l.pop()
            # else: return False
            try: l.pop()
            except: return False
    return False if l else True

for _ in range(int(input())):
    s = input().rstrip()
    if check(s): print("YES")
    else: print("NO")