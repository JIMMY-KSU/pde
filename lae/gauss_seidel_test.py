import unittest
import gauss_seidel

class GaussSeidelTestCase(unittest.TestCase):
  def setUp(self):
    pass

  def test_solve(self):
    a = [[2.0,  1.0,  1.0], 
         [2.0,  3.0,  1.0],
         [1.0,  1.0,  3.0]]
    rhs = [2.0, 4.0, -1.0]
    obj = gauss_seidel.GaussSeidel(a, rhs)
    ret = obj.solve()
    #ret = gauss_seidel.gauss_seidel()
    self.assertAlmostEqual(ret[0], 1.000000,5)
    self.assertAlmostEqual(ret[1], 0.999998,5)
    self.assertAlmostEqual(ret[2],-1.000000,5)

if __name__ == "__main__":
  unittest.main()
