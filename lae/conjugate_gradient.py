from laesolver import LAESolver
import numpy as np

class ConjugateGradient(LAESolver):

  def solve(self, mat, rhs):
    mat_a = np.array(mat)
    vec_b = np.array(rhs)
    vec_x = np.zeros(len(vec_b))
    vec_r = np.zeros(len(vec_b))
    vec_rn = np.zeros(len(vec_b))
    vec_p = np.zeros(len(vec_b))

    vec_r = vec_b - np.dot(mat_a, vec_x)

    vec_p = np.copy(vec_r)

    nitr = 100
    for k in range(nitr):
      alpha = np.dot(vec_r, vec_r) / np.dot(vec_p, np.dot(mat_a, vec_p))
      vec_x = vec_x + alpha * vec_p
      vec_rn = vec_r - alpha * np.dot(mat_a, vec_p)
      
      if(np.dot(vec_rn, vec_rn) < 0.0001):
        break
      beta = np.dot(vec_rn, vec_rn) / np.dot(vec_r, vec_r) 
      vec_p = vec_rn + beta * vec_p

      vec_r = vec_rn
    return vec_x
