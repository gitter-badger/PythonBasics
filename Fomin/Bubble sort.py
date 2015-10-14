""""сотрировка пузырьком"""
from random import randint
n = 10000
a = [randint(0,100) for x in range(n)]
print(a)
c = 1
while c != 0 :
 c = 0
 for x in range(n-1):
  if a[x] > a[x+1]:
   a[x], a[x+1] = a[x+1], a[x]
   c+=1
print(a)
### переделай, как обычно - через два цикла for ###