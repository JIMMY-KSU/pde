#--------------------------------------------------
# Class
#--------------------------------------------------
class Element:
  def __init__(self, elemid):
    self.elemid = elemid
    self.nodes = []

  def geta(self, targetnodeid, nodeid):
    #return 1.0
    if targetnodeid == nodeid:
      b = self.getb(targetnodeid)
      c = self.getc(targetnodeid)
      return b**2 + c**2
    else:
      b1 = self.getb(targetnodeid)
      b2 = self.getb(nodeid)
      c1 = self.getc(targetnodeid)
      c2 = self.getc(nodeid)
      #if targetnodeid == 5 and nodeid == 6:
      #  print("b1 = {0} b2 = {1} c1 = {2} c2 = {3}".format(b1,b2,c1,c2))
      return b1 * b2 + c1 * c2

  def getb(self, targetnodeid):
    for inode in range(len(self.nodes)):
      if self.nodes[inode].nodeid == targetnodeid:
        y0 = self.nodes[(inode+1)%len(self.nodes)].y
        y1 = self.nodes[(inode+2)%len(self.nodes)].y
        #print("{0} {1} {2}".format(self.nodes[inode].nodeid,self.nodes[(inode+1)%len(self.nodes)].nodeid,self.nodes[(inode+2)%len(self.nodes)].nodeid))
    return y0 - y1

  def getc(self, targetnodeid):
    for inode in range(len(self.nodes)):
      if self.nodes[inode].nodeid == targetnodeid:
        x0 = self.nodes[(inode+1)%len(self.nodes)].x
        x1 = self.nodes[(inode+2)%len(self.nodes)].x
    return x1 - x0

  def iscontain(self, nodeid):
    for node in self.nodes:
      if node.nodeid == nodeid:
        return True
    return False

class Node:
  def __init__(self, nodeid, x, y, u, isboundary):
    self.nodeid = nodeid
    self.x = x
    self.y = y
    self.u = u
    self.isboundary = isboundary

class Laplace:
  def __init__(self):
    pass

  def disc(self):
    import numpy as np
    import sys
  
    nelems = 18
    nnodes = 16
    nnodesx = int(np.sqrt(nnodes))
    nnodesy = int(np.sqrt(nnodes))
    width = 1.0
    height = 1.0
    h = width / (nnodesx - 1)
    k = height / (nnodesy - 1)
    #print("nelems = {0}, nnodes = {1}, width = {2}, height = {3}, h = {4}, k = {5}".format(nelems,nnodes,width,height,h,k))
  
    a = np.zeros((nnodes,nnodes))
    c = np.zeros((nnodes))
    e = []
  
    # set nodes
    nodes = []
    for inode in range(nnodes):
      x = h * (inode % nnodesx)
      y = k * int(inode / nnodesy) 
  
      # set boundary condition
      isboundary = False
      u = 0.0
      if y == 0.0:
        #u = 0.0
        u = 1.0
        isboundary = True
      elif y == height:
        u = 4.0 * x * (1.0 - x)
        isboundary = True
      if x == 0.0:
        u = 1.0 - y
        isboundary = True
      elif x == width:
        isboundary = True
  
      nodes.append(Node(inode, x, y, u, isboundary))
  
    #print("nodes :")
    #for node in nodes:
    #  print("x = {0}, y = {1}, u = {2} isboundary = {3}".format(node.x,node.y,node.u,node.isboundary))
  
    # set elements
    elements = []
    for ielem in range(nelems):
      elem = Element(ielem)
      if ielem % 2 == 0:
        one = (ielem/2)%(nnodesx-1)+int(ielem/2/(nnodesx-1))*nnodesx
        elem.nodes.append(nodes[one+nnodesx+1])
        elem.nodes.append(nodes[one+nnodesx])
        elem.nodes.append(nodes[one])
        #print("ielem = {0} : {1} {2} {3}".format(ielem,elem.nodes[0].nodeid,elem.nodes[1].nodeid,elem.nodes[2].nodeid))
      else:
        one = ((ielem-1)/2)%(nnodesx-1)+int((ielem-1)/2/(nnodesx-1))*nnodesx
        elem.nodes.append(nodes[one+1+nnodesx])
        elem.nodes.append(nodes[one])
        elem.nodes.append(nodes[one+1])
        #print("ielem = {0} : {1} {2} {3}".format(ielem,elem.nodes[0].nodeid,elem.nodes[1].nodeid,elem.nodes[2].nodeid))
      elements.append(elem)
  
    #print("elements :")
    #for elem in elements:
    #  print("elem :")
    #  for node in elem.nodes:
    #    print("x = {0}, y = {1}, u = {2}".format(node.x,node.y,node.u))
  
    # construct A
    for node in nodes:
      if node.isboundary == False:
        #print("target node id = {0}".format(node.nodeid))
        for elemnode in nodes:
          a[node.nodeid,elemnode.nodeid] = 0.0
        for elem in elements:
          if elem.iscontain(node.nodeid):
            #print("correspond elem id = {0}".format(elem.elemid))
            for elemnode in elem.nodes:
              #print(elemnode.nodeid)
              a[node.nodeid,elemnode.nodeid] += elem.geta(node.nodeid,elemnode.nodeid)
              #if node.nodeid == 5 and elemnode.nodeid == 6:
              #  print("u[{0}] elemid = {1} u[{2}]".format(node.nodeid,elem.elemid,elemnode.nodeid))
              #  #print("elem.geta = {0}".format(elem.geta(node.nodeid,elemnode.nodeid)))
  
    #print("a:")
    #for i in range(nnodes):
    #  for j in range(nnodes):
    #    print a[i,j],
    #  print ""
  
    # evaluate rhs vector
    for node in nodes:
      if node.isboundary == False:
        c[node.nodeid] = 0.0
        for node_ in nodes:
          c[node.nodeid] += a[node.nodeid,node_.nodeid] * node_.u 
  
  #  print("u:")
  #  for node in nodes:
  #    print node.u,
  #  print ""
  #
  #  print("c:")
  #  for i in range(nnodes):
  #    print c[i],
  #  print ""
  
    for node in nodes:
      if node.isboundary == False:
        e.append([])
        for node_ in nodes:
          if node_.isboundary == False:
            e[len(e)-1].append(a[node.nodeid,node_.nodeid])
        e[len(e)-1].append(-c[node.nodeid])
        
    #print("e:")
    #for row in e:
    #  for item in row:
    #    print item,
    #  print ""

    result_mat = np.array(e)

    return result_mat
