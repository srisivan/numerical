# Equation is (x^2 - 2x - 15)/(x - 5)

x = float(4.990)
step = float(0.001)
y = 0

for i in range(1,10):
    x = x + step
    x = round(x,3)
    y = float((x*x) - (2*x) - 15)/float(x-5)
    y = round(y,4)
    print (y)
