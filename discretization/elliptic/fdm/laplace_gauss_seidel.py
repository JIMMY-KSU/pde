import numpy as np

def laplace_gauss_seidel():

  h = 0.1
  m = 10
  n = 10
  e = 0.0001
  omega = 1.5278

  u = np.zeros((n+1,m+1))
  uf = np.zeros((n+1,m+1))

  for i in range(n+1):
    for j in range(m+1):
      u[i][j] = e

  for j in range(m+1):
    u[0][j] = 0.0
    u[n][j] = 4 * h * j * (1 - h * j)

  for i in range(1,n):
    u[i][0] = 0.0
    u[i][m] = 0.0

  print("initail u:")
  for i in range(n+1):
    for j in range(m+1):
      print u[i][j],
    print ""

  nitr = 100
  for k in range(nitr):
    for j in range(1,m):
      for i in range(1,n):
        uf[i][j] = u[i][j]
        u[i][j] = u[i][j] + omega * ((u[i][j+1] + u[i][j-1] + u[i+1][j] + u[i-1][j]) / 4.0 - u[i][j])

    sum1 = 0.0
    sum2 = 0.0
    for j in range(1,n):
      for i in range(1,m):
        sum1 += abs(u[i][j] - uf[i][j])
        sum2 += abs(u[i][j])

    #print("sum1/sum2={0}".format(sum1/sum2))
    if (sum1 / sum2) <= e:
      break 

  print("k = {0}".format(k))

  print("result u:")
  for i in range(n+1):
    for j in range(m+1):
      print u[i][j],
    print ""

  return u

if __name__ == "__main__":
  laplace_gauss_seidel()
