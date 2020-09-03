def palindromeChecker(checkString):
    #reversing the input string
    return checkString == checkString[::-1]

checkPalindromeWord = "madam"
isPalindrome = palindromeChecker(checkPalindromeWord)

if isPalindrome:
    print(f"{isPalindrome} is a palindrome")
else:
    print(f" {isPalindrome} is not a palidrome")
