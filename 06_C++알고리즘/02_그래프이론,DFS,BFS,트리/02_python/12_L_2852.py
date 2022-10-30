import sys
input = sys.stdin.readline

A = B = 0 # 1 team score \ 2 team score
asum = [0]
bsum = [0]
prev = ""

def timeform(x):
    m = "00" + str(x // 60)
    s = "00" + str(x % 60)
    return m[-2:] + ":" +s[-2:]

def changeToInt(x):
    m, s = map(int, x.split(':'))
    return m * 60 + s

def go(S, s1):
    S[0] += changeToInt(s1) - changeToInt(prev)
    # global asum, bsum
    # if flag == 'a': asum += changeToInt(s1) - changeToInt(prev)
    # else: bsum += changeToInt(s1) - changeToInt(prev)
    return 

for _ in range(int(input())):
    team, goal_t = input().split()
    # edit win flag
    if A > B: go(asum, goal_t)
    elif B > A: go(bsum, goal_t)
    # compare prev / flag
    if team == '1': A += 1
    else: B += 1
    prev = goal_t
last = "48:00"
if A > B: go(asum, last)
elif B > A: go(bsum, last)
print(timeform(asum[0]))
print(timeform(bsum[0]))