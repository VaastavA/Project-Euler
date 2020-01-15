m = 0

def is_palindrome(a):
	a = str(a)
	n = len(a)
	for x in range(n//2):
		if a[x] != a[n-x-1]:
			return False

	return True

for i in range(1000):
	for j in range(1000):
		k = i*j
		if is_palindrome(k):
			m = max(m,k)
print(m)
