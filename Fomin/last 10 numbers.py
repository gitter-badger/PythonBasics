"""Найдите 10 последних цифр в конечной сумме ряда 1^1 + 2^2 + 3^3 + ... + 1377^1377"""
a = sum(i ** i for i in range(1,1378))
print(str(a)[-10:])