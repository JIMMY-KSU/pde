import numpy as np

#--------------------------------------------------
# Class
#--------------------------------------------------
class Element:
  def __init__(self, elemid):
    self.elemid = elemid
    self.nodes = []

  def geta(self, targetnodeid, nodeid):
    if targetnodeid == nodeid:
      b = self.getb(targetnodeid)
      c = self.getc(targetnodeid)
      return b**2 + c**2
    else:
      b1 = self.getb(targetnodeid)
      b2 = self.getb(nodeid)
      c1 = self.getc(targetnodeid)
      c2 = self.getc(nodeid)
      return b1 * b2 + c1 * c2

  def getb(self, targetnodeid):
    for inode in range(len(self.nodes)):
      if self.nodes[inode].nodeid == targetnodeid:
        y0 = self.nodes[(inode+1)%len(self.nodes)].y
        y1 = self.nodes[(inode+2)%len(self.nodes)].y
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
    self._x = x
    self._y = y
    self._u = u
    self.isboundary = isboundary

  def getx(self):
    return self._x

  def gety(self):
    return self._y

  def getu(self):
    return self._u

  x = property(getx)
  y = property(gety)
  u = property(getu)

class Mesher:
  def __init__(self, width, height, nnodes, nelems):
    self.width = width
    self.height = height
    self.nodes = []
    self.nnodes = nnodes
    self.nnodesx = int(np.sqrt(nnodes))
    self.nnodesy = int(np.sqrt(nnodes))
    self.h = self.width / (self.nnodesx - 1)
    self.k = self.height / (self.nnodesy - 1)
    self.elements = []
    self.nelems = nelems

  def init_a(self):
    return np.zeros((self.nnodes,self.nnodes))

  def init_c(self):
    return np.zeros((self.nnodes))

  def _construct_a(self, a):
    for node in self.nodes:
      if node.isboundary == False:
        for elemnode in self.nodes:
          a[node.nodeid,elemnode.nodeid] = 0.0
        for elem in self.elements:
          if elem.iscontain(node.nodeid):
            for elemnode in elem.nodes:
              a[node.nodeid,elemnode.nodeid] += elem.geta(node.nodeid,elemnode.nodeid)

  def _construct_rhs(self, a, c):
    for node in self.nodes:
      if node.isboundary == False:
        c[node.nodeid] = 0.0
        for node_ in self.nodes:
          c[node.nodeid] += a[node.nodeid,node_.nodeid] * node_.u 

  def _construct_e(self, a, c, e):
    for node in self.nodes:
      if node.isboundary == False:
        e.append([])
        for node_ in self.nodes:
          if node_.isboundary == False:
            e[len(e)-1].append(a[node.nodeid,node_.nodeid])
        e[len(e)-1].append(-c[node.nodeid])
 
  def create(self):
    # set nodes
    for inode in range(self.nnodes):
      x = self.h * (inode % self.nnodesx)
      y = self.k * int(inode / self.nnodesy) 
  
      # set boundary condition
      isboundary = False
      u = 0.0
      if y == 0.0:
        u = 1.0
        isboundary = True
      elif y == self.height:
        u = 4.0 * x * (1.0 - x)
        isboundary = True
      if x == 0.0:
        u = 1.0 - y
        isboundary = True
      elif x == self.width:
        isboundary = True
  
      self.nodes.append(Node(inode, x, y, u, isboundary))
  
    # set elements
    for ielem in range(self.nelems):
      elem = Element(ielem)
      if ielem % 2 == 0:
        one = (ielem/2)%(self.nnodesx-1)+int(ielem/2/(self.nnodesx-1))*self.nnodesx
        elem.nodes.append(self.nodes[one+self.nnodesx+1])
        elem.nodes.append(self.nodes[one+self.nnodesx])
        elem.nodes.append(self.nodes[one])
      else:
        one = ((ielem-1)/2)%(self.nnodesx-1)+int((ielem-1)/2/(self.nnodesx-1))*self.nnodesx
        elem.nodes.append(self.nodes[one+1+self.nnodesx])
        elem.nodes.append(self.nodes[one])
        elem.nodes.append(self.nodes[one+1])
      self.elements.append(elem)


