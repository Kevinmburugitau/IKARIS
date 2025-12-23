# Program: recognize strings that end with "01"
# Author: Copilot (example)
# Usage: run the script and type a binary string when prompted (only '0' and '1' allowed)
# The program implements a simple DFA (deterministic finite automaton)
# that accepts exactly those binary strings whose last two characters are "01".

def transition_graph_ends01(input_string):
    # States:
    # q0 - start state; no relevant suffix seen yet
    # q1 - the last character seen was '0' (suffix "...0")
    # q2 - the last two characters seen are '01' (accepting state)
    #
    # We only need to track the last up to two characters to decide acceptance.
    # The DFA updates its state for each incoming character.

    state = "q0"

    for idx, char in enumerate(input_string):
        # Input validation: only '0' and '1' are allowed
        if char not in ("0", "1"):
            raise ValueError(f"Invalid character at position {idx}: {char}")

        # State transition table implemented as conditional logic
        if state == "q0":
            # From q0:
            #  - input '0' moves to q1 because the suffix could become "...0"
            #  - input '1' stays in q0 because suffix "...1" is not the start of "01"
            if char == "0":
                state = "q1"
            else:  # char == "1"
                state = "q0"
        elif state == "q1":
            # From q1 (we have seen a trailing '0'):
            #  - input '0' stays in q1 (still trailing '0')
            #  - input '1' moves to q2 because we just saw "...01"
            if char == "0":
                state = "q1"
            else:  # char == "1"
                state = "q2"
        elif state == "q2":
            # From q2 (the last two characters were '01'):
            # On a new input, we must update the trailing suffix:
            #  - input '0' makes the new suffix end with '0' -> go to q1
            #  - input '1' makes the new suffix end with '1' -> go to q0
            if char == "0":
                state = "q1"
            else:  # char == "1"
                state = "q0"

    # Accept if the machine ends in the accepting state q2
    return state == "q2"


if __name__ == "__main__":
    # Read a string from the user
    s = input("Enter a binary string (only 0 and 1): ").strip()

    # Guard: empty string is allowed; it will be rejected because it doesn't end with "01"
    try:
        accepted = transition_graph_ends01(s)
    except ValueError as err:
        print("Error:", err)
    else:
        print(f"{s} → {'Accepted' if accepted else 'Rejected'}")
