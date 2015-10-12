n = 0
for i in range(1,13702):
	b = str(i)
	c = 0
	while b != b[-1::-1]:
		if c == 51:
			n += 1
			break
		b = str(int(b) + int(b[-1::-1]))
		c += 1
print(n)