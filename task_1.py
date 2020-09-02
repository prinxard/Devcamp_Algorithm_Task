
evenOddArr = []
numArr = [1, 2, 3, 4, 5, 6]
def sumEvenOdd(numArr): 
    even = 0
    odd = 0

    for i in numArr:
        if i % 2 == 0:
            # print(i)
            even += i
        else:
            # print(i)
            odd += i 
      
    evenOddArr.append(even)
    evenOddArr.append(odd)
    print(f"Array containing sum of even and odd number => {evenOddArr}")
     
sumEvenOdd(numArr)
