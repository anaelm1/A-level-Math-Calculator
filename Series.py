'''
CODED BY RAPHEAL


Series is one of the early topics and comprisies of the following
    1. Binomial Expansion
        1. Expansion
        2. Coffecent of X term
        3. Expansion Multiplied by another bracket
        4. 1 Unknown variable 
        5. 1 unknown variable with 2 brackets



Frequently used functions
.sympify - converts into sympy datatype
.expand - expands the expression
.Add.make_args - extracts the different terms
'''

import sympy as sp
import math
from helperFunctions import *
x = sp.symbols('x')




'''
main function for series
all of its parameters have a default value of None to avoid any crash
it is incased in try and if to ensure there are no crashed at any given point
'''

def Series(methord=None, quesExpression=None, quesPower=None, optRange=None):
    if methord and quesExpression:
        try:
            match methord:
                case 1:
                    return coeffecientX(quesExpression, quesPower)
                case 2:
                    return completeExpansion(quesExpression, quesPower)
                case 3:
                    return unkownExpansion(quesExpression, quesPower, optRange)
                case 4:
                    return unknownExpansion2Brackets(quesExpression, quesPower, optRange)
                case _:
                    return (ReturnDict(False))
        except:
            return (ReturnDict(False))
    else:
        return (ReturnDict(False))




'''
FINDS THE COEFFECIENT OF X TO THE NTH POWER
Parameter Definations:
expression = the expression given in the question
MaxPower = it is the power of X the question wants

takes expression and power
used .expand() to expand all the powers
used .poly() to convert it into an polynomail
used .coeff_monomial() to find the co-effecient of the Nth term power
returns a string value of the effecint
NOTE: Does not return the variable part
'''
def coeffecientX(expression, power): 
    try:
        power = int(power)
        expression = sp.sympify(expression)
        expansion = sp.poly(sp.expand(expression), x)
        coeffecient = expansion.coeff_monomial(x**power)
        return (ReturnDict(solved=True, answer_string=str(coeffecient)))
    except:
        return (ReturnDict(False))
        

'''
FINDS THE EXPANSTION OF AN EXPRESSION
Parameter Definations:
expression = the expression given in the question
MaxPower = it is the maximum power of X the question wants

takes expression and power
used .expand() to expand all the powers
used .poly() to convert it into an polynomail
used .coeff_monomial() to find the co-effecient of X powers in ascending order
the co-effecient in concatinated into the variable result along with the X power part
returns a string statement of the whole expression
NOTE: Treats i=0 or X**0 as an exception to not print x**0
'''
def completeExpansion(expression, maxPower):
    try:
        maxPower = int(maxPower)
        expression = sp.sympify(expression)
        expansion = sp.poly(sp.expand(expression))
        result=""
        for i in range(maxPower +1):
            if i == 0:
                result += str(expansion.coeff_monomial(x**i))
            else:
                result = result + " + " + (str(expansion.coeff_monomial(x**i))+ "*"+ str(x**i))
        return (ReturnDict(solved=True, answer_string=result))
    except:
        return (ReturnDict(False))
        


'''
FIND THE VALUE OF AN UNKOWN VARIABLE BY COMPARISON OF X CO-EFFECINTS
Parameter Definations:
expression = the expression given in the question
xterm = it is the x term whose coeffecient is given in the question
rangeQues = it is the range = Optional

uses .sympify to covert the expression and the term into sympy expression
uses .as_coeff_exponent(x) to seperate the base and exponent
extracts the 2 terms from the expression
.as_coeff_exponent(x) used again on both the terms to seperate base and exponent
r is the basic variable for term expansion
uses basic algerba to get a simflified equation for the value of r
.solve solves the eqation with respect to r and stores in y
y is a list therefore y[0] is used to get a value of type int
.binomial is used to calculate the combination for the term
.Eq is used to turn the whole thing into an equation comparing the given coeffecient with the calculated one
.solve return a list with possible values of the eqn
NOTE: Will give error if more then 1 unkown
'''




def unkownExpansion(expression, xTerm, rangeQues=None):
    try:
        varName = unknownVariableFind(expression)
        if varName != 0:
            
            termCoeff, termPower = sp.sympify(xTerm).as_coeff_exponent(x)
            expr, maxPower = sp.sympify(expression).as_base_exp()
            terms = sp.Add.make_args(expr)
            term1, var1 = terms[0].as_coeff_exponent(x)
            term2, var2 = terms[1].as_coeff_exponent(x)
            r = sp.symbols('r')
            y = var1*(maxPower-r) + var2*(r) - termPower
            y = (sp.solve(y,r))
            y = y[0]
            fac = sp.binomial(maxPower, y)
            aFind = sp.Eq(fac * term1**(maxPower-y) * term2**(y), termCoeff)
            aFind = sp.solve(aFind, varName)
            answer = rangeCheck(aFind, rangeQues)
            return (ReturnDict(solved=True, answer_string=answer))
        else:
            return (ReturnDict(False))
    except:
        return (ReturnDict(False))
        

# expression1 = "(2*x**0.5 + p*x**2)**6"
# print(unkownExpansion(expression1, "4860*x**9", "a<0"))


'''
FIND THE VALUE OF AN UNKOWN VARIABLE IN 2 BRACKETS BY COMPARISON OF X CO-EFFECINTS
Parameter Definations:
expression = the expression given in the question
xterm = it is the x term whose coeffecient is given in the question
rangeQues = it is the range = Optional

splits the main equation in the middle
check both the equation to find which one has the unknown variable, using unknownVariableFind
expands both equations after converting
extracts the terms
.as_coeff_exponent() to get the power of the x term given
uses nested loops to compare everyterm of both the original brackets to find the terms that give that power
adds a + sign where there is no sign
concatinates the new term formed
uses .Eq to form the quadratic eqn
uses .solve to solve the eqn
uses rangeCheck function to ensure correct answers
return a STRING with the right answers
'''

def unknownExpansion2Brackets(expression, xTerm, rangeQues=None):
    try:
        varName = unknownVariableFind(expression)
        expressions = expression.split(" * ")
        if unknownVariableFind(expressions[0]):
            unknownVariableFind(expressions[0])
        else:
            unknownVariableFind(expressions[1])
        exp1 = sp.expand(sp.sympify(expressions[0]))
        exp2 = sp.expand(sp.sympify(expressions[1]))
        terms1 = sp.Add.make_args(exp1)
        terms2 = sp.Add.make_args(exp2)
        termCoeff, termPower = sp.sympify(xTerm).as_coeff_exponent(x)
        newEqn = ""
        for i in terms1:
            for j in terms2:
                power1 = sp.sympify(i).as_coeff_exponent(x)[1]
                power2 = sp.sympify(j).as_coeff_exponent(x)[1]
                if power1 + power2 == termPower:
                    newTerm = str(i*j)
                    termIndex = newTerm.find("*x**"+str(termPower))
                    newTerm = newTerm[0:termIndex]
                    if newTerm[0] != "-":
                        newTerm = "+"+ newTerm
                    newEqn += newTerm
        newEqn = sp.Eq(sp.sympify(newEqn), termCoeff)
        aFind = sp.solve(newEqn, varName)
        answer = rangeCheck(aFind, rangeQues)
        return (ReturnDict(solved=True, answer_string=answer))
    except:
        return (ReturnDict(False))
        






#-----------------HELPER FUNCTIONS-----------------





# if a range value is provided then it is converted into a condition
# incase the user used a different variable for the unknown range, the program parses through it and make correct range
# then it goes through the list of answers and checks if they are real values, only if they are it checks the condition
# incase of no condition the functiom returns all answers
def rangeCheck(answerSet, givenRange="None"):
    answer=[]
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
                        answer.append(str(roundingPlaces(j)))
            else:
                answer.append(str(roundingPlaces(j)))
    return answer



exp = "(1+2*x)**5 * (1-a*x)**6"

print(unknownExpansion2Brackets(exp, "-5*x**2", "a<2"))
expression = "(1 + a*x)**6"
#print(Series(3, expression, 135*x**2))

