'''
Trigonometry: Coded by Anael
The subtopics are:
    1. Graphs (THIS WILL BE IMPLEMENTED IN THE GRAPHING CALC PART. IT IS NOT WORTH IT TO IMPLEMENT IT HERE)
    2. Equations (With range specified)
    3. Identities  
The parameters are (method, mode, expression). Double equals to (==) for identities, Equals to (=) for equations.
The return dictionary contains:
{
'solved' : bool (true/false),
'error' : string
'answer_string': string(can be a list or a dict as well)
}

The universal output of all equations is in radii. If we want degree, conversion will be done at the last step.
Pi is written like this sp.pi
'''

import math
import sympy as sp #for solving
from helperFunctions import *
from Plotter import Plotter 
x = sp.Symbol('x')


def Trigonometry(method=None, mode="RAD", expression=None, range_lower=None, range_upper=None):
    if method and mode and expression:
        try:
            match method:
                case 1:
                    return Equations(mode, expression, range_lower, range_upper)
                case 2:
                    return Plotter(mode, expression, range_lower, range_upper)
                case _:
                    return (ReturnDict(False))
        except:
            return (ReturnDict(False))
    else:
        return (ReturnDict(False))


def Equations(mode, expression, rangeower, range_uppper): #everything in Rad
    try:
        x = sp.Symbol("x")
        if mode == "DEG":
            range_upper = math.radians(range_upper)
            range_lower = math.radians(range_lower)

        parts = expression.split("=", 1)
        if len(parts) != 2:
            return ReturnDict(False)

        equation = sp.Eq(sp.sympify(parts[0]), sp.sympify(parts[1]))
        solutions = sp.solveset(equation, x, domain=sp.Interval(range_lower, range_upper))
        answers = []
        for solution in solutions:
            if mode == "DEG":
                degree_value = math.degrees(float(solution.evalf()))
                answers.append(f"x = {degree_value:.1f} OR x = {degree_value:.3f}")
            else:
                answers.append(f"x = {solution} OR x = {float(solution.evalf()):.3f}")

        if not answers:
            return ReturnDict(False)
        return ReturnDict(solved=True, answer_string=answers)
    except:        
        return (ReturnDict(False))
