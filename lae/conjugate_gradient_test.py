import unittest
import conjugate_gradient

class ConjugateGradientTestCase(unittest.TestCase):
  def setUp(self):
    pass

  def test_solve(self):
    a = [[2.0,  1.0,  1.0], 
         [1.0,  3.0,  1.0],
         [1.0,  1.0,  3.0]]
    rhs = [2.0, 4.0, -1.0]
    #a = [[ 5.0, -2.0], 
    #     [-2.0,  2.0]]
    #rhs = [3.0, 0.0]
    obj = conjugate_gradient.ConjugateGradient()
    ret = obj.solve(a, rhs)
    self.assertAlmostEqual(ret[0],   5.0 /  6.0, 5)
    self.assertAlmostEqual(ret[1],  17.0 / 12.0, 5)
    self.assertAlmostEqual(ret[2], -13.0 / 12.0, 5)
    #self.assertAlmostEqual(ret[0], 1.0, 1)
    #self.assertAlmostEqual(ret[1], 1.0, 1)

if __name__ == "__main__":
  unittest.main()
