# add_hex_to_R7_small.py
# Reads two 8-bit hex numbers from the user, computes their 8-bit sum and carry,
# and prints a minimal 8051 assembly sequence that stores the low byte into R7.

def parse_hex(s):
    s = s.strip().lower()
    if s.startswith("0x"):
        s = s[2:]
    return int(s, 16)

# Prompt user with clear instructions, read inputs
a_in = input("Enter first hex byte (00-FF, e.g. 3A or 0x3A): ")
b_in = input("Enter second hex byte (00-FF, e.g. C7 or 0xC7): ")

# Convert to integers and validate 8-bit range
try:
    a = parse_hex(a_in)
    b = parse_hex(b_in)
    if not (0 <= a <= 0xFF and 0 <= b <= 0xFF):
        raise ValueError
except Exception:
    print("Invalid input. Use 2-digit hex bytes 00..FF (optionally prefixed with 0x).")
    raise SystemExit(1)

# Compute 9-bit sum to get carry and low byte
total = a + b
carry = 1 if total > 0xFF else 0
result = total & 0xFF

# Display computed result and minimal 8051 assembly
print(f"\nResult: 0x{result:02X}  Carry: {carry}")
print("8051 assembly (stores low byte of sum into R7):")
print(f"    MOV A,#0x{a:02X}    ; load first operand into accumulator A")
print(f"    ADD A,#0x{b:02X}    ; add second operand, sets CY on overflow")
print("    MOV R7,A           ; move low 8 bits of sum into register R7")
