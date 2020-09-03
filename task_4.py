
import re
passwordStrength = 0
password= (input("Input your password "))
def passVal(p):
    if re.match("^[a-zA-Z]+$", password):
      passwordStrength = 0
    elif re.match("^([\s\d]+)$", password):
        passwordStrength += 1
    elif re.match('[\da-zA-Z]*$', password):
        passwordStrength += 2
    elif re.match(r"^[A-Za-z0-9_-]*$", password):
        print("Alpha Numeric")
    

passVal(password)
