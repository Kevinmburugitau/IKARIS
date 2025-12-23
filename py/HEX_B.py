#!/usr/bin/env python3
# Compact 8051-like simulator: supports MOV A,#imm, ADD A,#imm, MOV R7,A
# Keeps A and R7 as 8-bit; updates flags C, AC, P. Retries on invalid input.

def to_byte(x): return x & 0xFF                          # mask to 8 bits
def parse_hex(s):                                        # accept BE, BEh, 0xBE
    t = s.strip().lower()
    if t.endswith('h'): t = t[:-1]
    if t.startswith('0x'): t = t[2:]
    return int(t, 16)

def parity(v): return 1 if bin(v & 0xFF).count("1") % 2 else 0
def aux_carry(a, b): return 1 if ((a & 0x0F) + (b & 0x0F)) > 0x0F else 0
def carry(a, b): return 1 if (a + b) > 0xFF else 0

A = 0x00                # accumulator
R7 = 0x00               # register R7
C = AC = P = 0          # flags

def state():             # print current state
    print(f"A=0x{A:02X} R7=0x{R7:02X}  C={C} AC={AC} P={P}")

def exec_line(line):
    global A, R7, C, AC, P
    code = line.split(';',1)[0].strip()                # drop comments
    if not code: return
    parts = [p for p in code.replace(',', ' ').split() if p]
    op = parts[0].upper()
    if op == "MOV" and len(parts) == 3:
        dst, src = parts[1].upper(), parts[2]
        if dst == "A":
            if src.upper().startswith('R') and src[1:] == '7':
                A = to_byte(R7)                        # MOV A,R7
            elif src.startswith('#'):
                A = to_byte(parse_hex(src[1:]))      # MOV A,#imm
            else:
                raise ValueError("unsupported MOV src")
            P = parity(A)                             # parity depends on A
        elif dst == "R7":
            if src.upper() == "A":
                R7 = to_byte(A)                       # MOV R7,A
            elif src.startswith('#'):
                R7 = to_byte(parse_hex(src[1:]))     # MOV R7,#imm
            else:
                raise ValueError("unsupported MOV src")
        else:
            raise ValueError("unsupported MOV dst")
    elif op == "ADD" and len(parts) == 3:
        dst, src = parts[1].upper(), parts[2]
        if dst != "A": raise ValueError("only ADD A,src supported")
        if src.startswith('#'):
            val = to_byte(parse_hex(src[1:]))         # immediate value
        elif src.upper() == "R7":
            val = R7                                  # register R7
        else:
            raise ValueError("unsupported ADD src")
        AC = aux_carry(A, val)
        C = carry(A, val)
        A = to_byte(A + val)                          # store low 8 bits
        P = parity(A)
    else:
        raise ValueError("unsupported instruction")

# interactive loop with retry on invalid input
print("Compact 8051 simulator. Examples: MOV A,#BEh  ADD A,#C9h  MOV R7,A  EXIT")
state()
while True:
    try:
        line = input("> ").strip()
        if not line: continue
        if line.upper() in ("EXIT","QUIT"): break
        try:
            exec_line(line)
        except Exception as e:
            print("Invalid input:", e)    # report error
            continue                      # loop again for correction
        state()
    except (EOFError, KeyboardInterrupt):
        print(); break
