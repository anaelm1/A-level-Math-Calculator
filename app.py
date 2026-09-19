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


'''
index is the homepage. On this page there will be the answer box and the keypad to type stuff. After the user is done typing, he will press the
calculate button and the equation will be sent to app.py (after topic selection page) as a post (to the calculate route). Along with this, the topic and the subtopic will also be sent to the app.py 
in a separate screen. 
'''

buttons_data = [
    # --- Row 1: Calculus & Inverse Trig ---

    # --- Row 2: Standard Trig & Logs ---
    {"id": "btn_sin", "label": "sin", "value": "sin(", "css_class": "btn-func"},
    {"id": "btn_cos", "label": "cos", "value": "cos(", "css_class": "btn-func"},
    {"id": "btn_tan", "label": "tan", "value": "tan(", "css_class": "btn-func"},

    # --- Row 3: Powers & Roots ---
    {"id": "btn_sqr", "label": "x²", "value": "^2", "css_class": "btn-func"},
    {"id": "btn_cube", "label": "x³", "value": "^3", "css_class": "btn-func"},
    {"id": "btn_pow", "label": "xⁿ", "value": "^", "css_class": "btn-func"},
    {"id": "btn_sqrt", "label": "√", "value": "sqrt(", "css_class": "btn-func"},
    {"id": "btn_cbrt", "label": "∛", "value": "cbrt(", "css_class": "btn-func"},

    # --- Row 4: Exponential, Inverse & Custom Log ---
    {"id": "btn_exp_e", "label": "eˣ", "value": "e^", "css_class": "btn-func"},
    {"id": "btn_exp_10", "label": "10ˣ", "value": "10^", "css_class": "btn-func"},
    {"id": "btn_inv", "label": "x⁻¹", "value": "^(-1)", "css_class": "btn-func"},
    {"id": "btn_frac", "label": "a/b", "value": "/", "css_class": "btn-func"},

    # --- Row 5: Combinatorics, Signs & Formatting ---
    {"id": "btn_ncr", "label": "nCr", "value": "nCr(", "css_class": "btn-func"},
    {"id": "btn_npr", "label": "nPr", "value": "nPr(", "css_class": "btn-func"},
    {"id": "btn_fact", "label": "x!", "value": "!", "css_class": "btn-func"},
    {"id": "btn_sd", "label": "S⇔D", "value": "TOGGLE_FORMAT","css_class": "btn-ctrl"},

    # --- Row 6: Brackets, Constants & Recall ---
    {"id": "btn_lparen", "label": "(", "value": "(", "css_class": "btn-func"},
    {"id": "btn_rparen", "label": ")", "value": ")", "css_class": "btn-func"},
    {"id": "btn_pi", "label": "π", "value": "pi", "css_class": "btn-func"},
    {"id": "btn_e", "label": "e", "value": "e", "css_class": "btn-func"},

    # --- Row 7: Keypad (7-9) & Clear Controls ---
    {"id": "btn_7", "label": "7", "value": "7", "css_class": "btn-num"},
    {"id": "btn_8", "label": "8", "value": "8", "css_class": "btn-num"},
    {"id": "btn_9", "label": "9", "value": "9", "css_class": "btn-num"},
    {"id": "btn_del", "label": "DEL", "value": "DEL", "css_class": "btn-danger"},
    {"id": "btn_ac", "label": "AC", "value": "CLEAR", "css_class": "btn-danger"},

    # --- Row 8: Keypad (4-6) & Basic Operators ---
    {"id": "btn_4", "label": "4", "value": "4", "css_class": "btn-num"},
    {"id": "btn_5", "label": "5", "value": "5", "css_class": "btn-num"},
    {"id": "btn_6", "label": "6", "value": "6", "css_class": "btn-num"},
    {"id": "btn_mul", "label": "×", "value": "*", "css_class": "btn-op"},
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
    {"id": "btn_exp", "label": "×10ⁿ", "value": "*10^", "css_class": "btn-op"},
    {"id": "btn_eq", "label": "=", "value": "=", "css_class": "btn-action"}
]

@app.route("/", methods = ["GET", "POST"])
def index(): 
    user_expression = ""

    if request.method == "POST":

        if request.form.get("solve") == "True":
            return redirect("/topic")

        user_expression = request.form.get('userExpression', '')
        print("Received from frontend:", user_expression)
        return render_template('index.html', user_expression=user_expression)

        
    else:
        
        return render_template("index.html")


@app.route("/topic", methods = ["GET", "POST"])
def topic():
    if request.method == "POST":
        session["topic"] = request.form.get("topic")
        #session["subTopic"] = request.form.get("subTopic")
        #session["userExpression"] = request.form.get("userExpression")
        #solving funcs calling here
        answer = "Answerrr"
        return render_template("answer.html", answer = answer)
    else: 
        return render_template("topicSelection.html")

    
@app.route("/base")
def test():
    return render_template("base.html")