# python-mini-projects
A collection of Python mini projects demonstrating fundamentals like loops, conditionals, functions, OOP, file handling, and utilities.

Version 1 — Basic Random Password
What It Does:
Creates a single string containing all possible characters.
Randomly selects n unique characters using random.sample().

Version 2 — Guaranteed 4-Category Password
What It Does:
Ensures the password always contains at least: 1 lowercase and 1 uppercase and 1 digit and 1 symbol.
Fills the remaining characters randomly.
Shuffles everything to avoid pattern (abcd1@Xz randomly mixed).

Version 3 — Loop + Validation Until Strong Password
What It Does:
User enters password length.
Generates a random password.
Checks all conditions: has lowercase and has uppercase and has digit and has symbol.
If conditions fail → generates again (loop).
Stops only when password is strong.
