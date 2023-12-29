from flask import Flask, render_template, request
import os
import csv
from datetime import datetime

app = Flask(__name__)

def write_to_csv(data):
    """Function to write data to a CSV file with timestamp"""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    data_with_timestamp = data + [timestamp]
    with open('homework_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_with_timestamp)
    file.close()

@app.route("/submtool")
def hello():
    return render_template('form.html')

@app.route('/done', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        formdata = request.form
        name = request.form['name']
        lesson_number = request.form['lesson_number']
        colab_url = request.form['colab_url']
        comments = request.form['comments']
        
        data = [name, lesson_number, colab_url, comments]
        write_to_csv(data)
        return render_template('done.html', data = formdata)
            
@app.route('/view-homework', methods = ['POST', 'GET'])
def view_homework():
    """Page to view all submitted homework data from CSV"""
    if request.method == 'GET':
        data = []
        with open('homework_data.csv', mode='r') as file:
            reader = csv.reader(file)        
            next(file)
            for row in reader:
                data.append(row)
            return render_template('view_homework.html', homework = data)
        

if __name__ == "__main__":
    app.run()


    
    
    
