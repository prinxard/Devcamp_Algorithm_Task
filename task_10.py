
checkString = "testsringsesesewwwwwwwwyyyyyyyy"
all_freq = {}
def maximumString(checkString):
    for i in checkString: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    result = max(all_freq, key = all_freq.get)  
  
    print (f"The maximum of all characters in {checkString} is : " + str(result))


maximumString(checkString)
