'''
Coded by Anael. Arithmetic is one of the subtopics of series, and these are its sub topics.
    1. nth term from d and a
    2. d and a from 2 term
    3. sum to nth term from a and d 
    4. sum to nth term from 2 terms
    5. nth term equation from d and a

difference is d. first term is a.

formulas we will use:
1) a + (n-1)d = nth
2) sum to nth term = (n/2) * (2a + (n-1)d)
'''

from helperFunctions import *
from sympy import *

def Arithmetic(method=None, a=None, d=None, n=None, terms=None):
    if method:
        try:
            match method:
                case 1: return nthTerm(n, d, a)
                case 2: return daFromtwoTerms(terms)
                case 3: return sumFromda(n, d, a)
                case 4: return sumFromtwoTerms(n, terms)
                case 5: return eqnFromda(d, a)
        except:
            return (ReturnDict(False))
    else:
        return (ReturnDict(False))

def nthTerm(n, d, a):
    try:
        nth = a + (n-1)*d
        nth = f"{n}th term is {roundingPlaces(nth)}"
        return  (ReturnDict(solved=True, answer_string=nth))
    except:
        return (ReturnDict(False))

#term1/term2 are both dicts [{'n': value}, {'n': value}]
def daFromtwoTerms(terms): 
    try:
        a, d = symbols('a d')

        #Getting n and nth value from my dict in a list data type
        n1 = terms[0].keys() 
        n1 = list(n1)
        n1 = n1[0]
        nth1 = terms[0][n1]
        n1 = int(n1)
        n2 = terms[1].keys() 
        n2 = list(n2)
        n2 = n2[0]
        nth2 = terms[1][n2]
        n2 = int(n2)

        eqn1 = Eq(a + (n1-1)*d, nth1)
        eqn2 = Eq(a + (n2-1)*d, nth2)

        answer = []
        solution = solve((eqn1, eqn2), (a, d))
        answer.append(f'a = {roundingPlaces(solution[a])}')
        answer.append(f'd = {roundingPlaces(solution[d])}')
        
        return (ReturnDict(True, answer_string = answer))
    except:
        return (ReturnDict(False))
    
def sumFromda(n, d, a):
    try:
        sum = (n/2) * (2*a + (n-1)*d)
        answer = f'Sum of {n}th terms is {roundingPlaces(sum)}'
        return (ReturnDict(True, answer_string = answer))
    except:
        return (ReturnDict(False))

def sumFromtwoTerms(n, terms):
    try:
        a, d = symbols('a d')

        #Getting n and nth value from my dict in a list data type
        n1 = terms[0].keys() 
        n1 = list(n1)
        n1 = n1[0]
        nth1 = terms[0][n1]
        n1 = int(n1)
        n2 = terms[1].keys() 
        n2 = list(n2)
        n2 = n2[0]
        nth2 = terms[1][n2]
        n2 = int(n2)

        eqn1 = Eq(a + (n1-1)*d, nth1)
        eqn2 = Eq(a + (n2-1)*d, nth2)

        answer = []
        solution = solve((eqn1, eqn2), (a, d))
        sum = (n/2) * (2*a + (n-1)*d)

        answer = f'Sum of {n}th terms is {roundingPlaces(sum)}'
        return (ReturnDict(True, answer_string = answer))

    except:
        return (ReturnDict(False))

def eqnFromda(d, a):
    try:
        answer = f"nth  term = {roundingPlaces(a)} + (n - 1){roundingPlaces(d)}"
        return (ReturnDict(True, answer_string = answer))
    except: 
        return (ReturnDict(False))


'''
# Test Case
terms = [{3: 10}, {7: 22}]
print(daFromtwoTerms(terms))


n = 10
d = -3
a = 2/7

print((sumFromda(n, d, a)))


d = -3
a = 1/3

print(eqnFromda(d, a))
'''