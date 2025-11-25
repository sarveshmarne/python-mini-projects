import random
import string

four = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation.replace("`",""))
rest = string.ascii_lowercase + string.ascii_uppercase + string.digits  + string.punctuation.replace("`","")
random.shuffle(list(rest))
random.shuffle(list(''.join(random.sample(list(rest),int(input("number : ")) - 4)) + four))
print(''.join(list(''.join(random.sample(list(rest),int(input("number : ")) - 4)) + four)))