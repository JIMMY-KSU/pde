class Element:
  def __init__(self):
    self.nodes = []

class Node:
  def __init__(self, x, y, u):
    self.x = x
    self.y = y
    self.u = u

def laplace():
  import numpy as np
  import sys

  nelems = 18
  nnodes = 16
  width = 1.0
  height = 1.0
  nelemx = np.sqrt(nnodes) - 1
  nelemy = np.sqrt(nnodes) - 1
  h = width / nelemx
  k = height / nelemy
  print("nelems = {0}, nnodes = {1}, width = {2}, height = {3}, h = {4}, k = {5}".format(nelems,nnodes,width,height,h,k))

  elements = []
  for ielem in range(nelems):
    elements.append(Element())
    if ielem % 2 == 0:
      x = h + h * ((ielem % nelemx) / 2.0)
      y = k + k * ((ielem / nelemy) / 2.0)
      elements[ielem].nodes.append(Node(x, y, 0.0))

      x = h * ((ielem % nelemx) / 2.0)
      y = k + k * ((ielem / nelemy) / 2.0)
      elements[ielem].nodes.append(Node(x, y, 0.0))
          
      x = h * ((ielem % nelemx) / 2.0)
      y = k * ((ielem / nelemy) / 2.0)
      elements[ielem].nodes.append(Node(x, y, 0.0))
    else:
      x = h + h * (((ielem - 1) % nelemx) / 2.0)
      y = k + k * (((ielem - 1) / nelemy) / 2.0)
      elements[ielem].nodes.append(Node(x, y, 0.0))

      x = h * (((ielem - 1) % nelemx) / 2.0)
      y = k * (((ielem - 1) / nelemy) / 2.0)
      elements[ielem].nodes.append(Node(x, y, 0.0))
      
      x = h + h * (((ielem - 1) % nelemx) / 2.0)
      y = k * (((ielem - 1) / nelemy) / 2.0)
      elements[ielem].nodes.append(Node(x, y, 0.0))

  for elem in elements:
    print("elem :")
    for node in elem.nodes:
      print("x = {0}, y = {1}, u = {2}".format(node.x,node.y,node.u))

  sys.exit()

  for i in range(m):
    for j in range(n):
      x[i][j] = 0.0 + h * j
      y[i][j] = 0.0 + k * i

  for i in range(m):
    for j in range(n):
      u[i][j] = 0.0

  for i in range(m):
    u[i][0] = 0.0
    u[i][n-1] = 0.0

  for j in range(n):
    u[0][j] = 0.0
    u[m-1][j] = 4.0 * h * j * (1.0 - h * j)

  print("x:")
  for i in range(m):
    for j in range(n):
      print x[i][j],
    print ""
  print ""

  print("y:")
  for i in range(m):
    for j in range(n):
      print y[i][j],
    print ""
  print ""

  print("initail u:")
  for i in range(m):
    for j in range(n):
      print u[i][j],
    print ""
  print ""

  sys.exit()

#  for i in range(m):
#    for j in range(n):
#
  #print("k = {0}".format(k))

  #print("result u:")
  #for j in range(n+1):
  #  for i in range(m+1):
  #    print u[j][i],
  #  print ""

if __name__ == "__main__":
  laplace()
