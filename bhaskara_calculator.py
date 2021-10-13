from math import sqrt

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

delta = b**2 - 4*a*c

if delta < 0:
    result = 'Not real'

elif delta == 0:
    result = -b/2*a

else:
    result = ((-b + sqrt(delta))/2*a, ((-b-sqrt(delta))/2*a))

print(result)