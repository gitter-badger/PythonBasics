n = int(input('Input N '))
a = [i for i in range(1,n+1)]
i = 1
m = len(a)
while i != len(a):
	n = a[i]
	a = set(a)
	b = {n*c for c in range(2, m // n + 1)}
	a = list(a - b)
	a.sort()
	i += 1
print(a)
### Простые числа до числа N по решету Эратосфена ###