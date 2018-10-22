
factor = 1
Q = 600851475143
for x in range(1,Q):
    if Q%x==0:
        factor = x
        print(factor)
        Q = Q/x
    if Q==1 : break;
print(71*839*1471*6857)