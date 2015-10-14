# """Выводит первые N простых чисел в виде списка"""
a = []
b = 1
n = int(input('Input N '))
while len(a) < n:
	isprime = bool(1)
	for i in a[1:]:
		if b % i == 0: isprime = bool(0)
	if isprime: a.append(b)
	b += 1
print(a)
### оцени эффективность и подумай над более оптимальным ###