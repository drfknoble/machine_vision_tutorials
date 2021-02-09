# %%

# Reference Sample

import time

i = 0
f = 0.0
A = False
B = False
C = False
op1 = 1
op2 = 2
res = 0.0
test = False

# Operators (strongest to weakest bindings)

test = A and (A and B) # Brackets have strongest binding

res = max(op1, op2) # Function

res = op1 ** op2 # Exponentation operator

res = -op1 # Negation operator
B = not A # not operator

res = op1 * op2 # Multiplication operator
res = op1 / op2 # Division operator
res = op1 % op2 # Modulo operator

res = op1 + op2 # Addition operator
res = op1 - op2 # Subtraction operator

test = op1 < op2 # Less than operator
test = op1 > op2 # Greater than operator
test = op1 <= op2 # Less than or equal to operator
test = op1 >= op2 # Greater than or equal to

test = op1 == op2 # Equality operator

C = A and B # AND operator

C = A != B # XOR operator

C = A or B # OR operator

# IF statement

if (A == B): # IF statement
    D = True

if (A == B): # IF-ELSE statement
    D = True
else:
    D = False

if (A == B): # IF-ELIF statement
    D = True
elif (A == C):
    D = False

# FOR statement

f = 0.0

for i in range(0, 5, 1):
    f = f + i
    # f += i

f = 0.0

for i in range(0, 5, 1):
    f = f + i

    if (f > 3):
        break

# WHILE statement

i = 0
f = 0.0

while f < 5:
    i = i + 1
    f = f + i

i = 0
f = 0.0

while f < 5:
    i = i + 1
    f = f + i

    if (f > 3):
        break

# Timer

D = False

now = time.time()
elapsed = 0.0

while (elapsed < 5.0):

    elapsed = time.time() - now
    
    if (elapsed > 3.0):
    
        D = True