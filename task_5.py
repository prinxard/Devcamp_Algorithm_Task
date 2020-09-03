
def replaceString(checkString):
    strArr = list(checkString)
    for i, c in enumerate(strArr):
        if c == ' ': strArr[i] = '%20'
    return ''.join(strArr)
print(replaceString(" I am John "))
