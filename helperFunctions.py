import sympy as sp


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