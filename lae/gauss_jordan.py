from laesolver import LAESolver
import numpy as np

class GaussJordan(LAESolver):
  def solve(self, mat, rhs):
    emat = []
    for row, b in zip(mat, rhs):
      row.append(b)
      emat.append(row)
  
    mat = np.array(emat)
  
    for k in range(len(mat)):
      mat_kk = mat[k,k]
      for j in range(len(mat[k])):
        mat[k,j] = mat[k,j] / mat_kk
      for i in range(len(mat)):
        if i == k:
          continue
        mat_ik = mat[i,k]
        for j in range(len(mat[i])):
          mat[i,j] = mat[i,j] - mat_ik * mat[k,j] 

    return mat[:,len(mat)]
