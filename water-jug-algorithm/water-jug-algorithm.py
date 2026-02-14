import math

def is_possible(m, n, d):
    # If target is greater than both jug capacities
    if d > max(m, n):
        return False
    
    # Check mathematical condition
    if d % math.gcd(m, n) == 0:
        return True
    
    return False


# Taking input
m = int(input("Enter capacity of Jug 1: "))
n = int(input("Enter capacity of Jug 2: "))
d = int(input("Enter target amount: "))

if is_possible(m, n, d):
    print("Yes, it is possible to measure", d, "liters.")
else:
    print("No, it is NOT possible to measure", d, "liters.")