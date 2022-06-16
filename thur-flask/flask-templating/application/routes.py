from flask import Flask, render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/bname')
def bname():
    return render_template('name.html')

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/betty')
def betty():
    return render_template('betty.html')

@app.route('/bobby')
def bobby():
    return render_template('bobby.html')