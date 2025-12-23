# balanced_parens.py
# Recursive parser for balanced parentheses and brackets based on grammar:
# S -> ε | ( S ) S | [ S ] S

def parse_S(s: str, i: int) -> int:
    """
    Parse S starting at index i.
    Return next index after parsing S, or -1 if failure.
    Accepts both () and [] as matching brackets.
    """
    # Loop to handle multiple adjacent bracketed expressions (S S)
    while i < len(s) and s[i] in '([':
        open_bracket = s[i]  # Current opening bracket ('(' or '[')
        close_bracket = ')' if open_bracket == '(' else ']'  # Matching closing bracket
        i += 1  # Move past the opening bracket
        i = parse_S(s, i)  # Recursively parse the inner S
        # If parsing failed or no matching closing bracket, return failure
        if i == -1 or i >= len(s) or s[i] != close_bracket:
            return -1
        i += 1  # Move past the closing bracket
        # Continue loop to parse any trailing S (adjacent bracketed expressions)
    return i  # Return the index after parsing S

def is_balanced(s: str) -> bool:
    """
    Returns True if the string s is a balanced sequence of () and [] brackets.
    """
    i = parse_S(s, 0)  # Start parsing from index 0
    return i == len(s)  # Balanced if all input is consumed

# User input: check if a string is balanced
user_input = input("Enter a string of parentheses and brackets: ")
print(f"{user_input!r} -> {is_balanced(user_input)}")

# Test cases for recognizer
tests = [
    "", "()", "(())", "()()", "(()())", "(()", ")(", "())(",
    "[]", "[[]]", "[][]", "[()]", "([[]])", "([)]", "[(])", "([()[]])"
]
for t in tests:
    print(f"{t!r:10} -> {is_balanced(t)}")

# Demonstrate ambiguous and non-ambiguous parses
print("\nAmbiguous parse example: '[()][]'")
print("This string can be parsed as '[()]' then '[]', or as '[()[]]'.")
# Explanation: '[()][]' can be split as '[()]' + '[]' (two S's), or as '[()[]]' (one S inside brackets).

print("\nNon-ambiguous parse example: '([[]])'")
print("This string can only be parsed as '(' '[' '[' ']' ']' ')'.")
# Explanation: '([[]])' has only one valid parse tree due to strict nesting.
