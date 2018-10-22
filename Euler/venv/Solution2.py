sum = 0
x_c = 1
x_p = 0

while(x_c<4000000):
    if x_c%2==0:
        sum+=x_c
    x_c+=x_p
    x_p = x_c-x_p
print(sum)