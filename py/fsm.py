def automaton(input_string):
    # Define the initial state (state 0)
    state = 0  # Start state

    # Process each character in the input string
    for char in input_string:
        # Transition based on current state and input character
        if state == 0:
            # If in state 0 and input is '0', move to state 1
            if char == '0':
                state = 1
            # If in state 0 and input is '1', stay in state 0
            else:  # char == '1'
                state = 0
        elif state == 1:
            # If in state 1 and input is '0', stay in state 1
            if char == '0':
                state = 1
            # If in state 1 and input is '1', move to state 2 (accepting state)
            else:  # char == '1'
                state = 2
        elif state == 2:
            # If in state 2 and input is '0', move to state 1
            if char == '0':
                state = 1
            # If in state 2 and input is '1', move back to state 0
            else:
                state = 0

    # After processing all characters, check if we're in the accepting state (state 2)
    if state == 2:
        return "Accepted"
    else:
        return "Rejected"

# Get input from the user
user_input = input("Enter a binary string: ")
# Run the automaton with the user's input
result = automaton(user_input)
# Print the result
print(f"Result: {result}")
