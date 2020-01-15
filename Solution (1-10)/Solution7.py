primes = []
cur = 2
while len(primes)<10001:
  p = True
  for x in primes:
    if cur%x == 0:
      p = False
      break
  
  if p:
    primes.append(cur)
  cur += 1
print(primes)
