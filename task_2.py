def numIsPrime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    elif (n == 0):
        return "Number must be greater than 0"
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


print(numIsPrime(9))
        
    
