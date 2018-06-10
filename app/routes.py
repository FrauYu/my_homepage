from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    
    return render_template('home.html', title='Home')

@app.route('/environment')
def environment():
    
    return render_template('environment.html', title='Environment')

@app.route('/framework')
def framework():
    
    return render_template('framework.html', title='Framework')

@app.route('/reference')
def reference():
    
    return render_template('reference.html', title='References')

@app.route('/summary')
def summary():
    
    return render_template('summary.html', title='Summary')

