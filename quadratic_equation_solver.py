from math import *

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c

if D == 0:
    print(-b / (2*a))
elif D < 0:
    print("Нет корней")
else:
    x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) - sqrt(D)) / (2 * a)
    print(min(x1,x2), max(x1,x2), sep='\n')