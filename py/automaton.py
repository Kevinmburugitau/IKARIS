state = "q0"

while True:
    symbol = input("Enter a binary: ").strip()

    if all (char in '01' for char in symbol):
        print("Valid binary input!")
        break
    else:
        print("Invalid input. Please enter only binary digits (0 or 1).")

for ch in symbol:
#   state = transitions[state][ch]
    if state == "q0":
        state = "q1" if ch == "1"  else "q0"
    elif state == "q1":
        state = "q0" if ch == "0" else "q1"

print (symbol)
print(f"Final state: {state}")

if state == "q1":
    print("Accepted")
else:
    print("Rejected")