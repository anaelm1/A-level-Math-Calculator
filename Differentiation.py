'''
Differentiation is part of calculus and has the following types of questions
    1. unknown variable with stationary point
'''



import sympy as sp
import math
x = sp.symbols('x')

#def unknownVariableStationaryPoint(expression, xCoorTP):



'''
CALCULATES THE EQUATION OF NORMAL OR TANGENT
Parameter Definations
expression = equation of the curve
lineType = Normal or Tangent
xCord = x coordinate of the line

converts expression into sympy
calls gradientFind to calculate gradient
.subs to subsitute x coordinate into curve equation to find the y coordinate
calls yIntCalc to find c and returns the final equation
returns a string
'''
def eqnOfLineXcord(expression, lineType, xCord): #lineType 0 = Tangent, 1 = Normal
    expression = sp.simplify(expression)
    gradient = gradientFind(expression, lineType, xCord)
    yCord = expression.subs(x, xCord)
    return yIntCalc(xCord, yCord, gradient)


'''
CALCULATES THE EQUATION OF NORMAL OR TANGENT USING THE Y COORDINATE
Parameter Definations
expression = equation of the curve
lineType = Normal or Tangent
yCord = y coordinate of the line
givenRange = the range for x coordinate incase there are more then 1 answer

converts expression into sympy
.Eq and .solve to form and solve the equation to find x values
if a range is given then it call rangeCheck to check for the range
else just uses the 1st x value incase there are 2
calls gradientFind to calculate gradient
.subs to subsitute x coordinate into curve equation to find the y coordinate
calls yIntCalc to find c and returns the final equation
returns a string
'''
def eqnOfLineYcord(expression, lineType, yCord, givenRange="None"):
    expression = sp.simplify(expression)
    xCordEq = sp.Eq(yCord, expression)
    xCord = sp.solve(xCordEq, x)
    if givenRange:
        finalXcord = rangeCheck(xCord, givenRange)
    else:
        finalXcord = xCord[0]
    gradient = gradientFind(expression, lineType, finalXcord)
    return yIntCalc(finalXcord, yCord, gradient)

def eqnOfLineStationaryPoint






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
    yInt[0] = round(float(yInt[0]),2)
    gradient = round(float(gradient),2)
    if yInt[0].is_integer():
        yInt[0] = int(yInt[0])
    if gradient.is_integer():
        gradient = int(gradient)
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
                        answer = float(j)
    return answer



exp = "x**3 - 4*x**2 + 5*x + 1"
print(eqnOfLineYcord(exp, 0, 3, "x<3"))