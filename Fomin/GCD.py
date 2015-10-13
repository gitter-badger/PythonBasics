"""выводит НОД двух чисел"""
a = int(input())
b = int(input())
if a < b :
	a, b = b, a
for c in range(b):
	i = b-c
	if a % i == 0 and b % i == 0 : break
print(i)