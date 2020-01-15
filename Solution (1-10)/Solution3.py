import math 

pf = 1
lpf = 1
p = math.sqrt(600851475143)
q = 600851475143
while pf<p and pf<q:
  if q%pf == 0:
    lpf = q//pf
    q = lpf
  pf += 1

print(lpf)
