a = [False for x in range(1000)]

sum = 0

for i in range(0,1000,3):
	if a[i] == False:
		a[i] = True
		sum += i

for i in range(0,1000,5):
	if a[i] == False:
		a[i] = True
		sum += i
print(sum)
