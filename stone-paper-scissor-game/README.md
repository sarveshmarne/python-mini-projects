## Version 1 — Basic Match

**What It Does:**
- Creates a list of Stone, Paper, Scissor.
- Computer picks one option using `random.sample()`.
- User enters a choice:
  - If both match → Win
  - Else → Lose.

---

## Version 2 — Infinite Loop (Same Logic)

**What It Does:**
- Runs inside a while True loop.  
- User keeps entering choices.
- Win only if user input equals computer’s choice.

---

## Version 3 — Real Game Logic + Quit

**What It Does:**
- Computer chooses a new option every round.  
- User can type Quit to stop.  
- Validates input.
- Implements full game rules.  
- Shows computer’s choice + result (Win/Lose/Draw).

---

## Version 4 — Score System + Best-of Match

**What It Does:**
- Randomly selects match type: best of 3 / 5 / 7.
- Calculates required score to win.
- Tracks user score and computer score.
- Ends automatically when:
  - Someone reaches winning score
  - OR user types Quit.
- Shows final winner.

