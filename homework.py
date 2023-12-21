from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def submit_homework():
    """Home page with form to submit homework"""
    if request.method == 'POST':
        name = request.form['name']
        lesson_number = request.form['lesson_number']
        colab_url = request.form['colab_url']
        comments = request.form['comments']

        return redirect(url_for('thank_you'))
    return render_template('name.html')

@app.route('/thank-you')
def thank_you():
    """Thank you page after submitting homework succesfully"""
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run()