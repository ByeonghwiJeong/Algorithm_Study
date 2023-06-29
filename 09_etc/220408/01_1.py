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
    
    while "AWS" in s:
        s = s.replace("AWS", "")
    if not s:
        return "-1"
    return s

