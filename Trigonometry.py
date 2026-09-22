'''
Trigonometry: Coded by Anael
The subtopics are:
    1. Graphs (THIS WILL BE IMPLEMENTED IN THE GRAPHING CALC PART. IT IS NOT WORTH IT TO IMPLEMENT IT HERE)
    2. Equations (With range specified)
    3. Identities  
The parameters are (method, mode, equation_str). Double equals to (==) for identities, Equals to (=) for equations.
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
x = sp.Symbol('x')


def Trigonometry(method=None, mode=None, equation_str=None, range_lower=None, range_upper=None):
    if method and mode and equation_str:
        try:
            match method:
                case 1:
                    return Equations(mode, equation_str, range_lower, range_upper)
                case _:
                    return (ReturnDict(False))
        except:
            return (ReturnDict(False))
    else:
        return (ReturnDict(False))


def Equations(mode, equation_str, range_lower, range_uppper): #everything in Rad
    #try:
        if mode == 'deg':
            range_uppper = math.radians(range_uppper)
            range_lower = math.radians(range_lower)
        parts = equation_str.split("=", 1)
        LHS = parts[0]
        RHS = parts[1]
        if LHS: 
            LHS = sp.sympify(LHS)
        if RHS:
            RHS = sp.sympify(RHS)

        equation = sp.Eq(LHS, RHS)

        solutions = sp.solveset(equation, x, domain= sp.Interval(range_lower, range_uppper))
        answers = []
        for solution in solutions:
            if mode == 'deg':
                solution = math.degrees(solution)
                answers.append(f"x = {solution:.1f} OR x = {solution:.3f}")
            else:
                answers.append(f"x = {solution} OR x = {float(solution.evalf()):.3f}")

        if answers == []:
            return (ReturnDict(False))
        
        return ReturnDict(solved = True, error = None, answer_string = answers)
    # except:
    #     return (ReturnDict(False))
