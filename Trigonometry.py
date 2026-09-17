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

x = sp.Symbol('x')

def ReturnDict(solved = True, error = None, answer_string = None):
    return {'solved': solved, 'error': error, 'answer_string': answer_string}

def Trigonometry(method, mode, equation_str, range_lower, range_upper):
    if method == 2:
        return Equations(mode, equation_str, range_lower, range_upper)


def Equations(mode, equation_str, range_lower, range_uppper): #everything in Rad
    if mode == 'deg':
        range_uppper = math.radians(range_uppper)
        range_lower = math.radians(range_lower)
    parts = equation_str.split("=", 1)
    LHS = parts[0]
    RHS = parts[1]

    LHS = sp.sympify(LHS)
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
        return ReturnDict(solved = False, error = 'Equation has imaginary solutions')
    
    return ReturnDict(solved = True, error = None, answer_string = answers)

def Identities(equation_str): #equation will be separated by the two equals to (==) 
    parts = equation_str.split("=", 1)
    LHS = parts[0]
    RHS = parts[1]

    equal_check = LHS.equals(RHS)
    if not equal_check:
       return ReturnDict(solved = False, error = 'LHS AND RHS are not equal') 
    #This requires AI concepts Breath first search algorithm 

