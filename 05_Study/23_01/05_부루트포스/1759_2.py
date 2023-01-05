import sys
input = sys.stdin.readline

def is_valid(x):
    vowels = set("aeiou") # 모음저장
    count = 0 # 모음수
    for i in x:
        if i in vowels:
            count += 1
    return count >= 1 and len(x) - count >= 2

# idx:현재보고있는알파벳의index, cnt:남은알파벳의개수, x:현재까지 만들어진암호
def make_password(idx, cnt, x):
    if cnt == 0:
        if is_valid(x):
            answer.append(x)
        return

    if idx == len(alphabets):
        return
    
    make_password(idx + 1, cnt - 1, x + alphabets[idx])
    make_password(idx + 1, cnt, x)



n, m = map(int, input().split())
alphabets = list(input().split())

alphabets.sort()
answer = []     # 가능한 암호

make_password(0, n, "")
print(*answer, sep='\n')
