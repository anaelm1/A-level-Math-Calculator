'''
Quadratics is one of starting topics of A level Maths. This file is being coded by Anael.
The subtopics are: 
    1. Middle Term Breaking (Factoring)
    2. Completing the Square
    3. Quadratic Formula 
    4. Discriminant Analysis 
    5. Hidden / Disguised Quadratics
    6. Grapher of Quadratic curve (THIS WILL BE IMPLEMENTED IN THE GRAPHING CALC PART. IT IS NOT WORTH IT TO IMPLEMENT IT HERE)
The parameters are (method, a, b, c). 5 is exception where parameter is (eqn_str) method is an integer from 1 to 6 as the topics are numbered above. 
The eqn format should be outputted before taking user input. It is ax^2 + bx + c
The return dictionary contains:
{
'solved' : bool (true/false),
'error' : string
'roots': [{"type": string (real/complex), "value": float, "exact_value": string }, {"type": string, "value": float, "exact_value": string }],
'vertex': {x,y},
'discriminant': {"value": float, "nature": string},
"completed_square": {"a": integer, "h": integer, "k": integer, "form": string},
"factored_form": string
}

The roots are a list inside a dictionary value. To acess one, access the return dictionary's roots value, select a list index, access the value's value for the root.
Similar style is used for the completing square but no list. 

If either of the dict values are not required, they will be set to None. 
''' 

import math
import sympy as sp #for factoring
x = sp.Symbol('x')


def Quadratics(method, equation_str): #TODO: I need to make the input more user friendly as the current formating is ** for powers
    poly = sp.Poly(equation_str, x)
    a = float(poly.coeff_monomial(x**2))
    b = float(poly.coeff_monomial(x**1))
    c = float(poly.coeff_monomial(x**0))

    print(a, b, c)
    
    if method != 5 and a == 0: 
        output = {"solved": False, "error": "a cannot be 0 as that is a linear equation."}
    if method == 1:
        return MiddleTerm(a, b, c)
    elif method == 2:
        return CompletingSquare(a, b, c)
    elif method == 3:
        return QuadraticFormula(a, b, c)
    elif method == 4:
        return Discriminant(a, b, c)
    elif method == 5: 
        return DisguisedQuadratic(equation_str) 

def MiddleTerm(a, b, c):
    expression = a*x**2 + b*x + c
    factored = sp.factor(expression)

    if factored == expression: #sp returns same eqn if no factoring possible
        output = {"solved": False, "error": "No factoring possible. Quadratic formula option is available."}
        return output
    else:
        solutions = sp.solveset(expression, x)
        roots = []
        for solution in solutions:
            roots.append({"type": "real", "value": float(solution.evalf(3)), "exact_value": solution}) #evalf is a part of sp that converts fraction into decimal as the specified 3 digit number
        output = {"solved": True, "roots": roots, "factored_form": factored}
        return output

def CompletingSquare(a, b, c):
    h = -b / (2 * a)
    k = c - (b**2 / (4 * a))

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

    if a == 1:
        target_a = a
    elif a == -1:
        target_a = "-"
    else: 
        target_a = ""

    form = f"{target_a}(x {h_str})^2{k_str}"

    output = {'solved' : True, 'error' : None, "completed_square": {"a": a, "h": h, "k": k, "form": form}}

    return output

def QuadraticFormula(a, b, c):
    expression = a*x**2 + b*x + c
    solutions = sp.solveset(expression, x)
    roots = []
    for solution in solutions:
        if (b ** 2) - (4 * a * c) < 0:
            roots.append({"type": "complex", "value": None, "exact_value": solution}) #evalf is a part of sp that converts fraction into decimal as the specified 3 digit number
        else:
            roots.append({"type": "real", "value": float(solution.evalf(3)), "exact_value": solution})
    output = {"solved": True, "roots": roots}
    return output

def Discriminant(a, b, c):
    D = (b ** 2) - (4 * a * c)
    data_roots = QuadraticFormula(a, b, c)
    roots = data_roots["roots"]
    if D > 0: 
        output = {"solved": True, "roots": roots, "discriminant": {"value": D, "nature": "Real"}}
        return output
    if D == 0: 
        output = {"solved": True, "roots": roots, "discriminant": {"value": D, "nature": "Real and Equal"}}
        return output
    if D < 0: 
        output = {"solved": True, "roots": roots, "discriminant": {"value": D, "nature": "Imaginary"}}
        return output

def DisguisedQuadratic(equation_str):
  try:
    equation = sp.sympify(equation_str)
    solutions = sp.solve(equation, x)

    roots = []
    for solution in solutions:
        roots.append({"type": "real", "value": float(solution.evalf(3)), "exact_value": solution}) #evalf is a part of sp that converts fraction into decimal as the specified 3 digit number
    output = {"solved": True, "roots": roots}
    return output
  except:
    output = {"solved": False, "error": "Equation can't be solved."}
