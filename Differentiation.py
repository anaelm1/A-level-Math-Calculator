'''
CODED BY RAPHEAL


Differentiation is part of calculus and has the following types of questions
    1. Normal Derivative
    2. Equation of normal/Tangent with x coordinate 
    3. Equation of normal/Tangent with y coordinate
    4. Coordinates of stationary point
    5. Double Derivative
    6. Unknown variable with x Coordinate
    7. Nature of Stationary Point


Frequently used functions
- .sympify - converts into sympy datatype
- .subs - subsitutes into a variable
- .Eq - form an equation with RHS and LHS
- .solve - solve an equation
- .diff - derivates an equation
'''

import sympy as sp
import math
from helperFunctions import *
x = sp.symbols('x')


'''
this is the master function used to call all the functions related to differentiation
all of its parameters have a default value of None to avoid any crash
it is incased in try and if to ensure there are no crashed at any given point
'''


def differentiation(method=None, expression=None, argument1=None, argument2=None, argument3=None):
    if method and expression:
        try:
            match method:
                case 1: 
                    return eqnOfLineXcord(expression, argument1, argument2)
                    #eqnOfLineXcord(expression, lineType, xCord)
                case 2:
                    return eqnOfLineYcord(expression, argument1, argument2, argument3)
                    #eqnOfLineYcord(expression, lineType, yCord, givenRange=None)
                case 3:
                    return coordinatesStationaryPoint(expression, argument1)
                    #coordinatesStationaryPoint(expression, givenRange=None)
                case 4:
                    return unknownVariableWithXCord(expression, argument1, argument2, argument3)
                    #unknownVariableWithXCord(expression, gradient, xCord, givenRange=None)
                case 5:
                    return natureOfStationaryPoint(expression, argument1, argument2)
                    #natureOfStationaryPoint(expression, xCords == is a list, derivative=None)
                case 6:
                    return findDerivative(expression)
                case 7:
                    return findDoubleDerivative(expression)
                case _:
                    return (ReturnDict(False))
        except:
            return (ReturnDict(False))
    else:
        return (ReturnDict(False))







'''
CALCULATES THE EQUATION OF NORMAL OR TANGENT
Parameter Definations
expression = equation of the curve
lineType = Normal or Tangent
xCord = x coordinate of the line

converts expression into sympy
calls gradientFind to calculate gradient
subsitutes x coordinate into curve equation to find the y coordinate
calls yIntCalc to find c and returns the final equation
appends the answer string into a list
calls ReturnDict to append the list with answers in a final dictionary, changes solved to ture
in case of an error at any point calls ReturnDict to store error
returns a dictionary
'''
def eqnOfLineXcord(expression, lineType, xCord): #lineType 0 = Tangent, 1 = Normal
    try:
        lineEqn=[]
        expression = sp.simplify(expression)
        gradient = gradientFind(expression, lineType, xCord)
        yCord = expression.subs(x, xCord)
        lineEqn.append(yIntCalc(xCord, yCord, gradient))
        return (ReturnDict(solved=True, answer_string=lineEqn))
    except:
        return (ReturnDict(False))

'''
CALCULATES THE EQUATION OF NORMAL OR TANGENT USING THE Y COORDINATE
Parameter Definations
expression = equation of the curve
lineType = Normal or Tangent
yCord = y coordinate of the line
givenRange = the range for x coordinate incase there are more then 1 answer

converts expression into sympy
forms and solve the equation to find x values
if a range is given then it call rangeCheck to check for the range
else iterates throught the values of x, and forms the equation for real values
calls gradientFind to calculate gradient
subsitute x coordinate into curve equation to find the y coordinate
calls yIntCalc to find c and returns the final equation
appends the answer string into a list
calls ReturnDict to append the list with answers in a final dictionary, changes solved to ture
in case of an error at any point calls ReturnDict to store error
returns a dictionary
'''
def eqnOfLineYcord(expression, lineType, yCord, givenRange=None):
    try:
        expression = sp.simplify(expression)
        xCordEq = sp.Eq(yCord, expression)
        xCords = sp.solve(xCordEq, x)
        equations = []
        if givenRange:
            xCord = rangeCheck(xCords, givenRange)
            gradient = gradientFind(expression, lineType, xCord)
            lineEqn =  yIntCalc(xCord, yCord, gradient)
            equations.append(lineEqn)
        else:
            for xCord in xCords:
                if xCord.is_real:   
                    gradient = gradientFind(expression, lineType, xCord)
                    lineEqn =  yIntCalc(xCord, yCord, gradient)
                    equations.append(lineEqn)
        return (ReturnDict(solved=True, answer_string=equations))
    except:
        return (ReturnDict(False))
    

'''
FINDS THE COORDINATES OF THE STATIONARY POINT OF A CURVE
Parameter Definations
expression = equation of the curve
givenRange = the range for x coordinate incase there are more then 1 answer

converts expression into sympy
derivate the equation
forms and solve the equation to find x values when derivative is compared with 0
if a range is given then it call rangeCheck to check for the range
else gives the coordinates for both the values of x
subsitute x coordinate into curve equation to find the y coordinate
calls roundingPlaces to check for floats and ensure 2 decimal places or 0 if an integer
appends the answer string into a list
calls ReturnDict to append the list with answers in a final dictionary, changes solved to ture
in case of an error at any point calls ReturnDict to store error
returns a dictionary
'''


def coordinatesStationaryPoint(expression, givenRange=None):
    try:
        expression = sp.sympify(expression)
        derivative = sp.diff(expression)
        gradientEq = sp.Eq(derivative, 0)
        xCords = sp.solve(gradientEq)
        coordinates = []
        if givenRange:
            xCord = rangeCheck(xCords, givenRange)
            yCord = expression.subs(x, xCord)
            coordinates.append(f"({(xCord)},{roundingPlaces(yCord)})")
        else:
            for xCord in xCords:
                yCord = expression.subs(x, xCord)
                coordinates.append(f"({(xCord)},{roundingPlaces(yCord)})")
        return (ReturnDict(solved=True, answer_string=coordinates))
    except:
        return (ReturnDict(False))



'''
FIND THE VALUE OF AN UNKNOWN VARIABLE WITH A X COORDINATE
Parameter Definations
expression = equation of the curve
gradient = gradient at that point on X
xCord = X coordinate of the point
givenRange = the range for x coordinate incase there are more then 1 answer

calls unknownVariableFind to find the unknown
converts expression into sympy
derivate the equation
forms, subsitute x and solve the equation to find unknown when derivative is compared with gradint
if a range is given then it call rangeCheck to check for the range
else gives the coordinates for both the values of x
.subs to subsitute x coordinate into curve equation to find the y coordinate
calls roundingPlaces to check for floats and ensure 2 decimal places or 0 if an integer
appends the answer string into a list
calls ReturnDict to append the list with answers in a final dictionary, changes solved to ture
in case of an error at any point calls ReturnDict to store error
returns a dictionary
'''

def unknownVariableWithXCord(expression, gradient, xCord, givenRange=None):
    try:
        varName = unknownVariableFind(expression)
        expression = sp.sympify(expression)
        derivative = sp.diff(expression, x)
        gradientEq = sp.Eq(derivative, gradient)
        unknownEq = gradientEq.subs(x, xCord)
        unknownValues = sp.solve(unknownEq)
        Values = []
        if givenRange:
            unKnownValue = rangeCheck(unknownValues, givenRange)
            Values.append(unKnownValue)
        else:
            for value in unknownValues:
                if value.is_real:
                    Values.append(value)
        return (ReturnDict(solved=True, answer_string=Values))
    except:
        return (ReturnDict(False))


'''
FIND THE NATURE OF A STATIONARY POINT AT X COORDINATE
Parameter Definations
expression = equation of the curve
gradient = gradient at that point on X
derivative = derivative of the eqn (optional)

converts expression into sympy
checks if derivative is given else derivates the equation
forms, subsitute x and solve the equation to find unknown when derivative is compared with gradint
if a range is given then it call rangeCheck to check for the range
else gives the coordinates for both the values of x
subsitute x coordinate into curve equation to find the y coordinate
calls roundingPlaces to check for floats and ensure 2 decimal places or 0 if an integer
appends the answer string into a list
calls ReturnDict to append the list with answers in a final dictionary, changes solved to ture
in case of an error at any point calls ReturnDict to store error
returns a dictionary
'''

def natureOfStationaryPoint(expression, xCords, derivative=None):
    try:
        natures = []
        expression = sp.sympify(expression)
        if not derivative:
            derivative = sp.diff(expression)
        else:
            derivative = sp.sympify(derivative)
        doubleDerivative = sp.diff(derivative)
        for xCord in xCords:
            xCord = roundingPlaces(xCord)
            nature = doubleDerivative.subs(x , xCord)
            if nature < 0:
                natures.append({xCord:"maximum point"})
            elif nature > 0:
                natures.append({xCord:"minimum point"})
            
        return (ReturnDict(solved=True, answer_string=natures))
    except:
        return (ReturnDict(False))


def findDerivative(expression):
    try:
        expression = sp.sympify(expression)
        derivative = sp.diff(expression)
        return (ReturnDict(solved=True, answer_string=derivative))
    except:
        return (ReturnDict(False))

def findDoubleDerivative(expression):
    try:
        expression = sp.sympify(expression)
        derivative = sp.diff(expression)
        doubleDerivative = sp.diff(derivative)
        return (ReturnDict(solved=True, answer_string=doubleDerivative))
    except:
        return (ReturnDict(False))

    

         
    


#-----------------HELPER FUNCTIONS-----------------


# .derivative to calculate the 1st derivative of the equation
# .subs to subsitute x coordinate into the derivative equation
# check is lineType is 1, if it is takes negative reciprocal of the gradient
def gradientFind(expression, lineType, xCord):
    derivative = sp.diff(expression, x)
    gradient = derivative.subs(x, xCord)
    if lineType:
        gradient = -1/gradient
    return gradient

# .eq to form an equation with y coordinate on one side and standard line equation mx + c on other
# .solve to find the value of c
# turns yInt[0] and gradient into float anf then rounds both to 2 decimal places
# check if either of them doesnt have a decimal value, if it dosn`t then turns into an interger
# check if y intercept is positive, if it is adds a + sign in the final output
# returns the equation of line
def yIntCalc(xCord, yCord, gradient):
    global c
    c = sp.symbols('c')
    yIntEqn = sp.Eq(yCord, gradient*xCord + c)
    yInt = sp.solve(yIntEqn, c)
    yInt[0] = roundingPlaces(yInt[0])
    gradient = roundingPlaces(gradient)
    if yInt[0]:
        answer = f"y={gradient}x+{yInt[0]}"
    else:
        answer = f"y={gradient}x{yInt[0]}"
    return answer

# if a range value is provided then it is converted into a condition
# incase the user used a different variable for the unknown range, the program parses through it and make correct range
# then it goes through the list of answers and checks if they are real values, only if they are it checks the condition
def rangeCheck(answerSet, givenRange="None"):
    if givenRange:
        operators = ["<", ">", ">=", "<="]
        found = False
        condition = "j"
        for i in range(len(givenRange)):
            if (givenRange[i] in operators) or found:
                found = True
                condition += givenRange[i]
    for j in answerSet:
        if j.is_real:
            if givenRange:
                if eval(condition):
                        answer = roundingPlaces(j)
    return answer


## Checked Functions
# print(eqnOfLineXcord(exp,0,4))
# print(eqnOfLineYcord(exp, 0,3, "x>0"))
# print(coordinatesStationaryPoint(exp))
# print(unknownVariableWithXCord("k**2 * x**3 - 5*k*x**2 + 8*x - 3", 1,1))
# print(natureOfStationaryPoint(exp, [1, 5/3]))
# print(findDerivative(exp))
# print(findDoubleDerivative(exp))

#All Working as intended


exp = "x**3 - 4*x**2 + 5*x + 1"
exp2 = "k**2 * x**3 - 5*k*x**2 + 8*x - 3"
