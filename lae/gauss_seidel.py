def gauss_seidel():
  import numpy as np
  a = [[2.0,  1.0,  1.0], 
       [2.0,  3.0,  1.0],
       [1.0,  1.0,  3.0]]
  b = [2.0, 4.0, -1.0]
  mat_a = np.array(a)
  vec_b = np.array(b)
  vec_x = np.zeros(len(vec_b))
  vec_r = np.zeros(len(vec_b))

  print("initail matrix a:")
  print(mat_a)
  print("initail vec b:")
  print(vec_b)


  print("initail vec x:")
  print(vec_x)

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

    print("itr = {0}".format(k))
    print("current vec x:")
    print(vec_x)
    print("current vec r:")
    print(vec_r)

    flag = False
    for i in range(len(vec_x)):
      if abs(vec_x[i] - vec_r[i]) > 0.00001:
        flag = True

    if flag == False:
      break

  print("number of iterations:")
  print(k)

  print("result vec x:")
  print(vec_x)

if __name__ == "__main__":
  gauss_seidel()
