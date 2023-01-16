'''
palindrome 팰린드롬
뒤집어도 똑같은 문자
121 -> true
3333 -> true
90783 -> false
 ㄴ int
5 -> true
주어진 인자가 팰린드롬인지 확인하는 함수
str, array(list) 사용 금지
오직 int 만 사용
'''
def solution(x):
    l = 1
    tmp = x
    while True:  # 자리수 check ; l
        if x // 10**l == 0: # 1 : 
            break # 12321 >> 100000 = 10**5
        l += 1
    l -= 1 
    while l > 0:
        left = x // (10 ** l) # 
        right = x % 10 # 
        if left != right: return False
        x = (x % (10 ** l)) // 10
        l -= 2
    return True

print(solution(90783)) # 
print(solution(12321)) # 
print(solution(5)) # 

# print(1)