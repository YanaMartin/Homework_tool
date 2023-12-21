from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
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

        return redirect('/thank-you')
    return render_template('name.html', title='Homework submission', form=form)

if __name__ == "__main__":
    app.run()