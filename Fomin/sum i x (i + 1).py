"""Выводит сумму последовательности 1*2 + 2*3 + ... + (n-1)*n"""
n = int(input('Enter the last term of sequenсe'))
print(sum(i * (i+1) for i in range(n)))