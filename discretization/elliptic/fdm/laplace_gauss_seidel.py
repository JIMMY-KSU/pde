import numpy as np
from gauss_jordan import GaussJordan

class Laplace:
  def __init__(self):
    pass

  def solve(self):
  
    #h = 0.1
    m = 10
    n = 10
    e = 0.0001
    omega = 1.5278
    ngrids = (m+1)*(n+1)

    h = 0.1
    k = 0.1
  
    u = np.zeros((m+1,n+1))
    uf = np.zeros((m+1,n+1))
    a = np.zeros((ngrids,ngrids))
    c = np.zeros(ngrids)
    mat = []
  
    # set boundary condition
    for i in range(m+1):
      for j in range(n+1):
        #u[i][j] = e
        u[i][j] = 0.0
  
    for j in range(n+1):
      u[0][j] = 0.0
      u[m][j] = 4 * h * j * (1 - h * j)
  
    for i in range(1,m):
      u[i][0] = 0.0
      u[i][n] = 0.0
  
    #print("initail u:")
    #for i in range(n+1):
    #  for j in range(m+1):
    #    print u[i][j],
    #  print ""

    # set coefficient matrix
    for i in range(ngrids):
      if i >= (n+1) and i < (n+1) * m and (i % (n + 1)) != 0 and ((i - n) % (n + 1)) != 0:
        for j in range(ngrids):
          if j == (i - (n + 1)) or j == (i + n + 1):
            a[i][j] = h * h
          elif j == (i - 1) or j == (i + 1):
            a[i][j] = k * k
          elif j == i:
            a[i][j] = -2.0 * (h * h + k * k)

    #print "a:"
    #for i in range(ngrids):
    #  for j in range(ngrids):
    #    print a[i][j],
    #  print ""

    #print "u:"
    #for i in range(m+1):
    #  for j in range(n+1):
    #    print u[i,j]

    for i in range(ngrids):
      for j in range(ngrids):
        c[i] += a[i][j] * u[int(j/(n+1)),j%(n+1)]

    #print "c:"
    #for i in range(ngrids):
    #  print c[i]

    for i in range(ngrids):
      if i >= (n+1) and i < (n+1) * m and (i % (n + 1)) != 0 and ((i - n) % (n + 1)) != 0:
        mat.append([])
        for j in range(ngrids):
          if j >= (n+1) and j < (n+1) * m and (j % (n + 1)) != 0 and ((j - n) % (n + 1)) != 0:
            mat[len(mat)-1].append(a[i,j])
        mat[len(mat)-1].append(-c[i])

    #print "mat:"
    #for row in mat:
    #  for item in row:
    #    print item,
    #  print ""

    mat_ = np.array(mat)
  
    lae = GaussJordan()
    return lae.solve(mat_[:,:len(mat)].tolist(),mat_[:,len(mat)].tolist())
    

    #nitr = 100
    #for k in range(nitr):
    #  for j in range(1,n):
    #    for i in range(1,m):
    #      uf[i][j] = u[i][j]
    #      u[i][j] = u[i][j] + omega * ((u[i][j+1] + u[i][j-1] + u[i+1][j] + u[i-1][j]) / 4.0 - u[i][j])
  
    #  sum1 = 0.0
    #  sum2 = 0.0
    #  for j in range(1,m):
    #    for i in range(1,n):
    #      sum1 += abs(u[i][j] - uf[i][j])
    #      sum2 += abs(u[i][j])
  
    #  #print("sum1/sum2={0}".format(sum1/sum2))
    #  if (sum1 / sum2) <= e:
    #    break 
  
    #print("k = {0}".format(k))
  
    #print("result u:")
    #for i in range(n+1):
    #  for j in range(m+1):
    #    print u[i][j],
    #  print ""
  
    #return u
