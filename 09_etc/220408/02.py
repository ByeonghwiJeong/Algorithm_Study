'''
< Error Digit Range >

111
- 999
- 111
>> 888

10018
- 90098
    - 첫번째 자리가 9가 아니면 9로 바꿔준다.
    - 첫번째 자릭가 9이면 두번째자리 check
        - 이후에 숫자가 9가 아니면 9로 바꿔준다. 
- 10010
    - 첫번째 자리수가 1이 아니면 1로 바꿔준다.
    - 첫번째 자리수가 1이면 두번째자리 check
        - 두번째 자리가 0 or 1이 아니면 0으로 바꿔준다.
        - 두번째 자리가 0 or 1이 이면 
            -이후에 1과 0이 아닌 수를 찾아서 0으로

112233445
- 992233445
- 110033445
'''
def findRange(num):
    # Write your code here
    _max = num
    _min = num
    S = str(num)
    for s in S:
        if s == "9": continue
        else: 
            _max = int(S.replace(s, "9"))
            break
    for i, s in enumerate(S):
        if i == 0 and s != "1":
            _min = int(S.replace(s, "1"))
            break
        else:
            if s == "1" or s == "0":
                continue
            else:
                _min = int(S.replace(s, "0"))
                break
    print(_max, _min)
    return _max - _min

print(findRange(112233445))