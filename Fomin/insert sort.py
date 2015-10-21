import random
a = [random.randint(1,10000) for i in range(10000)]
print(a)
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if a[i] > a[j]: a[i], a[j] = a[j], a[i]
print(a)