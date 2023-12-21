from flask import Flask, flash, redirect, render_template, request, session, abort
import os
app = Flask(__name__)
@app.route("/submtool")
def hello():
    return render_template(
'form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        formdata = request.form
        return render_template('data.html', formdata = formdata)

if __name__ == "__main__":
    app.run()


    
    
