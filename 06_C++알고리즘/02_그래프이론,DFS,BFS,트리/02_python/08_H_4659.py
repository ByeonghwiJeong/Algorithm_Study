import sys
input = sys.stdin.readline

vowel = {'a', 'e', 'i', 'o', 'u'}

while (s:=input().rstrip()) != "end":
    lcnt = 0 # 연속모음수
    vcnt = 0 # 연속자음수
    is_include_v = False
    flag = True # True
    prev = -1;
    for i, v in enumerate(s):
        if v in vowel:
            lcnt += 1 
            vcnt = 0 
            is_include_v = True
        else:
            lcnt = 0
            vcnt += 1
        if i >= 1 and prev == v and v not in {'e','o'}:
            flag = False
            break
        if vcnt == 3 or lcnt == 3: 
            flag = False
            break 
        prev = v
    if not is_include_v: 
        flag = 0
    if flag: print(f'<{s}> is acceptable.')
    else: print(f'<{s}> is not acceptable.')
    