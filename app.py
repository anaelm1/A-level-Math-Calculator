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
from Integration import integration
from Differentiation import differentiation
from Arithmetic import Arithmetic
from Geometric import Geometric
from helperFunctions import *

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'local-development-fallback-key')


@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        session["topic"] = request.form.get("topic")
        session["subTopic"] = request.form.get("subTopic")
        return redirect("/solver")
    else: 
        return render_template("index.html")


@app.route("/solver", methods=["GET", "POST"])
def solver():
    buttonsData = [
        #Row 1: Inverse Trig x y 
        {"id": "btn_asin", "label": "sin⁻¹", "value": "sin⁻¹(", "css_class": "btn-func"},
        {"id": "btn_acos", "label": "cos⁻¹", "value": "cos⁻¹(", "css_class": "btn-func"},
        {"id": "btn_atan", "label": "tan⁻¹", "value": "tan⁻¹(", "css_class": "btn-func"},
        {"id": "btn_x", "label": "x", "value": "x", "css_class": "btn-op"},
        {"id": "btn_y", "label": "y", "value": "y", "css_class": "btn-op"},

        #Row 2: Standard Trig 
        {"id": "btn_sin", "label": "sin", "value": "sin(", "css_class": "btn-func"},
        {"id": "btn_cos", "label": "cos", "value": "cos(", "css_class": "btn-func"},
        {"id": "btn_tan", "label": "tan", "value": "tan(", "css_class": "btn-func"},

        # Row 3: Powers & Roots 
        {"id": "btn_sqr", "label": "x²", "value": "^2", "css_class": "btn-func"},
        {"id": "btn_cube", "label": "x³", "value": "^3", "css_class": "btn-func"},
        {"id": "btn_pow", "label": "xⁿ", "value": "^", "css_class": "btn-func"},
        {"id": "btn_sqrt", "label": "√", "value": "√(", "css_class": "btn-func"},
        {"id": "btn_cbrt", "label": "∛", "value": "∛(", "css_class": "btn-func"},

        # Row 6: Brackets Constants
        {"id": "btn_lparen", "label": "(", "value": "(", "css_class": "btn-func"},
        {"id": "btn_rparen", "label": ")", "value": ")", "css_class": "btn-func"},
        {"id": "btn_pi", "label": "π", "value": "π", "css_class": "btn-func"},
        {"id": "btn_e", "label": "e", "value": "e", "css_class": "btn-func"},

        # Row 7: Keypad (7-9)
        {"id": "btn_7", "label": "7", "value": "7", "css_class": "btn-num"},
        {"id": "btn_8", "label": "8", "value": "8", "css_class": "btn-num"},
        {"id": "btn_9", "label": "9", "value": "9", "css_class": "btn-num"},
        {"id": "btn_infinity", "label": "oo", "value": "oo", "css_class": "btn-num"}, #double 0 is infinity is sympy


        # Row 8: Keypad (4-6) 
        {"id": "btn_4", "label": "4", "value": "4", "css_class": "btn-num"},
        {"id": "btn_5", "label": "5", "value": "5", "css_class": "btn-num"},
        {"id": "btn_6", "label": "6", "value": "6", "css_class": "btn-num"},
        {"id": "btn_mul", "label": "*", "value": "*", "css_class": "btn-op"},
        {"id": "btn_div", "label": "÷", "value": "/", "css_class": "btn-op"},

        # Row 9: Keypad (1-3) & Basic Operators 
        {"id": "btn_1", "label": "1", "value": "1", "css_class": "btn-num"},
        {"id": "btn_2", "label": "2", "value": "2", "css_class": "btn-num"},
        {"id": "btn_3", "label": "3", "value": "3", "css_class": "btn-num"},
        {"id": "btn_add", "label": "+", "value": "+", "css_class": "btn-op"},
        {"id": "btn_sub", "label": "-", "value": "-", "css_class": "btn-op"},

        # Row 10: 0, Decimal, Comma, delete equals to 
        {"id": "btn_0", "label": "0", "value": "0", "css_class": "btn-num"},
        {"id": "btn_dot", "label": ".", "value": ".", "css_class": "btn-num"},
        {"id": "btn_equalsto", "label": "=", "value": "=", "css_class": "btn-op"},
        {"id": "btn_del", "label": "DEL", "value": "DEL", "css_class": "btn-action"}
    ]

    if request.method == "POST":
        session['userExpression'] = request.form.get('userExpression', '')
        if request.form.get("solve") == "True" or "solve" in request.form:
            if not session.get("topic") or not session.get("subTopic"):
                return redirect("/")
            else:
                return redirect("/answer")
        else:
            return render_template('solver.html', userExpression=session['userExpression'], buttonsData=buttonsData)
    else:
        session.pop('userExpression', None)
        return render_template('solver.html', userExpression="", buttonsData=buttonsData)

    
@app.route("/answer")
def answer():
    userExpression = session['userExpression']
    cleanedInput = inputCleaner(userExpression)
    return render_template("answer.html")

