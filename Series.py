'''
Series is one of the early topics and comprisies of the following
    1. Binomial Expansion
        1. Expansion
        2. Coffecent of X term
        3. Expansion Multiplied by another bracket
        4. Unknown variable
    2. Arthematic Progression
    3. Geometric Progression
'''



import sympy as sp
import math

x = sp.symbols('x')
#def Binomial(methord, equation_str):

expression = (1 + 3*x)**6

'''
FINDS THE COEFFECIENT OF X TO THE NTH POWER
takes expression and power
used .expand() to expand all the powers
used .poly() to convert it into an polynomail
used .coeff_monomial() to find the co-effecient of the Nth term power
returns a string value of the effecint
NOTE: Does not return the variable part
'''
def coeffecientX(expression, power): 
    expansion = sp.poly(sp.expand(expression), x)
    coeffecient = expansion.coeff_monomial(x**power)
    return(str(coeffecient))

'''
FINDS THE EXPANSTION OF AN EXPRESSION
takes expression and power
used .expand() to expand all the powers
used .poly() to convert it into an polynomail
used .coeff_monomial() to find the co-effecient of X powers in ascending order
the co-effecient in concatinated into the variable result along with the X power part
returns a string statement of the whole expression
NOTE: Treats i=0 or X**0 as an exception to not print x**0
'''
def completeExpansion(expression, MaxPower):
    expansion = sp.poly(sp.expand(expression))
    result=""
    for i in range(MaxPower +1):
        if i == 0:
            result += str(expansion.coeff_monomial(x**i))
        else:
            result = result + " + " + (str(expansion.coeff_monomial(x**i))+ "*"+ str(x**i))
    return(result)



expression1 = "(1-p*x)**5"

def unkownExpansion(expression, xterm):
    r = int()
    for i in range(len(expression)):
        if expression[i].isalpha() and expression[i] != 'x':
            a = sp.symbols(expression[i])
    termCoeff, termPower = sp.sympify(xterm).as_base_exp()
    #print(termPower)
    expr, MaxPower = sp.sympify(expression).as_base_exp()
    var1 = x
    var2 = 1/x
    #eqn = 
    r = sp.solveset((0**(MaxPower - r) * x**(r), 3), r)
    print(r)
    
    # termCoeff = sp.poly(sp.sympify(xterm)).coeff_monomial(x**i)



print(unkownExpansion(expression1, "-2160*x**3"))




