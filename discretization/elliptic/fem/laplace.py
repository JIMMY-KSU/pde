from mesher import Mesher
import numpy as np

class Laplace:
  def __init__(self):
    nelems = 18
    nnodes = 16
    width = 1.0
    height = 1.0
    self.mesher = Mesher(width, height, nnodes, nelems)
    self.a = np.zeros((self.mesher.nnodes,self.mesher.nnodes))
    self.c = np.zeros((self.mesher.nnodes))
    self.e = []

  def disc(self):
  
    # create nodes and elements
    self.mesher.create()
 
    # construct A
    self._construct_a()

    # evaluate rhs vector
    self._construct_rhs()

    # construct extension matrix e
    self._construct_e()

    # return extension matrix as numpy matrix
    return np.array(self.e)

  def _construct_a(self):
    for node in self.mesher.nodes:
      if node.isboundary == False:
        for elemnode in self.mesher.nodes:
          self.a[node.nodeid,elemnode.nodeid] = 0.0
        for elem in self.mesher.elements:
          if elem.iscontain(node.nodeid):
            for elemnode in elem.nodes:
              self.a[node.nodeid,elemnode.nodeid] += elem.geta(node.nodeid,elemnode.nodeid)

  def _construct_rhs(self):
    for node in self.mesher.nodes:
      if node.isboundary == False:
        self.c[node.nodeid] = 0.0
        for node_ in self.mesher.nodes:
          self.c[node.nodeid] += self.a[node.nodeid,node_.nodeid] * node_.u 

  def _construct_e(self):
    for node in self.mesher.nodes:
      if node.isboundary == False:
        self.e.append([])
        for node_ in self.mesher.nodes:
          if node_.isboundary == False:
            self.e[len(self.e)-1].append(self.a[node.nodeid,node_.nodeid])
        self.e[len(self.e)-1].append(-self.c[node.nodeid])
        
