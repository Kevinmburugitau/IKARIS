def dfa_endswith01(input_string):
    state = 0  # q0 start state
    for char in input_string:
        if state == 0:
            if char == '0':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == '1':
                state = 2
            else:
                state = 1
        elif state == 2:
            if char == '0':
                state = 1
            else:
                state = 0
    return "Accepted" if state == 2 else "Rejected"

# User input
user_input = input("Enter a binary string: ")
print(f"{user_input} → {dfa_endswith01(user_input)}")

# Test
for s in ["01", "101", "1101", "111", "000"]:
    print(f"{s} → {dfa_endswith01(s)}")
