
t1 = 0
t2 = 1
sum = 0
cur = 0

while cur<4000000:
	cur = t1+t2
	temp = t1
	t1 = cur
	t2 = temp
	if cur%2==0:
		sum += cur
print(sum)
