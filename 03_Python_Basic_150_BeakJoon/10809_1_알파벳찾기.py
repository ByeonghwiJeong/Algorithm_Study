word = input()
# 아스키코드 a : 97  // z : 122
alphabet = list(range(97, 123))
for x in alphabet:
    print(word.find(chr(x)))