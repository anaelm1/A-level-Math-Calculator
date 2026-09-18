'''
Coded by Anael.
We are making the main infrastructure using Flask and Django as it will allow to make a really similar design to DESMOS.
Tkinter was hard to work with esp in design.
'''



from flask import Flask, flash, redirect, render_template, request

from Quadratics import Quadratics
from Trigonometry import Trigonometry
#from Series import 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

