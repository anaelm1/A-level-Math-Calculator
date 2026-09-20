'''
CODED BY RAPHEAL


Integration is another essential topic of P1 and has the following topics
    1. Basic Integration
'''


import sympy as sp
import math
from helperFunctions import *

x = sp.symbols('x')


def basicIntegration(expression, Coordinates):
    try:
        c = sp.symbols('c')
        equations = []
        expression = sp.sympify(expression)
        integral = sp.integrate(expression)
        wholeEq = integral + c
        finalEq = sp.Eq(wholeEq, Coordinates[1])
        intConstantEq = finalEq.subs(x, Coordinates[0])
        intConstant = sp.solve(intConstantEq)
        for value in intConstant:
            if value.is_real:
                value = roundingPlaces(value)
                if value > 0:
                    equation = str(integral) + " + " + str(value)
                    equations.append(equation)
                else:
                    equation = str(integral) + str(value)
                    equations.append(equation)
        return (ReturnDict(True, equations))
    except:
        return (ReturnDict(False))



exp = "6*x**2 - 4*x + 3"
basicIntegration(exp, (2,11))
