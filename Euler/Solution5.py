
factor = 2520
factors = []

for x in range(1, 1260):
    if factor % x == 0 and x > 1:
        factors.append(x)
        factor /= x
print(factors)
print(factor)

print(2520*11*13*17*19*2)
