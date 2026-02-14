import math

def pour(fromCap, toCap, d):
    fromJug = fromCap
    toJug = 0
    step = 1  # filling fromJug

    while fromJug != d and toJug != d:
        # Find amount to pour
        transfer = min(fromJug, toCap - toJug)
        toJug += transfer
        fromJug -= transfer
        step += 1

        # If target reached
        if fromJug == d or toJug == d:
            break

        # If fromJug becomes empty, fill it
        if fromJug == 0:
            fromJug = fromCap
            step += 1

        # If toJug becomes full, empty it
        if toJug == toCap:
            toJug = 0
            step += 1

    return step


def min_steps(m, n, d):
    # Check if possible
    if d > max(m, n) or d % math.gcd(m, n) != 0:
        return -1  # Not possible
    
    # Try both ways and take minimum
    return min(pour(m, n, d), pour(n, m, d))


# ---- Input ----
m = int(input("Enter capacity of Jug 1: "))
n = int(input("Enter capacity of Jug 2: "))
d = int(input("Enter target amount: "))

steps = min_steps(m, n, d)

if steps == -1:
    print("Not possible")
else:
    print("Possible in", steps, "steps")