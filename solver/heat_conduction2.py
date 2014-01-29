def heat_conduction():
  #import numpy as np
  
  m = 10
  n = 300
  u = []

  kai = 0.07
  h = 0.1
  a = 0.5
  k = a * h ** 2.0 / (2 * kai)
  #k = 0.07
  r = kai * k / h ** 2

  print("kai = {0}, h = {1}, k = {2}, r = {3}".format(kai,h,k,r))

  for i in range(m+1):
    u.append(0.0)

  u[0] = 0.0
  u[m] = 100.0

  print("initial u:")
  print u

  for j in range(n+1):
    for i in range(1,m):
      u[i] = (1 - 2 * r) * u[i] + r * (u[i+1] + u[i-1])

    print("j = {0} time = {1} h".format(j,j*k))
    print u

if __name__ == "__main__":
  heat_conduction()
