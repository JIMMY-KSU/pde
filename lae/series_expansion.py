from math import *
h = 0.1
m = 10
n = 10
for j in range(n+1):
  y = h * j
  for i in range(m+1):
    x = h * i
    sum=0.0
    for k in range(1,11):
      sum+=(sin((2*k-1)*pi*x)*sinh((2*k-1)*pi*y))/((2*k-1)**3*sinh((2*k-1)*pi))
    u=(32/pi**3)*sum
    print("y = {0}, x = {1}, u = {2}".format(y,x,u))
