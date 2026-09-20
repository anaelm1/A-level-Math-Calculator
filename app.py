'''
Coded by Anael.
We are making the main infrastructure using Flask and Django as it will allow to make a really similar design to DESMOS.
Tkinter was hard to work with esp in design.

'''


import os
from flask import Flask, flash, redirect, render_template, request, jsonify, session

from Quadratics import Quadratics 
from Trigonometry import Trigonometry
#from Series import 

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'local-development-fallback-key')


@app.route("/", methods=["GET", "POST"])
def index(): 
    topics =  {} #need to fil
    if request.method == "POST":
        session["topic"] = request.form.get("topic")
        session["subTopic"] = request.form.get("subTopic")
        return redirect("/solver")
    else: 
        return render_template("index.html", topics=topics)


@app.route("/solver", methods=["GET", "POST"])
def solver():
    buttonsData = [
        #Row 1: Calculus & Inverse Trig
        {"id": "btn_diff", "label": "d/dx", "value": "d/dx(", "css_class": "btn-func"},
        {"id": "btn_integ", "label": "∫", "value": "∫(", "css_class": "btn-func"},
        {"id": "btn_asin", "label": "sin⁻¹", "value": "sin⁻¹(", "css_class": "btn-func"},
        {"id": "btn_acos", "label": "cos⁻¹", "value": "cos⁻¹(", "css_class": "btn-func"},
        {"id": "btn_atan", "label": "tan⁻¹", "value": "tan⁻¹(", "css_class": "btn-func"},

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

        # --- Row 6: Brackets, Constants & Recall ---
        {"id": "btn_lparen", "label": "(", "value": "(", "css_class": "btn-func"},
        {"id": "btn_rparen", "label": ")", "value": ")", "css_class": "btn-func"},
        {"id": "btn_pi", "label": "π", "value": "pi", "css_class": "btn-func"},
        {"id": "btn_e", "label": "e", "value": "e", "css_class": "btn-func"},

        # --- Row 7: Keypad (7-9) & Clear Controls ---
        {"id": "btn_7", "label": "7", "value": "7", "css_class": "btn-num"},
        {"id": "btn_8", "label": "8", "value": "8", "css_class": "btn-num"},
        {"id": "btn_9", "label": "9", "value": "9", "css_class": "btn-num"},

        # --- Row 8: Keypad (4-6) & Basic Operators ---
        {"id": "btn_4", "label": "4", "value": "4", "css_class": "btn-num"},
        {"id": "btn_5", "label": "5", "value": "5", "css_class": "btn-num"},
        {"id": "btn_6", "label": "6", "value": "6", "css_class": "btn-num"},
        {"id": "btn_mul", "label": "x", "value": "*", "css_class": "btn-op"},
        {"id": "btn_div", "label": "÷", "value": "/", "css_class": "btn-op"},

        # --- Row 9: Keypad (1-3) & Basic Operators ---
        {"id": "btn_1", "label": "1", "value": "1", "css_class": "btn-num"},
        {"id": "btn_2", "label": "2", "value": "2", "css_class": "btn-num"},
        {"id": "btn_3", "label": "3", "value": "3", "css_class": "btn-num"},
        {"id": "btn_add", "label": "+", "value": "+", "css_class": "btn-op"},
        {"id": "btn_sub", "label": "-", "value": "-", "css_class": "btn-op"},

        # --- Row 10: 0, Decimal, Comma, Notation & Execute ---
        {"id": "btn_0", "label": "0", "value": "0", "css_class": "btn-num"},
        {"id": "btn_dot", "label": ".", "value": ".", "css_class": "btn-num"},
        {"id": "btn_del", "label": "DEL", "value": "DEL", "css_class": "btn-action"}
    ]

    if request.method == "POST":
        session['user_expression'] = request.form.get('userExpression', '')
        if request.form.get("solve") == "True" or "solve" in request.form:
            if not session.get("topic") or not session.get("subTopic"):
                return redirect("/")
            else:
                return redirect("/answer")
        else:
            return render_template('solver.html', user_expression=session['user_expression'], buttonsData=buttonsData)
    else:
        session.pop('user_expression', None)
        return render_template('solver.html', user_expression="", buttonsData=buttonsData)

    
@app.route("/answer")
def answer():
    #equation gets calculated here.
    return render_template("answer.html")