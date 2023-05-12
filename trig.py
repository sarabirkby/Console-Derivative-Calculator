import math

from function import *


class Sin(Function):
    def __init__(self, variables, coefficient, inner_term):
        super().__init__(variables, coefficient, inner_term)

    def __str__(self):
        if self.coefficient:
            return f'{self.coefficient}sin({self.inner_term})'
        if self.coefficient == 0:
            return '0'
        return f'sin({self.inner_term})'

    def evaluate(self, input_vals: dict[str:float]) -> float:
        sin_val = math.sin(self.inner_term.evaluate(input_vals))
        return self.coefficient * sin_val


class Cos(Function):
    def __init__(self, variables, coefficient, inner_term):
        super().__init__(variables, coefficient, inner_term)

    def __str__(self):
        if self.coefficient:
            return f'{self.coefficient}cos({self.inner_term})'
        if self.coefficient == 0:
            return '0'
        return f'cos({self.inner_term})'

    def evaluate(self, input_vals: dict[str:float]) -> float:
        cos_val = math.cos(self.inner_term.evaluate(input_vals))
        return self.coefficient * cos_val


def sin_derivation_method(self: Sin) -> Cos | int:
    if self.coefficient == 0:
        return 0
    return Cos(self.variables, self.coefficient, self.inner_term)


def cos_derivation_method(self: Cos) -> Sin | int:
    if self.coefficient == 0:
        return 0
    return Sin(self.variables, -self.coefficient, self.inner_term)


Sin.derive = sin_derivation_method
Cos.derive = cos_derivation_method
