import numpy as np

class LAESolver:
  def __init__(self, mat, rhs):
    self.mat = mat
    self.rhs = rhs

class GaussSeidel(LAESolver):

  def solve(self):
    mat_a = np.array(self.mat)
    vec_b = np.array(self.rhs)
    vec_x = np.zeros(len(vec_b))
    vec_r = np.zeros(len(vec_b))
  
    nitr = 100
    for k in range(nitr):
      for i in range(len(vec_x)):
        vec_r[i] = vec_x[i]
  
      for i in range(len(mat_a)):
        sum = 0.0
        for j in range(len(mat_a[i])):
          if i != j:
            sum += mat_a[i][j] * vec_x[j] 
        vec_x[i] = (vec_b[i] - sum) / mat_a[i][i]
  
      flag = False
      for i in range(len(vec_x)):
        if abs(vec_x[i] - vec_r[i]) > 0.00001:
          flag = True
  
      if flag == False:
        break
  
    return vec_x
