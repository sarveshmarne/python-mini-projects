import random
import string

a = string.ascii_lowercase + string.ascii_uppercase + string.digits  + string.punctuation.replace("`","")
n = int(input("Enter the length of password: "))
b = random.sample(list(a), n)
print(''.join(b)) 