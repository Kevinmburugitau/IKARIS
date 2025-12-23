import re

# Regex equivalent of NFA for "ab"
pattern = r"(a|b)*ab(a|b)*"

def nfa_ab(input_string):
    return "Accepted" if re.fullmatch(pattern, input_string) else "Rejected"

# User input
user_input = input("Enter a string of a's and b's: ")
print(f"{user_input} → {nfa_ab(user_input)}")

# Test
for s in ["ab", "aab", "baba", "xyz", "aa"]:
    print(f"{s} → {nfa_ab(s)}")
