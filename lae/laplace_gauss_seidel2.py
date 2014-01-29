def laplace_gauss_seidel():
  import numpy as np
  import sys

  h = 0.1
  k = h
  m = 2.0 / h
  n = 1.0 / k
  e = 0.0001
  mu = np.cos(np.pi / m) + np.cos(np.pi / n)
  omega = 2 / (1 + np.sqrt(1 - (mu / 2) ** 2))
  print("h = {0}, k = {1}, m = {2}, n = {3}".format(h,k,m,n))

  u = np.zeros((n+1,m+1))
  uf = np.zeros((n+1,m+1))

  for j in range(n+1):
    for i in range(m+1):
      u[j][i] = e

  for i in range(m+1):
    u[0][i] = 0.0
    u[n][i] = 0.5 * h * i

  for j in range(1,n):
    u[j][m] = k * j

  print("initail u:")
  for j in range(n+1):
    for i in range(m+1):
      print u[j][i],
    print ""

  nitr = 100
  for k in range(nitr):
    for i in range(m):
      for j in range(1,n):
        uf[j][i] = u[j][i]
        if i == 0:
          u[j][i] = u[j][i] + omega * ((2 * u[j][i+1] + u[j+1][i] + u[j-1][i]) / 4.0 - u[j][i])
        else:
          u[j][i] = u[j][i] + omega * ((u[j][i+1] + u[j][i-1] + u[j+1][i] + u[j-1][i]) / 4.0 - u[j][i])

    sum1 = 0.0
    sum2 = 0.0
    for j in range(1,n):
      for i in range(1,m):
        sum1 += abs(u[j][i] - uf[j][i])
        sum2 += abs(u[j][i])

    #print("sum1/sum2={0}".format(sum1/sum2))
    if (sum1 / sum2) <= e:
      break 

  print("k = {0}".format(k))

  print("result u:")
  for j in range(n+1):
    for i in range(m+1):
      print u[j][i],
    print ""

if __name__ == "__main__":
  laplace_gauss_seidel()
