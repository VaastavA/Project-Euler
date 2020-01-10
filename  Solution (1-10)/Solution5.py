import math
import collections

primes = [[] for i in range(21)]
ps = set()

def prime_factor(a):
	global ps
	pf = 2
	lpf = []
	q = a
	while pf<=q:
		if q in ps:
			lpf.extend(primes[q])
			return lpf	
  		if q%pf == 0:
    			temp = q//pf
    			q = temp
			lpf.append(pf)
  		else:
			pf += 1
	return lpf

ps.add(1)
real = collections.Counter()
for i in range(21):
	primes[i] = prime_factor(i)
	ps.add(i)
	temp = collections.Counter(primes[i])
	for j in temp.items():
		if real[j[0]] < j[1]:
			real[j[0]] = j[1]

sim = 1
for x in real.items():
	sim *= (x[0]**x[1])
print(sim)
