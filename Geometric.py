'''
Coded by Anael. Geometric is one of the sub topics of series, and it has these sub topics:
    1. nth term from a and r
    2. a and r from 2 terms
    3. sum to nth term from a and r 
    4. sum to infinity    

a is the first term. r is the common ratio. 

formulas we will use: 
1) ar**(n-1) = nth term
2) r = tn+1/tn
3) sum to nth = a((1-r**n)/1-r))
4) sum to infinity = a/(1-r)

It is similar to arithmetic except for that it has common ratio rather than difference
'''

from helperFunctions import *
from sympy import *

def Geometric(method=None, a=None, r=None, n=None, term1=None, term2=None):
    if method:
        try:
            match method:
                case 1: return nthTerm(n, r, a)
                case 2: raFromtwoTerms(term1, term2)
                case 3: sumFromra(n, r, a)
                case 4: sumtoInfinity(term1, term2)
        except:
            return (ReturnDict(solved=False))

def nthTerm(n, r, a):
    try:
        nth = a*r**(n-1)
        nth = f"{n}th term is {roundingPlaces(nth)}"
        return (ReturnDict(solved=True, answer_string=nth))
    except:
        return (ReturnDict(solved=False))

#term1/term2 are both lists with n on 0 index and its value on 1 index
def raFromtwoTerms(term1, term2): 
    try:
        a, r = symbols('a r')

        eqn1 = Eq(a*r**(term1[0]-1), term1[1])
        eqn2 = Eq(a*r**(term2[0]-1), term2[1])
        answer = []
        solution = solve((eqn1, eqn2), (a, r))
        print(solution)
        for sol in solution:
            answer.append(f'a = {roundingPlaces(sol[0])}')
            answer.append(f'r = {roundingPlaces(sol[1])}')
            answer.append('or')

        if answer[-1] == 'or':
            answer.pop()
        
        return (ReturnDict(True, answer_string = answer))
    except:
        return (ReturnDict(False))
 
def sumFromra(n, r, a):
    try:
        sum = a*((1 - r**n) / (1 - r))
        answer = f'Sum to {n}th term is {roundingPlaces(sum)}'
        return (ReturnDict(True, answer_string = answer))
    except:
        return (ReturnDict(False))

def sumtoInfinity(r, a):
    try:
        sum = a/(1-r)
        answer = f'Sum to infinity is {roundingPlaces(sum)}'
        return (ReturnDict(True, answer_string=answer))
    except:
        return (ReturnDict(False))

#Test
#print(nthTerm(4, 3, 2))
#print(raFromtwoTerms(term1=[1, 5], term2=[3, 20]))
#print(sumFromra(3, 1/2, 5))
#print(sumtoInfinity(0.5, 10))
