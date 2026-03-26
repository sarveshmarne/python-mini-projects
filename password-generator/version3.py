import random
import string

a = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation.replace("`","")

while True:
    password = ''.join(random.choice(a) for _ in range (int(input("Enter the number :")))) 
    
    lower = any(c in string.ascii_lowercase for c in password)
    upper = any(c in string.ascii_uppercase for c in password)
    digit = any(c in string.digits for c in password)
    punc = any(c in string.punctuation for c in password)
    
    if lower and upper and digit and punc:
        print(password)
        break 