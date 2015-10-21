n = int(input('Input N '))
a = [i for i in range(1,n+1)]
i = 1
while i != len(a):
	m = a[i]
	a = set(a)
	b = {m*c for c in range(2, n // m + 1)}
	a = list(a - b)
	i += 1
a.sort()
print(a)
### Простые числа до числа N по решету Эратосфена ###