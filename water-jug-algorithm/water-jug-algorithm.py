from collections import deque

def water_jug_problem(m, n, d):
    # Check if solution is possible
    if d > max(m, n):
        return "No solution possible"
    
    visited = set()
    queue = deque([(0, 0, [])])  # (jug1, jug2, path)

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))

        # Add current state to path
        path = path + [(jug1, jug2)]

        # If target reached
        if jug1 == d or jug2 == d:
            return path

        # Possible operations
        next_states = [
            (m, jug2),                # Fill Jug1
            (jug1, n),                # Fill Jug2
            (0, jug2),                # Empty Jug1
            (jug1, 0),                # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, n - jug2), jug2 + min(jug1, n - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, m - jug1), jug2 - min(jug2, m - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return "No solution found"


# Example
m = 4   # Jug1 capacity
n = 3   # Jug2 capacity
d = 2   # Target

solution = water_jug_problem(m, n, d)

print("Steps to reach solution:")
print(solution)
