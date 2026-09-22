import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication
import re

# takes a number, turns it into a float
# checks if the number has non zero decimal place
# if it does then rounds to 2 decimal place 
# else round to nearest whole number
def roundingPlaces(number):
    number = float(number)
    if number == int(number):
        number = int(number)
    else:
        number = round(number, 2)

    return number


def ReturnDict(solved = False, answer_string = None):
    return {'solved': solved, 'answer_string': answer_string}


#parses through the expression looking for unkown variable
#if an unknown variable is found then declares it and returns 1
#if an unknown variable is not found then return 0
usedVariable = {}
def unknownVariableFind(expression):
    for i in range(len(expression)):
            if expression[i].isalpha() and expression[i] != 'x':
                usedVariable[expression[i]] = sp.symbols(expression[i])
                return expression[i]
    return 0

#This changes powers, roots, trig etc into notation understood by sympy
#^ into **
#underroots into sp.sqrt()
#pi into sp.pi
#trig func into sp.sin, sp.cos, sp.tan
#inverse trig func into sp.asin, sp.acos, sp.atan
#. and x into *
#e as sp.E
def inputCleaner(userInput):
    replacements = {
        'sin⁻¹(': 'sp.asin(',
        'cos⁻¹(': 'sp.acos(',
        'tan⁻¹(': 'sp.atan(',
        'sin(': 'sp.sin(',
        'cos(': 'sp.cos(',
        'tan(': 'sp.tan(',
        '∛(': 'sp.cbrt(',    
        '√': 'sp.sqrt(',  
        'π': 'sp.pi'
    }

    for userSymbol, symSymbol in replacements.items():
        userInput = userInput.replace(userSymbol, symSymbol)

    userInput = re.sub(r'\be\b', 'sp.E', userInput)

    return userInput 