import sys
input = sys.stdin.readline

vowel = set(['a', 'e', 'i', 'o', 'u'])

while True:
    s = input().rstrip()
    if s == "end": break
    lcnt = 0
    vcnt = 0
    is_include_v = 0
    flag = 1 # True
    prev = -1;
    for i, v in enumerate(s):
        if v in vowel:
            lcnt += 1 # 연속모음수
            vcnt = 0 # 연속자음수
            is_include_v = 1
        else:
            lcnt = 0
            vcnt += 1
        if vcnt == 3 or lcnt == 3: flag = 0 # False
        if i >= 1 and prev == v and v not in ['e','o']:
            flag = 0
        prev = v
    if not is_include_v: 
        flag = 0
    if flag: print(f'<{s}> is acceptable.')
    else: print(f'<{s}> is not acceptable.')
    