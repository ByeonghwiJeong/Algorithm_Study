'''
Elimninate Substrings

Example:

'''
# Elimninate Substrings : AWS
# AWAWSSG -> AWSSG
# AAWSWS -> -1
# 7 ~ 4
def getFinalString(s):
    # Write your code here
    stack = []
    a = "AWS"
    for i in s:
        stack.append(i)
        if len(stack) >= 3:
            if "".join(stack[-3:]) == a:
                stack.pop()
                stack.pop()
                stack.pop()
    if stack:
        return "".join(stack)
    else:
        return "-1"
