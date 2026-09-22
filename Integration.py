'''
CODED BY RAPHEAL/ANAEL


Integration is another essential topic of P1 and has the following topics
    1. Integration of equation
    2. Integration of equation (with limits)
'''


import sympy as sp
import math
from helperFunctions import *

x = sp.symbols('x')

#argument1 is either a list of xy or list of lowerlimit and upperlimit
def integration(method, expression, argument1):
    if method and argument1 and expression:
        try:
            match method:
                case 1:
                    return eqnIntegration(expression, argument1)
                case 2:
                    return eqnIntegrationRoots(expression, argument1)
        except:
            return (ReturnDict(False))

def eqnIntegration(expression, Coordinates):
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

def eqnIntegrationRoots(expression, limits):
    try:
        expression = sp.sympify(expression)
        integral = sp.integrate(expression, (x, limits[0], limits[1]))
        return (ReturnDict(True, integral))
    except:
        return (ReturnDict(False))

'''
(x, 0, 3)
exp = "x**2"                                      
print(eqnIntegrationRoots(exp, (0,3)))'''

