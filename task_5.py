
def replaceString(s):
    strArr = list(s)
    for i, c in enumerate(strArr):
        if c == ' ': strArr[i] = '%20'
    return ''.join(strArr)
print(replaceString(" I am John "))
