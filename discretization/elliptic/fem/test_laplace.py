import unittest
import laplace

class TestLaplace(unittest.TestCase):
  def setUp(self):
    self.obj = laplace.Laplace()

  def test_disc(self):
    ret = self.obj.disc()
    self.assertAlmostEqual(ret[0][0],0.8889,4)
    self.assertAlmostEqual(ret[0][1],-0.2222,4)
    self.assertAlmostEqual(ret[0][2],-0.2222,4)
    self.assertAlmostEqual(ret[0][3],-0.0000,4)
    self.assertAlmostEqual(ret[0][4],0.3704,4)
    self.assertAlmostEqual(ret[1][0],-0.2222,4)
    self.assertAlmostEqual(ret[1][1],0.8889,4)
    self.assertAlmostEqual(ret[1][2],0.0000,4)
    self.assertAlmostEqual(ret[1][3],-0.2222,4)
    self.assertAlmostEqual(ret[1][4],0.2222,4)
    self.assertAlmostEqual(ret[2][0],-0.2222,4)
    self.assertAlmostEqual(ret[2][1],0.0000,4)
    self.assertAlmostEqual(ret[2][2],0.8889,4)
    self.assertAlmostEqual(ret[2][3],-0.2222,4)
    self.assertAlmostEqual(ret[2][4],0.2716,4)
    self.assertAlmostEqual(ret[3][0],0.0000,4)
    self.assertAlmostEqual(ret[3][1],-0.2222,4)
    self.assertAlmostEqual(ret[3][2],-0.2222,4)
    self.assertAlmostEqual(ret[3][3],0.8889,4)
    self.assertAlmostEqual(ret[3][4],0.1975,4)

if __name__ == "__main__":
  unittest.main()
