a = []
b = 1
n = int(input())
while len(a) < n:
	isprime = bool(1)
	for i in a[1:]:
		if b % i == 0: isprime = bool(0)
	if isprime: a.append(b)
	b += 1
print(a)