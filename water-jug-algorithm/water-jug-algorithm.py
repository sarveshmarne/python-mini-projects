import math

def pour(fromCap, toCap, d):
    fromJug = fromCap
    toJug = 0
    steps = []
    step_count = 1

    steps.append(f"Fill {fromCap}L jug")

    while fromJug != d and toJug != d:
        # Pour from fromJug to toJug
        transfer = min(fromJug, toCap - toJug)
        toJug += transfer
        fromJug -= transfer
        step_count += 1
        steps.append(f"Pour {transfer}L from {fromCap}L jug to {toCap}L jug")

        if fromJug == d or toJug == d:
            break

        # If fromJug empty, fill it
        if fromJug == 0:
            fromJug = fromCap
            step_count += 1
            steps.append(f"Fill {fromCap}L jug")

        # If toJug full, empty it
        if toJug == toCap:
            toJug = 0
            step_count += 1
            steps.append(f"Empty {toCap}L jug")

    return step_count, steps


def min_steps_with_process(m, n, d):
    if d > max(m, n) or d % math.gcd(m, n) != 0:
        return -1, []

    # Try both directions
    steps1, process1 = pour(m, n, d)
    steps2, process2 = pour(n, m, d)

    if steps1 <= steps2:
        return steps1, process1
    else:
        return steps2, process2


# ---- Input ----
m = int(input("Enter capacity of Jug 1: "))
n = int(input("Enter capacity of Jug 2: "))
d = int(input("Enter target amount: "))

steps, process = min_steps_with_process(m, n, d)

if steps == -1:
    print("Not possible")
else:
    print(f"\nPossible in {steps} steps.\n")
    print("Procedure:")
    for i, step in enumerate(process, 1):
        print(f"{i}. {step}")
