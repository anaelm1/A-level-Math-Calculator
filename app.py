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
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'local-development-fallback-key')


@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        session["buttonNumber"] = request.form.get("subTopicId") 
        topic, session["subTopic"] = session["buttonNumber"].split(".")
        match topic:
            case 1:
                session["topic"] = "Quadratics"
            case 2:
                session["topic"] = "Binomial"
            case 3:
                session["topic"] = "Arithmetic"
            case 4:
                session["topic"] = "Geometric"
            case 5:
                session["topic"] = "Trigonometry"
            case 6:
                session["topic"] = "Differentiation"
            case 7:
                session["topic"] = "Integration"
        return redirect("/grid")
    else: 
        return render_template("index.html")


@app.route("/grid", methods=["GET", "POST"])
def grid():
    parameters = {
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

    4.1: "Enter n, d, a" ,
    4.2: "Enter T1, T2" ,
    4.3: "Enter n, d, a" ,
    4.4: "Enter n, T1, T2" ,
    4.5: "Enter d, a" ,

    5.1: "Enter Angle Mode, Exp, Start, Stop" ,
    5.2: "Enter Angle Mode, Exp, Start, Stop" ,

    6.1: "Enter Exp, Line Type, X" ,
    6.2: "Enter Exp, Line Type, Y, Range" ,
    6.3: "Enter Exp, Range" ,
    6.4: "Enter Exp, m, X, Range" ,
    6.5: "Enter Exp, X cords" ,
    6.6: "Enter Exp" ,
    6.7: "Enter Exp" ,

    7.1: "Enter Exp, Coordinates" ,
    7.2: "Enter Exp, limits" }

    number = float(session['buttonNumber'])
    outputedString = parameters[number]
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
    userExpression = session['userExpression']
    cleanedInput = inputCleaner(userExpression)
    return render_template("answer.html")

@app.route("/graph")
def graph():
    userExpression = session['userExpression']
    cleanedInput = inputCleaner(userExpression)
    mode = session['mode']
    lower = session['lowerLimit']
    upper = session['upperLimit']

    limit0Str = str(lower).replace("sp.", "math.")
    limit1Str = str(upper).replace("sp.", "math.")
    expression = expression.replace("sp.", "math.")

    plotUrl = Plotter(cleanedInput, mode, [limit0Str, limit1Str])

    return render_template("graph.html", plotUrl=plotUrl)
