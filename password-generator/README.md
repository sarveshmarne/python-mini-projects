## Version 1 — Basic Random Password

**What It Does:**
- Creates a single string containing all possible characters.
- Randomly selects `n` unique characters using `random.sample()`.

---

## Version 2 — Guaranteed 4-Category Password

**What It Does:**
- Ensures the password always contains at least:
  - 1 lowercase  
  - 1 uppercase  
  - 1 digit  
  - 1 symbol  
- Fills the remaining characters randomly.
- Shuffles everything to avoid predictable patterns.

---

## Version 3 — Loop + Validation Until Strong Password

**What It Does:**
- User enters password length.  
- Generates a random password.  
- Checks all conditions:
  - has lowercase  
  - has uppercase  
  - has digit  
  - has symbol  
- If conditions fail → generates again (loop).  
- Stops only when password is strong.  