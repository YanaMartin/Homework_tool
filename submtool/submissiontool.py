from flask import Flask, render_template, request
import os
import csv
from datetime import datetime

app = Flask(__name__)

def write_to_csv(data):
    """Function to write data to a CSV file with timestamp"""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    data_with_timestamp = data[0:4] + [timestamp] + data[4:]
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
        name = request.form["name"]
        lesson_number = request.form["lesson_number"]
        colab_url = request.form["colab_url"]
        comments = request.form["comments"]
        checked = request.form["checked"]
        mentorname = request.form["mentorname"]
        data = [name, lesson_number, colab_url, comments, checked, mentorname]
        write_to_csv(data)
        return render_template('done.html', data = formdata)
            
@app.route('/view-homework', methods = ['POST', 'GET'])
def view_homework():
    """Page to view all submitted homework data from CSV"""
    if request.method == 'GET':

        sortedcsv = []
        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            sortedcsv.append(next(reader))
            sortedcsv.extend(sorted(reader, key=lambda row: int(row[1])))

        with open('homework_data.csv', mode='w', newline='') as filein:
            writer = csv.writer(filein)
            for row in sortedcsv:
                writer.writerow(row)

        data = []
        i = 0
        nums = []

        for row in sortedcsv[1:]:
            data.append(row)   
            nums.append(i)
            i =+ 1
        return render_template('view_homework.html', homework = data, i = nums)  
    
    if request.method == 'POST':        
               
        stati = []
        for status in request.form.getlist("status"):
            stati.append(status)
            print(stati)

        mentors = []
        for mentorname in request.form.getlist("mentorname"):
            mentors.append(mentorname)
            print(mentors)

        newcsv = []
        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            header = next(reader)
            newcsv.extend(reader)

        with open('homework_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        
        with open('homework_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            i = 0
            for row in newcsv:
                status = stati[i]
                newdata = mentors[i]
                row = row[0:5] + [status] + [newdata]
                i += 1
                writer.writerow(row)

        sortedcsv = []
        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            sortedcsv.append(next(reader))
            sortedcsv.extend(sorted(reader, key=lambda row: int(row[1])))
    
        data = []
        for row in sortedcsv[1:]:
            data.append(row)                
        return render_template('view_homework.html', homework = data)

if __name__ == "__main__":
    app.run()