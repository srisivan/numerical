# Equation is (x^2 + 12x + 27)/(x + 3)

x = float(-2.99)
step = float(-0.001)
y = 0

for i in range(1,10):
    x = x + step
    x = round(x,3)
    y = float((x*x) + (12*x) + 27)/float(x+3)
    y = round(y,4)
    print (y)
