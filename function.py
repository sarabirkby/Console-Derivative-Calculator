import math

import util

class Function:
    def __init__(self, variables, coefficient, inner_term=None):
        self.variables: set[str] = variables
        self.coefficient: float | None = coefficient
        self.inner_term: Function = inner_term
        if self.coefficient is None:
            self.coefficient = 1

class CompositFunction:
    def __init__(self, variables, terms, operators):
        self.variables: list[str] = variables
        self.terms: list[object] = terms
        self.operators: list[str] = operators
        if len(self.operators) != len(self.terms) - 1:
            raise RuntimeError('Improper operator count.')

    def __str__(self):
        output_string = ''
        for i,term in enumerate(self.terms):
            if i != 0:
                output_string += f'{self.operators[i-1]} '
            if i == len(self.terms)-1:
                output_string += f'{term}'
            else:
                output_string += f'{term} '
        return output_string




class Polynomial(Function):
    """
    This class represents any function in the form cx^n where c and n are real non-zero constants.
    """

    def __init__(self, variables, coefficient, powers):
        super().__init__(variables, coefficient)
        del self.inner_term
        self.powers: dict[str:float] = powers
        if isinstance(self.powers, int):
            if len(self.variables) != 1:
                raise RuntimeError('Must be a dictionary for more than 1 variable')
            variable = self.variables.pop()
            self.powers = {variable: self.powers}
            self.variables = set([variable])
        if len(self.powers) < len(self.variables):
            for var in self.variables:
                if not var in self.powers:
                    self.powers[var] = 0

    def __str__(self):
        if self.coefficient == 0:
            return '0'
        if not self.coefficient is None:
            output_str = str(self.coefficient)
        else:
            output_str = ''
            if len(self.powers) == 1 and self.powers[self.variables[0]] == 0:
                return '1'
        for var in sorted(self.variables):
            power = self.powers[var]
            if power == 1:
                output_str += var
            else:
                output_str += f'{var}^{power}'
        return output_str


    def evaluate(self, input_vals: dict[str:float]) -> float:
        value = self.coefficient
        for variable in self.variables:
            value *= (input_vals[variable] ** self.powers[variable])
        return value

    def derive(self, variable_of_derivation: str) -> Function | float:
        if self.coefficient == 0:
            return 0
        new_coefficient = self.coefficient * self.powers[variable_of_derivation]
        new_powers = {}
        for var, power in self.powers.items():
            if var == variable_of_derivation:
                new_powers[var] = self.powers[var] - 1
            else:
                new_powers[var] = self.powers[var]
        if new_powers[variable_of_derivation] == 0:
            new_vars = [variable for variable in self.variables if variable != variable_of_derivation]
            del new_powers[variable_of_derivation]
            if len(self.powers) == 1:
                return self.coefficient
            return Polynomial(new_vars, self.coefficient, new_powers)
        return Polynomial(self.variables, new_coefficient, new_powers)


class NaturalLog(Function):
    def __init__(self, variables, coefficient, inner_term):
        super().__init__(variables, coefficient, inner_term)

    def __str__(self):
        if self.coefficient:
            return f'{self.coefficient}ln({self.inner_term})'
        if self.coefficient == 0:
            return '0'
        return f'ln({self.inner_term})'

    def evaluate(self, input_vals: dict[str:float]) -> float:
        ln_val = math.log(self.inner_term.evaluate(input_vals))
        if self.coefficient is not None:
            return self.coefficient * ln_val
        return ln_val

    def derive(self, variable_of_derivation):
        if self.coefficient == 0:
            return 0
        new_powers = {var: -1 for var in self.variables}
        return Polynomial(self.variables, self.coefficient, new_powers)
