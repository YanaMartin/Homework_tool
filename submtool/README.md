# Homework Submission Tool
## description
This Flask application is designed to facilitate the submission and review workflow for the homeworks from the [Pyladies Vienna courses] (https://pyladies.at/runs/). 
Various web interfaces allow course attendees to hand in homeworks that afterwards can be checked and reviewed by the course mentors.

### features
#### Submit homework (form.html)
Users can submit name, lesson number, Colab URL to the homework, and comments via a form, the data is stored in a CSV file. After that they are redirected to a "done" page.

#### View submitted homeworks (view_homework.html): 
Page with authentication where mentors have an overview over the submitted homeworks in a tabular format. They can mark a homework as done and add the reviewers name.

#### check missing homeworks (missing.html)
see submitted homeworks per user, select from list

## technologies
html/css
python

flask 
flask_httpauth

## install and usage

git clone [git@gitlab.com:tuub/Homework_tool.git](https://github.com/YanaMartin/Homework_tool.git)
cd Homework_tool
cd submtool
flask run

## status
in progress

# Credits
Daniela Limbeck
Yana Martin
