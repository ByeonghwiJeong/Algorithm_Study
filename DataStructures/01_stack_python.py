stack = []

# 삽입(5, 2, 3, 7) - 삭제() - 삽입(1, 4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
# [1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력
# [5, 2, 3, 1]
