def gauss():
  import numpy as np
  #a = [[1.0, 2.0, 1.0], [3.0, 4.0, 2.0]]
  a = [[1.0,  1.0, -2.0, 3.0], 
       [5.0,  2.0,  1.0, 1.0],
       [1.0, -4.0,  3.0, 8.0]]
  mat = np.array(a)

  print("initail matrix:")
  print(mat)

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

  print("result matrix:")
  print(mat)

if __name__ == "__main__":
  gauss()
