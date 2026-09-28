'''
Coded by Anael. This is an universal plotter which will plot trignometric curves. 
It will take input the expression as a string and the lower limit and upper limit. Mode is RAD or DEG
then it will decide the step and and plot the curve.
'''

import io
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp
import math
import numpy as np
from helperFunctions import *
import re


def Plotter(expression=None, mode='RAD', range_lower=None, range_upper=None):
    try:
        if expression is None or range_lower is None or range_upper is None:
            return (ReturnDict(False))

        if isinstance(range_lower, (list, tuple)):
            range_upper = range_lower[1]
            range_lower = range_lower[0]  

        lowerlimit = float(sp.N(range_lower))
        upperlimit = float(sp.N(range_upper))

        functions = r'\b(sin|cos|tan)\s*\(' #\b is boundary, sin cos tan are the options, \s* is 0 gaps or more, open bracket is the opening 
        period = 0
        step = (upperlimit - lowerlimit) / 100.0 #default 
        pointsPerPeriod = 50 #can be changed. 

        for match in re.finditer(functions, expression, re.IGNORECASE): #find functions in expression ignoring case. this syntax is new
            function = match.group(1)
            startingIndex = match.start()
            endingIndex = match.end()
            openingBracketIndex = endingIndex-1

            currentIndex = int((openingBracketIndex))
            found = False

            closingBracketIndex = len(expression)
            
            while (currentIndex < len(expression) - 1 and not found):
                char = expression[currentIndex]
                if char == ')':
                    closingBracketIndex = currentIndex
                    found = True
                currentIndex += 1

            b = expression[openingBracketIndex + 1: closingBracketIndex]
            b = b.replace("*", "").replace("x", "")

            try:
                b = float(b)
            except ValueError:
                b = 1.0

            if mode == 'DEG':
                if function == 'tan':
                    period = 180/b
                else: 
                    period = 360/b
            else:
                if function == 'tan':
                    period = sp.pi/b
                else: 
                    period = (2*sp.pi)/b

            period = roundingPlaces(float(sp.N(period)))
            step = roundingPlaces(period/pointsPerPeriod)

        symbol = sp.Symbol('x')
        expression = sp.sympify(expression)

        if mode == "DEG":
            expression = expression.subs(symbol, symbol * sp.pi / 180)

        f = sp.lambdify(symbol, expression, 'numpy')

        x = np.arange(lowerlimit, upperlimit + (step / 2), step)

        y = f(x) 

        plt.figure(figsize=(10, 4))
        plt.plot(x, y, label=f"y = {expression}", color="purple", linewidth=1.5)

        #plotting the min max values (amplitude)
        yMin = np.min(y)
        yMax = np.max(y)
        plt.axhline(yMin, color='blue', linestyle=':', linewidth=1.2, label=f"Min: {yMin:.2f}")
        plt.axhline(yMax, color='red', linestyle=':', linewidth=1.2, label=f"Max: {yMax:.2f}")

        plt.title(f"Plot of: {expression}", fontsize=12)
        plt.xlabel("x", fontsize=10)
        plt.ylabel("y", fontsize=10)
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend()

        img_buf = io.BytesIO()
        plt.savefig(img_buf, format="png", bbox_inches="tight")
        img_buf.seek(0)
        plt.close()

        return base64.b64encode(img_buf.getvalue()).decode("utf-8") 

    except:
        return (ReturnDict(False))

#Testing
#print(Plotter("cos(x)", "RAD", [-sp.pi, sp.pi]))
#print(Plotter("-sin(3*x)", "RAD", [0, math.pi]))
#print(Plotter("sin(2*x) + cos(3*x)", "RAD", [0, 2 * math.pi]))
#print(Plotter("sin(x)", "RAD", [0, 2 * math.pi]))
#print(Plotter("cos(x)", "RAD", [0, 2 * math.pi]))
#print(Plotter("tan(x)", "RAD", [-math.pi / 4, math.pi / 4]))
#print(Plotter("sin(x)", "DEG", [0, 360]))
#print(Plotter("cos(x)", "DEG", [0, 360]))
#print(Plotter("tan(x)", "DEG", -45, 45))