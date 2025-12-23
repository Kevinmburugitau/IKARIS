# recognizer_anbn.py
# Simple recursive recognizer and generator for L = { a^n b^n | n >= 0 }

def is_anbn(s: str) -> bool:
    """
    Recursive check for a^n b^n.
    Base: empty string is in the language.
    Inductive: if s starts with 'a' and ends with 'b', remove them and recurse.
    """
    # Check if all characters are 'a' or 'b'
    if any(ch not in ('a','b') for ch in s):
        return False

    # Base case: empty string is valid (n=0)
    if s == "":
        return True
    # If string is too short to be valid (must be at least "ab")
    if len(s) < 2:
        return False
    # If string starts with 'a' and ends with 'b', check the inside recursively
    if s[0] == 'a' and s[-1] == 'b':
        return is_anbn(s[1:-1])
    # Otherwise, not in the language
    return False

def generate_anbn(n):
    """
    Recursively generate all strings in a^n b^n for n from 0 up to given n.
    For each n, returns a list with a single string: n 'a's followed by n 'b's.
    """
    if n == 0:
        return [""]  # Base case: empty string for n=0
    else:
        prev = generate_anbn(n-1)  # Get all strings for n-1
        # For each string in prev, add 'a' at the start and 'b' at the end
        return ["a" + s + "b" for s in prev]

# User input: check if a string is in a^n b^n
user_input = input("Enter a string of a's and b's: ")
print(f"{user_input!r} -> {is_anbn(user_input)}")

# Test cases for recognizer
tests = ["", "ab", "aabb", "aaabbb", "aba", "abb", "ba", "aaaaabbbbb"]
for t in tests:
    print(f"{t!r:12} -> {is_anbn(t)}")

# Generate and print all strings in a^n b^n for n = 0 to 4
print("\nAll strings in a^n b^n for n = 0 to 4:")
for n in range(5):
    for s in generate_anbn(n):
        print(repr(s))
