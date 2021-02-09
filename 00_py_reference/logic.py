# %%

# notebook for generating logic tables
# https://en.wikipedia.org/wiki/Boolean_algebra

# Boolean AND

A = [False, True]
B = [False, True]

print("Boolean AND")

for a in A:
    for b in B:
        c = a and b
        print("{} AND {} = {}".format(a, b, c))

print()

A = [0b0, 0b1]
B = [0b0, 0b1]

print("Bitwise AND")

for a in A:
    for b in B:
        c = a & b
        print("{} & {} = {}".format(a, b, c))

print()

A = 0b1100
B = 0b1001

C = A & B

print("Bitwise example:")
print("  {:08b}\n& {:08b}\n  {:08b}".format(A, B, C))

# %%

# Boolean OR

A = [False, True]
B = [False, True]

print("Boolean OR")

for a in A:
    for b in B:
        c = a or b
        print("{} OR {} = {}".format(a, b, c))

print()

A = [0b0, 0b1]
B = [0b0, 0b1]

print("Bitwise OR")

for a in A:
    for b in B:
        c = a | b
        print("{} | {} = {}".format(a, b, c))

print()

A = 0b1100
B = 0b1001

C = A | B

print("Bitwise example:")
print("  {:08b}\n| {:08b}\n  {:08b}".format(A, B, C))

#%%

# Boolean XOR

A = [False, True]
B = [False, True]

print("Boolean XOR")

for a in A:
    for b in B:
        c = (a != b)
        print("{} XOR {} = {}".format(a, b, c))

print()

A = [0b0, 0b1]
B = [0b0, 0b1]

print("Bitwise XOR")

for a in A:
    for b in B:
        c = a ^ b
        print("{} ^ {} = {}".format(a, b, c))

print()

A = 0b1100
B = 0b1001

C = A ^ B

print("Bitwise example:")
print("  {:08b}\n^ {:08b}\n  {:08b}".format(A, B, C))

# %%

# Boolean NOT

A = [False, True]

print("Boolean NOT")
for a in A:
    b = not a
    print("NOT {} = {}".format(a, b))

print()

A = [0b0, 0b1]

print("Bitwise NOT via XOR")
for a in A:
    b = a ^ 0b1
    print("{} ^ 0b1 = {}".format(a, b))

print()

A = 0b1100

B = A ^ 0b11111111

print("Bitwise example:")
print("~{:08b}\n {:08b}".format(A, B))

# %%

# Bitwise complement

A = [0b0, 0b1]

print("Bitwise NOT via ~")
for a in A:
    b = ~a
    print("~ {} = {}".format(a, b))

print()

A = 0b1100

B = ~A

print("Bitwise example:")
print("~{:08b}\n {:08b}".format(A, B))

# ~ inverts the number's bits.
# The result looks like the 2's complement of a number.
# 2's complement is used to represent a negative number. 
# Python shows the result as the negative number.

# https://en.wikipedia.org/wiki/Ones%27_complement
# https://en.wikipedia.org/wiki/Two%27s_complement


# %%

# Boolean NAND

A = [False, True]
B = [False, True]

print("Boolean NAND")

for a in A:
    for b in B:
        c = not (a and b)
        print("{} NAND {} = {}".format(a, b, c))

print()

# %%

# Boolean NOR

A = [False, True]
B = [False, True]

print("Boolean NOR")

for a in A:
    for b in B:
        c = not (a | b)
        print("{} NOR {} = {}".format(a, b, c))

print()

# %%