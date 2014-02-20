import unittest
import gauss_jordan

class GaussJordanTestCase(unittest.TestCase):
  def setUp(self):
    pass

  def test_solve(self):
    a = [[1.0,  1.0, -2.0, 3.0], 
         [5.0,  2.0,  1.0, 1.0],
         [1.0, -4.0,  3.0, 8.0]]
    ret = gauss_jordan.gauss(a)
    self.assertAlmostEqual(ret[0],1.875,3)
    self.assertAlmostEqual(ret[1],-3.125,3)
    self.assertAlmostEqual(ret[2],-2.125,3)

if __name__ == "__main__":
  unittest.main()
