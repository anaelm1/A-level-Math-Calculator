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

def splitArgs(text):
    parts = []
    current = []
    depth = 0
    for char in text:
        if char == '(':
            depth += 1
            current.append(char)
        elif char == ')':
            depth = max(0, depth - 1)
            current.append(char)
        elif char == ',' and depth == 0:
            part = ''.join(current).strip()
            if part:
                parts.append(part)
            current = []
        else:
            current.append(char)
    part = ''.join(current).strip()
    if part:
        parts.append(part)
    return parts

def prepareExpression(text):
    if text is None:
        return ""
    cleaned = inputCleaner(str(text).strip())
    cleaned = cleaned.replace("^", "**")
    cleaned = cleaned.replace("sp.", "")
    return cleaned

def parseNumber(text):
    expression = prepare_expression(text)
    value = sp.N(sp.sympify(expression))
    return float(value)


def parseInt(text):
    return int(round(parse_number(text)))


def parseTerm(token):
    token = token.strip()
    if ":" in token:
        index, value = token.split(":", 1)
        return [parse_int(index), parse_number(value)]
    raise ValueError("Term must look like n:value, for example 3:10")


def parseTwoTerms(tokens):
    if len(tokens) == 2:
        return parse_term(tokens[0]), parse_term(tokens[1])
    if len(tokens) == 4:
        return (
            [parse_int(tokens[0]), parse_number(tokens[1])],
            [parse_int(tokens[2]), parse_number(tokens[3])],
        )
    raise ValueError("Enter two terms as n:value, n:value or n, value, n, value")


def parseLineType(text):
    value = str(text).strip().lower()
    if value in ("1", "normal", "n"):
        return 1
    return 0


def parseMode(text):
    value = str(text).strip().upper()
    if value in ("DEG", "DEGREE", "DEGREES", "D"):
        return "DEG"
    return "RAD"


def formatAnswer(result):
    if not result or not result.get("solved"):
        return "Could not solve. Check the input format shown above the display."
    answer = result.get("answer_string")
    if answer is None:
        return "Could not solve. Check the input format shown above the display."
    if isinstance(answer, list):
        pieces = []
        for item in answer:
            if isinstance(item, dict):
                pieces.extend(f"{key}: {value}" for key, value in item.items())
            else:
                pieces.append(str(item))
        return "  |  ".join(pieces)
    return str(answer)

