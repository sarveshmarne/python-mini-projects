import math

def pour(fromCap, toCap, d):
    fromJug = fromCap
    toJug = 0
    steps = []
    step_count = 1

    steps.append(f"Step 1: Fill {fromCap}L Jug")

    while fromJug != d and toJug != d:
        transfer = min(fromJug, toCap - toJug)
        toJug += transfer
        fromJug -= transfer
        step_count += 1
        steps.append(f"Step {step_count}: Pour {transfer}L from {fromCap}L Jug to {toCap}L Jug")

        if fromJug == d or toJug == d:
            break

        if fromJug == 0:
            fromJug = fromCap
            step_count += 1
            steps.append(f"Step {step_count}: Fill {fromCap}L Jug")

        if toJug == toCap:
            toJug = 0
            step_count += 1
            steps.append(f"Step {step_count}: Empty {toCap}L Jug")

    if fromJug == d:
        final_statement = f"\nResult: {d}L remains in the {fromCap}L Jug."
    else:
        final_statement = f"\nResult: {d}L remains in the {toCap}L Jug."

    return step_count, steps, final_statement


def water_jug(m, n, d):
    print("\n----- WATER JUG PROBLEM -----")
    print(f"Jug 1 Capacity : {m}L")
    print(f"Jug 2 Capacity : {n}L")
    print(f"Target         : {d}L\n")

    if d > max(m, n) or d % math.gcd(m, n) != 0:
        print("Result: Not Possible")
        return

    steps1, process1, final1 = pour(m, n, d)
    steps2, process2, final2 = pour(n, m, d)

    if steps1 <= steps2:
        print("Minimum Steps :", steps1)
        print("\nProcedure:")
        for step in process1:
            print(step)
        print(final1)
    else:
        print("Minimum Steps :", steps2)
        print("\nProcedure:")
        for step in process2:
            print(step)
        print(final2)


# ---- Main Program ----
m = int(input("Enter capacity of Jug 1: "))
n = int(input("Enter capacity of Jug 2: "))
d = int(input("Enter target amount: "))

water_jug(m, n, d)