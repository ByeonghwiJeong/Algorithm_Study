import sys
input = sys.stdin.readline

# 초기 문자열과 명령어 수 입력
left_stack = list(input().rstrip()) 
right_stack = []

# 명령어 처리
for _ in range(int(input())):
    command = input().split()
    match command[0]:
        case 'L' if left_stack:
            right_stack.append(left_stack.pop())
        case 'D' if right_stack:
            left_stack.append(right_stack.pop())
        case 'B' if left_stack:
            left_stack.pop()
        case 'P':
            left_stack.append(command[1])

# 결과 출력
print(''.join(left_stack + right_stack[::-1]))
