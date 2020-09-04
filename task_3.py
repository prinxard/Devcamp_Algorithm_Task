numberList = [4, 5, 6, 7, 8, 9, 10, 11, 13, 21,12]
primes = []
def showPrimes(numbers):  
    for num in numbers:
        if num == 2:
            primes.append(num)
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)
                print(num)

    return len(primes)


print(showPrimes(numberList))
