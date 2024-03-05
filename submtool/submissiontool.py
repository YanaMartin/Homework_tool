from flask import Flask, render_template, request
import os
import csv
import glob
import time
import shutil
import json
from datetime import datetime
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

'''
def backup():
    list_of_files = glob.glob('backups/*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    crtime = datetime.strptime(time.ctime(os.path.getctime(latest_file)), "%a %b %d %H:%M:%S %Y")
    local_time = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    if crtime < local_time:
        now = datetime.now()
        timestamp = str(now.strftime("%Y%m%d"))
        filename = "homework_" + timestamp
        shutil.copyfile('homework_data.csv', './backups/{}.csv'.format(filename))
'''
         

def write_to_csv(data):
    """Function to write data to a CSV file with timestamp"""
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('homework_data.csv', newline='') as file:
        reader = csv.reader(file)
        rownum = int(sum(1 for row in reader))
    data_with_timestamp = data[0:4] + [timestamp] + data[4:] + [rownum]
    
    with open('homework_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_with_timestamp)
    file.close()

@auth.verify_password
def verify_password(username, password):
    
    file = open("credentials.js")
    creds = json.load(file)
    print(creds)
    if username in creds and check_password_hash(generate_password_hash(creds.get(username)), password):
        return True
       

@app.route("/submtool")
def hello():
    #backup()
    return render_template('form.html')

@app.route('/done', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        formdata = request.form
        name = request.form["name"].lower()
        lesson_number = request.form["lesson_number"]
        colab_url = request.form["colab_url"]
        comments = request.form["comments"]
        checked = request.form["checked"]
        mentorname = request.form["mentorname"]
        data = [name, lesson_number, colab_url, comments, checked, mentorname]
        write_to_csv(data)
        return render_template('done.html', data = formdata)
            
@app.route('/view-homework', methods = ['POST', 'GET'])
@auth.login_required
def view_homework():
    """Page to view all submitted homework data from CSV"""

    row_id = []
    with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            next(reader)
            for row in reader:
                row_id.append(row[7])

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

        for row in sortedcsv[1:]:
            data.append(row)   
        
        return render_template('view_homework.html', homework = data)  
    
    if request.method == 'POST':        
               
        stati = []
        for status in request.form.getlist("status"):
            stati.append(status)

        mentors = []
        for mentorname in request.form.getlist("mentorname"):
            mentors.append(mentorname)

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
                if row_id[i] == row[7]:
                    row = row[0:5] + [status] + [newdata] + [row[7]]
                else:
                    row = row
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
    
    
@app.route("/missing", methods = ['POST', 'GET'])
@auth.login_required
def missing():
    """Page to check missing homeworks"""

    if request.method == 'GET':
        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            next(reader)
            names = []
            for row in reader:
                names.append(row[0])
                sortcsv = sorted(set(names))
            return render_template('missing.html', homework = sortcsv) 

    if request.method == 'POST':        
        names = []
        for name in request.form.getlist("name"):
            names.append(name) 
            names = list(set(names))

        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            next(reader)
            nums = []
            for row in reader:
                if row[0] in names:
                    nums.append(int(row[1]))
                    nums = sorted(set(nums))
                     
        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            next(reader)
            data = []
            for row in reader:
                data.append(row[0])
                sortcsv = sorted(list(set(data)))
        return render_template('missing.html', homework = sortcsv, nums = nums) 
    
    
def get_names():
    """Function to get a list of all names from the CSV"""
    names = set()
    with open('homework_data.csv', newline='') as filein:
        reader = csv.reader(filein)
        next(reader)  
        for row in reader:
            names.add(row[0])
    return sorted(names)

def get_lesson_numbers():
    """Function to get a list of all lesson numbers from the CSV"""
    lesson_numbers = set()
    with open('homework_data.csv', newline='') as filein:
        reader = csv.reader(filein)
        next(reader) 
        for row in reader:
            lesson_numbers.add(row[1])
    return sorted(lesson_numbers)

@app.route('/select-name', methods=['GET', 'POST'])
def select_name():
    """Filter homework data based on selected name or lesson number"""
    if request.method == 'GET':
        names = get_names()
        lesson_numbers = get_lesson_numbers()
        return render_template('select_name.html', names=names, lesson_numbers=lesson_numbers)

    if request.method == 'POST':
        #selected_name = request.form.getlist('selected_name')
        selected_lesson = request.form.get('selected_lesson')

        names = []
        for name in request.form.getlist("selected_name"):
            names.append(name) 
            names = list(set(names))

        filtered_homework = []
        with open('homework_data.csv', newline='') as filein:
            reader = csv.reader(filein)
            next(reader) 
            for row in reader:
                if (row[0] in names) or (selected_lesson and row[1] == selected_lesson):
                    filtered_homework.append(row)

        return render_template('filtered_homework.html', name=names, lesson=selected_lesson, homework=filtered_homework)
    

if __name__ == "__main__":
    app.run()