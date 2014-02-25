import unittest
import laplace_gauss_seidel
from gauss_jordan import GaussJordan
from gauss_seidel import GaussSeidel

class LaplaceTestCase(unittest.TestCase):
  #def setUp(self):
  #  nelems = 18
  #  nnodes = 16
  #  width = 1.0
  #  height = 1.0
  #  mesher = Mesher(width, height, nnodes, nelems)

  #  lae = GaussJordan()
  #  self.obj = laplace.Laplace(mesher, lae)

  #  lae2 = GaussSeidel()
  #  self.obj2 = laplace.Laplace(mesher, lae2)

  #def test_disc(self):
  #  ret = self.obj.disc()
  #  self.assertAlmostEqual(ret[0][0],0.8889,4)
  #  self.assertAlmostEqual(ret[0][1],-0.2222,4)
  #  self.assertAlmostEqual(ret[0][2],-0.2222,4)
  #  self.assertAlmostEqual(ret[0][3],-0.0000,4)
  #  self.assertAlmostEqual(ret[0][4],0.3704,4)
  #  self.assertAlmostEqual(ret[1][0],-0.2222,4)
  #  self.assertAlmostEqual(ret[1][1],0.8889,4)
  #  self.assertAlmostEqual(ret[1][2],0.0000,4)
  #  self.assertAlmostEqual(ret[1][3],-0.2222,4)
  #  self.assertAlmostEqual(ret[1][4],0.2222,4)
  #  self.assertAlmostEqual(ret[2][0],-0.2222,4)
  #  self.assertAlmostEqual(ret[2][1],0.0000,4)
  #  self.assertAlmostEqual(ret[2][2],0.8889,4)
  #  self.assertAlmostEqual(ret[2][3],-0.2222,4)
  #  self.assertAlmostEqual(ret[2][4],0.2716,4)
  #  self.assertAlmostEqual(ret[3][0],0.0000,4)
  #  self.assertAlmostEqual(ret[3][1],-0.2222,4)
  #  self.assertAlmostEqual(ret[3][2],-0.2222,4)
  #  self.assertAlmostEqual(ret[3][3],0.8889,4)
  #  self.assertAlmostEqual(ret[3][4],0.1975,4)

  #def test_solve_with_gauss_jordan(self):
  #  self.obj.disc()
  #  ret = self.obj.solve()

  #  self.assertAlmostEqual(ret[0],0.708333,6)
  #  self.assertAlmostEqual(ret[1],0.555556,6)
  #  self.assertAlmostEqual(ret[2],0.611111,6)
  #  self.assertAlmostEqual(ret[3],0.513889,6)

  def test_solve_with_gauss_seidel(self):
  #  self.obj2.disc()
  #  ret = self.obj2.solve()
    ret = laplace_gauss_seidel.laplace_gauss_seidel()

    self.assertAlmostEqual(ret[10][0],0.00,2)
    self.assertAlmostEqual(ret[10][1],0.36,2)
    self.assertAlmostEqual(ret[10][2],0.64,2)
    self.assertAlmostEqual(ret[10][3],0.84,2)
    self.assertAlmostEqual(ret[9][0],0.00,2)
    self.assertAlmostEqual(ret[9][1],0.25,2)
    self.assertAlmostEqual(ret[9][2],0.46,2)
    self.assertAlmostEqual(ret[9][3],0.61,2)
    self.assertAlmostEqual(ret[9][4],0.71,2)
    self.assertAlmostEqual(ret[9][5],0.74,2)
    self.assertAlmostEqual(ret[9][6],0.71,2)
    self.assertAlmostEqual(ret[9][7],0.61,2)
    self.assertAlmostEqual(ret[9][8],0.46,2)
    self.assertAlmostEqual(ret[9][9],0.25,2)
    self.assertAlmostEqual(ret[9][10],0.00,2)
    self.assertAlmostEqual(ret[1][0],0.00,2)
    self.assertAlmostEqual(ret[1][1],0.01,2)
    self.assertAlmostEqual(ret[1][2],0.02,2)
    self.assertAlmostEqual(ret[1][3],0.02,2)
    self.assertAlmostEqual(ret[1][4],0.03,2)
    self.assertAlmostEqual(ret[1][5],0.03,2)
    self.assertAlmostEqual(ret[1][6],0.03,2)
    self.assertAlmostEqual(ret[1][7],0.02,2)
    self.assertAlmostEqual(ret[1][8],0.02,2)
    self.assertAlmostEqual(ret[1][9],0.01,2)
    self.assertAlmostEqual(ret[1][10],0.00,2)

if __name__ == "__main__":
  unittest.main()
