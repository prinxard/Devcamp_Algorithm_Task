
test_str = "testsringsesesee"
all_freq = {}
def maximumString(test_str):
    for i in test_str: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    res = max(all_freq, key = all_freq.get)  
  
    print (f"The maximum of all characters in {test_str} is : " + str(res))


maximumString(test_str)
