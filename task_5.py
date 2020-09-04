
def replaceString(checkString):
    strArr = list(checkString)
    for i, y in enumerate(strArr):
        if y == ' ': strArr[i] = '%20'
    return ''.join(strArr)
print(replaceString(" I am John abel"))
