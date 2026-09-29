'''
Quadratics is one of starting topics of A level Maths. This file is being coded by Anael.
The subtopics are: 
    1. Middle Term Breaking (Factoring)
    2. Completing the Square
    3. Quadratic Formula 
    4. Discriminant Analysis 
    5. Hidden / Disguised Quadratics
    6. Grapher of Quadratic curve (THIS WILL BE IMPLEMENTED IN THE GRAPHING CALC PART. IT IS NOT WORTH IT TO IMPLEMENT IT HERE)
The parameters are (method, expression).
The return dictionary contains:
{
'solved' : bool (true/false),
'error' : string
'answer_string': string(can be a list or a dict as well)
}

''' 

import math
from sympy import *
from helperFunctions import *

x = Symbol('x')


def Quadratics(method=None, expression=None): #TODO: I need to make the input more user friendly as the current formating is ** for powers
    try:
        expression = sp.sympify(expression)
        poly = sp.Poly(expression, x)
        a = poly.coeff_monomial(x**2)
        b = poly.coeff_monomial(x**1)
        c = poly.coeff_monomial(x**0)
        match method:
            case 1:
                return MiddleTerm(a, b, c)
            case 2:
                return CompletingSquare(float(a), float(b), float(c))
            case 3:
                return QuadraticFormula(a, b, c)
            case 4:
                return Discriminant(float(a), float(b), float(c))
            case 5:
                return DisguisedQuadratic(expression)
            case _:
                return (ReturnDict(False))
    except:
        return (ReturnDict(False))



def MiddleTerm(a, b, c): #answerstring[0] = factored form, answerstring[1] = root1, answerstring[2] = root 2...
    try:
        expression = a*x**2 + b*x + c
        factored = sp.factor(expression)

        if factored == expression: #sp returns same eqn if no factoring possible
            return ReturnDict(solved = False)
        else:
            solutions = sp.solveset(expression, x)
            answer = []
            answer.append(factored)
            for solution in solutions:
                answer.append(f"x = {roundingPlaces(solution)}") 
            return ReturnDict(solved = True, answer_string = answer)
    except:
        return (ReturnDict(False))

def CompletingSquare(a, b, c): #answerstring[0] = factored form, answerstring[1] = a, answerstring[2] = h, answerstring[2] = k
    try:
        h = -b / (2 * a)
        h = roundingPlaces(h)

        k = c - (b**2 / (4 * a))
        k = roundingPlaces(k)

        if h >= 0:
            h_str = f"- {abs(h)}"
        elif h < 0:
            h_str = f"+ {abs(h)}"
        else:
            h_str = ""
        
        if k > 0:
            k_str = f" + {abs(k)}"
        elif k < 0:
            k_str = f" - {abs(k)}"
        else:
            k_str = ""

        if a == 1 or a == 1.0:
            target_a = ""
        elif a == -1 or a == -1.0:
            target_a = "-"
        else: 
            target_a = str(roundingPlaces(a))

        form = f"{target_a}(x {h_str})**2{k_str}"

        return ReturnDict(solved = True, answer_string = [form, a, h, k])
    except:
        return (ReturnDict(False))


    
def QuadraticFormula(a, b, c): #answerstring[0] = root1, answerstring[1] = root2...
    try:
        expression = a*x**2 + b*x + c
        solutions = sp.solveset(expression, x)
        answers = []
        for solution in solutions:
            if (b ** 2) - (4 * a * c) < 0:
                answers.append(f"x = {solution}")
            else:
                answers.append(f"x = {roundingPlaces(solution)}")
        return ReturnDict(solved = True, answer_string = answers)
    except:
        return (ReturnDict(False))


def Discriminant(a, b, c): #answerstring[0] = discriminant value, answerstring[1] = nature...
    try:
        D = (b ** 2) - (4 * a * c)
        if D > 0: 
            return ReturnDict(solved = True, answer_string = [f"discriminant = {roundingPlaces(D)}", "Nature = Real"])
        if D == 0: 
            return ReturnDict(solved = True, answer_string = [f"discriminant = {roundingPlaces(D)}", "Nature = Real but equal"])
        if D < 0: 
            return ReturnDict(solved = True, answer_string = [f"discriminant = {roundingPlaces(D)}", "Nature = Imaginary"])
    except:
        return (ReturnDict(False))



def DisguisedQuadratic(expression): #answerstring[0] = root1, answerstring[1] = root2...
  try:
    expression = sp.sympify(expression)
    solutions = sp.solve(expression, x)
    answers = []
    for solution in solutions:
        answers.append(f"x = {roundingPlaces(solution)}")
    return ReturnDict(solved = True, answer_string = answers)
  except:
    return (ReturnDict(False))



#Checked Functions