'''
Coded by Anael.
We are making the main infrastructure using Flask and Django as it will allow to make a really similar design to DESMOS.
Tkinter was hard to work with esp in design.

'''


import os
from flask import Flask, flash, redirect, render_template, request, jsonify, session

from Quadratics import Quadratics 
from Trigonometry import Trigonometry
from Binomial import Binomial
from Integration import Integration
from Differentiation import Differentiation
from Arithmetic import Arithmetic
from Geometric import Geometric
from Plotter import Plotter
from helperFunctions import *
import math

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key_for_dev')

TOPIC_NAMES = {
    "1": "Quadratics",
    "2": "Binomial",
    "3": "Arithmetic",
    "4": "Geometric",
    "5": "Trigonometry",
    "6": "Differentiation",
    "7": "Integration",
}

PARAMETERS = {
    1.1: "Enter Exp",
    1.2: "Enter Exp",
    1.3: "Enter Exp",
    1.4: "Enter Exp",
    1.5: "Enter Exp",

    2.1: "Enter Exp, Power",
    2.2: "Enter Exp, Power",
    2.3: "Enter Exp, Power, Range",
    2.4: "Enter Exp, Power, Range",

    3.1: "Enter n, d, a" ,
    3.2: "Enter T1, T2" ,
    3.3: "Enter n, d, a" ,
    3.4: "Enter n, T1, T2" ,
    3.5: "Enter d, a" ,

    4.1: "Enter n, r, a" ,
    4.2: "Enter T1, T2" ,
    4.3: "Enter n, r, a" ,
    4.4: "Enter r, a",

    5.1: "Enter Angle Mode, Exp, Start, Stop" ,
    5.2: "Enter Angle Mode, Exp, Start, Stop" ,

    6.1: "Enter Exp, Line Type, X" ,
    6.2: "Enter Exp, Line Type, Y, Range" ,
    6.3: "Enter Exp, Range" ,
    6.4: "Enter Exp, m, X, Range" ,
    6.5: "Enter Exp, X cords" ,
    6.6: "Enter Exp" ,
    6.7: "Enter Exp" ,
    6.8: "Enter Exp" ,

    7.1: "Enter Exp, Coordinates" ,
    7.2: "Enter Exp, limits" }

def solveUserInput(topic, method,  rawInput):
    rawInput = inputCleaner(rawInput)
    parts = splitArgs(rawInput)
    if not parts:
        return ReturnDict(False)

    if topic == "Quadratics":
        return Quadratics(method, prepareExpression(rawInput))

    if topic == "Binomial":
        expression = prepareExpression(parts[0])
        if len(parts) > 1:
            power = prepareExpression(parts[1])
        else:
            None
        if len(parts) > 2:
            optRange = parts[2]
        else: 
            None 
        return Binomial(method, expression, power, optRange)

    if topic == "Arithmetic":
        if method == 1:
            n, d, a = parseInt(parts[0]), parseNumber(parts[1]), parseNumber(parts[2])
            return Arithmetic(1, n=n, d=d, a=a)
        if method == 2:
            term1, term2 = parseTwoTerms(parts)
            return Arithmetic(2, term1=term1, term2=term2)
        if method == 3:
            n, d, a = parseInt(parts[0]), parseNumber(parts[1]), parseNumber(parts[2])
            return Arithmetic(3, n=n, d=d, a=a)
        if method == 4:
            n = parseInt(parts[0])
            term1, term2 = parseTwoTerms(parts[1:])
            return Arithmetic(4, n=n, term1=term1, term2=term2)
        if method == 5:
            d, a = parseNumber(parts[0]), parseNumber(parts[1])
            return Arithmetic(5, d=d, a=a)
        return Arithmetic(method)

    if topic == "Geometric":
        if method == 1:
            n, r, a = parseInt(parts[0]), parseNumber(parts[1]), parseNumber(parts[2])
            return Geometric(1, n=n, r=r, a=a)
        if method == 2:
            term1, term2 = parseTwoTerms(parts)
            return Geometric(2, term1=term1, term2=term2)
        if method == 3:
            n, r, a = parseInt(parts[0]), parseNumber(parts[1]), parseNumber(parts[2])
            return Geometric(3, n=n, r=r, a=a)
        if method == 4:
            r, a = parseNumber(parts[0], parseNumber(parts[1]))
            return Geometric(4, r=r, a=a)
    return (ReturnDict(False))

    if topic == "Trigonometry":
        mode = parseMode(parts[0])
        expression = prepareExpression(parts[1])
        lower = parseNumber(parts[2])
        upper = parseNumber(parts[3])
        if method == 1:
            return Trigonometry(1, mode, expression, lower, upper)
        if method == 2: 
            return Trigonometry(2, mode, expression, lower, upper)
        return ReturnDict(False)

    if topic == "Differentiation":
        expression = prepareExpression(parts[0])
        if method == 1:
            line_type = parseLineType(parts[1])
            x_cord = parseNumber(parts[2])
            return Differentiation(1, expression, line_type, x_cord)
        if method == 2:
            line_type = parseLineType(parts[1])
            y_cord = parseNumber(parts[2])
            given_range = parts[3] if len(parts) > 3 else None
            return Differentiation(2, expression, line_type, y_cord, given_range)
        if method == 3:
            given_range = parts[1] if len(parts) > 1 else None
            return Differentiation(3, expression, given_range)
        if method == 4:
            gradient = parseNumber(parts[1])
            x_cord = parseNumber(parts[2])
            given_range = parts[3] if len(parts) > 3 else None
            return Differentiation(4, expression, gradient, x_cord, given_range)
        if method == 5:
            x_cords = [parseNumber(item) for item in parts[1:]]
            return Differentiation(5, expression, x_cords)
        if method == 6:
            return Differentiation(6, expression)
        if method in (7, 8):
            return Differentiation(7, expression)
        return ReturnDict(False)

    if topic == "Integration":
        expression = prepareExpression(parts[0])
        if method == 1:
            coordinates = [parseNumber(parts[1]), parseNumber(parts[2])]
            return Integration(1, expression, coordinates)
        if method == 2:
            limits = [prepareExpression(parts[1]), prepareExpression(parts[2])]
            return Integration(2, expression, limits)
        return ReturnDict(False)

    return ReturnDict(False)

def currentPrompt():
    number = float(session["buttonNumber"])
    return PARAMETERS.get(number, "Enter values separated by commas")

@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        session["buttonNumber"] = request.form.get("subTopicId") 
        topic, session["subTopic"] = session["buttonNumber"].split(".")
        session["topic"] = TOPIC_NAMES.get(topic)
        if not session["topic"]:
            return redirect("/")
        return redirect("/grid")
    else: 
        return render_template("index.html")


@app.route("/grid", methods=["GET", "POST"])
def grid():
    if "buttonNumber" not in session:
        return redirect("/")
    number = float(session['buttonNumber'])
    outputedString = PARAMETERS[number]
    if request.method == "POST":
        session['userExpression'] = request.form.get('userExpression', '')
        if request.form.get("solve") == "True" or "solve" in request.form:
            if not session.get("topic") or not session.get("subTopic"):
                return redirect("/")
            else:
                return redirect("/answer")
        else:
            return render_template('grid.html', userExpression=session['userExpression'], outputedString=outputedString)
    else:
        session.pop('userExpression', None)
        return render_template('grid.html', userExpression="", outputedString=outputedString)

    
@app.route("/answer")
def answer():
    if not session.get("topic") or "userExpression" not in session:
        return redirect("/")

    userExpression = session.get("userExpression", "")
    try:
        if session["topic"] == "Trigonometry" and int(session["subtopic"]) == 2:
            return redirect("/graph")
        result = solveUserInput(session["topic"], int(session["subTopic"]), userExpression)
        outputedString = formatAnswer(result)
    except Exception:
        outputedString = "Could not solve. Check the input format shown above the display."

    return render_template("answer.html", userExpression=userExpression, outputedString=outputedString)


@app.route("/graph")
def graph():
    if "userExpression" not in session:
        return redirect("/")
    userExpression = session["userExpression"]
    parts = splitArgs(userExpression)
    if len(parts) < 4:
        return render_template("graph.html", plotUrl=None)
    mode = parseMode(parts[0])
    expression = prepareExpression(parts[1])
    lower = parseNumber(parts[2])
    upper = parseNumber(parts[3])
    plotUrl = Plotter(expression, mode, lower, upper)
    if isinstance(plotUrl, dict):
        plotUrl = None
    return render_template("graph.html", plotUrl=plotUrl)

if __name__ == "__main__":
    app.run()