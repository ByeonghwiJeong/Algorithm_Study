_number = ['one', 'two', 'three', 'four']
_num = [1, 2, 3, 4]
_dict = dict((zip(_number, _num)))

print(sorted(_dict))
# ['four', 'one', 'three', 'two']
print(sorted(_dict.items()))
# [('four', 4), ('one', 1), ('three', 3), ('two', 2)]
