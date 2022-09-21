'''
일련의 숫자가 있고, 이 숫자는 1씩 증가, 또는 감소한다. 
N 번째의 숫자가 있을 시에, 이 숫자가 7의 배수(7, 14, 21)이거나 7이란 숫자를 포함할 시에 (7, 17, 27) 방향을 바꾼다.

즉, 1, 2, 3, 4, 5, 6, [7], 6, 5, 4, 3, 2, 1, [0], 1, 2, [3], 2, 1, 0, [-1], 0, 1

과 같이 숫자는 진행한다. (첫번째 7은 7번째, 두번째 0은 14번째, 세번째 3은 17번째, 네번째 -1은 21번째)

다음의 제약 하에pingpong(x)의 함수를 작성하라. 예시의 인풋과 아웃풋은 다음과 같다.

pingpong(8) = 6

pingpong(22)=0

pingpong(68)=2

pingpong(100)=2

- For Loop / While 또는 Array를 쓰지 말 것
- Assignment 를 쓰지 말 것. 즉, 변수 할당을 하지 말 것.
- 스트링을 쓰지 말 것.
'''
def includeSeven(x):
    return (x - 1) % 10 == 7 or (x - 1) // 10 % 10 == 7 or (x - 1) // 100 % 10 == 7

def diff(x):
    if x == 1:
        return 1
    else:
        if (x - 1) % 7 == 0 or includeSeven(x):
            return -diff(x - 1)
        else:
            return diff(x - 1)

def pingpong(x):
    if x == 1:
        return 1
    else:
        return pingpong(x - 1) + diff(x)

print(pingpong(8))
print(pingpong(22))
print(pingpong(68))
print(pingpong(100))