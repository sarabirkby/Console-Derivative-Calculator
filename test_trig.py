import unittest

from trig import *
class TestTrig(unittest.TestCase):
    def setUp(self) -> None:
        self.poly = Polynomial({'x', 'y'}, 4, {'x': 2, 'y': 3})
        self.sin_val = Sin({'x', 'y'}, 3, self.poly)
        self.sin_val2 = Sin({'x'}, 0, self.poly)
        self.eval_set = {'x': 3, 'y': 2}

    def test_sin_str(self):
        self.assertEqual(self.sin_val.__str__(), '3sin(4x^2y^3)')
        self.assertEqual(self.sin_val2.__str__(), '0')

    def test_sin_evaluate(self):
        self.assertAlmostEqual(self.sin_val.evaluate(self.eval_set), -2.5665, delta=0.001)
        self.assertEqual(self.sin_val2.evaluate(self.eval_set), 0)

    def test_sin_derive(self):
        cos_term = self.sin_val.derive()
        self.assertEqual(cos_term.__str__(), '3cos(4x^2y^3)')
        cos_term = self.sin_val2.derive()
        self.assertEqual(cos_term.__str__(), '0')