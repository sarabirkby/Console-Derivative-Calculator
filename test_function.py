import unittest

from function import *
class TestFunction(unittest.TestCase):
    def test_polynomial_evaluate(self):
        variables = {'x'}
        coefficient = 5
        powers = {'x': 1}
        input_values = {'x': 5}
        poly = Polynomial(variables, coefficient, powers)
        self.assertAlmostEqual(poly.evaluate(input_values), 25)

        variables = {'x'}
        coefficient = 10
        powers = {'x': 2}
        input_values = {'x': 2}
        poly = Polynomial(variables, coefficient, powers)
        self.assertAlmostEqual(poly.evaluate(input_values), 40)

        variables = {'x'}
        coefficient = 0
        powers = {'x': 1}
        input_values = {'x': 5}
        poly = Polynomial(variables, coefficient, powers)
        self.assertAlmostEqual(poly.evaluate(input_values), 0)

        variables = {'x', 'y'}
        coefficient = 6
        powers = {'x': 1}
        input_values = {'x': 5, 'y': 3}
        poly = Polynomial(variables, coefficient, powers)
        self.assertAlmostEqual(poly.evaluate(input_values), 30)


    def test_polynomial_str(self):
        variables = {'x'}
        coefficient = 5
        powers = {'x': 1}
        poly = Polynomial(variables, coefficient, powers)
        self.assertEqual(poly.__str__(), '5x')

        variables = {'x'}
        coefficient = 0
        powers = {'x': 1}
        poly = Polynomial(variables, coefficient, powers)
        self.assertEqual(poly.__str__(), '0')

        variables = {'x', 'y'}
        coefficient = 6
        powers = {'x': 1, 'y': 2}
        poly = Polynomial(variables, coefficient, powers)
        self.assertEqual(poly.__str__(), '6xy^2')

    def test_polynomial_derive(self):
        variables = {'x'}
        coefficient = 5
        powers = {'x': 2}
        poly = Polynomial(variables, coefficient, powers)
        derivative = poly.derive('x')
        self.assertEqual(derivative.__str__(), '10x')

        variables = {'x'}
        coefficient = 0
        powers = {'x': 2}
        poly = Polynomial(variables, coefficient, powers)
        derivative = poly.derive('x')
        self.assertEqual(derivative.__str__(), '0')

        variables = {'x', 'y'}
        coefficient = 3
        powers = {'x': 2, 'y': 1}
        poly = Polynomial(variables, coefficient, powers)
        derivative = poly.derive('x')
        derivative = derivative.derive('y')
        self.assertEqual(derivative.__str__(), '6x')

class TestCompositeFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.term_1, self.term_2 = Polynomial({'x'}, 3, 2), Polynomial({'x'}, 14, 1)
        self.assertEqual(self.term_1.__str__(), '3x^2')
        self.assertEqual(self.term_2.__str__(), '14x')
        self.composite_func = CompositFunction({'x'}, [self.term_1, self.term_2], ['+'])
    def test_composite_str(self):
        self.assertEqual(self.composite_func.__str__(), '3x^2 + 14x')

    def test_composite_evaluate(self):
        self.assertAlmostEqual(self.composite_func.evaluate({4}), 104, delta=0.001)