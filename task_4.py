
import re

password= (input("Input your password "))
def passVal(p):
    passwordStrength = 0
    if re.match("^[a-zA-Z]+$", password):
      passwordStrength = passwordStrength
    elif re.match("^([\s\d]+)$", password):
        passwordStrength += 1
    elif re.match('[\da-zA-Z]*$', password):
        passwordStrength += 2
    elif re.match("^[A-Za-z0-9_-]*$", password):
        passwordStrength += 3
    if passwordStrength == 0:
        print("Very Weak Password")
    elif passwordStrength == 1:
        print("Weak Password")
    elif passwordStrength == 2:
        print("Strong Password")
    else:
        print("Very Strong Password")
passVal(password)

