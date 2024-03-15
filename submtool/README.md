# Homework Submission Tool
## description
This Flask application is designed to facilitate the submission and review workflow for the homeworks from the [Pyladies Vienna courses](https://pyladies.at/runs/). 

This tool provides an easy a fast way for course participants to submit their homework. For the course instructors and mentors the tool allows to view submitted homeworks, filter homeworks by name or lesson number and check missing submissions.

### features
* Submit homework (form.html): <br/>
Pyladies can submit their homeworks by providing their name, lesson number, Colab or GitHub URL, and comments. The name, lesson number and link for the homework are mandatory fields while the comments field is optional.  After filling the form, the user should review the inserted information and make sure that the Colab notebook has permissions set correctly: "Anyone with link can edit". In addition, users should keep in mind they have to submit the homework by the same name every time so that it's managing would be possible later.
After the user pressed the the "submit" button, the data is stored in a CSV file, timestamped and backed up, and the page is redirected to the "done" route, where a confirmation of the submition is presented.

* View submitted homeworks (view_homework.html): <br/>
Page with authentication where mentors have an overview over the submitted homeworks in a tabular format. There is also the possibility of keeping track of reviewed homework for the convenience of the instructors. The status of a homework submission can be "open" for an unreviewed submission, or the status can be changed to "done" after it has been examined. A field for adding the reviewers name is also available but not mandatory. In this page is also a link "filter" for the route (select_name.html) where the table can be filtered by a name or a lesson number selected from a list.

* On route (missing.html) Instructors can check for missing homeworks by student names.

## technologies
html/css <br/>
python <br/>

Flask <br/>
Flask_HTTPAuth <br/>
The app is hosted on www.pythonanywhere.com

## Installation and Usage

Access to the application through web browser at: https://pyladiesvienna.pythonanywhere.com/submtool <br/>
git clone https://github.com/YanaMartin/Homework_tool.git
cd Homework_tool
cd submtool
flask run

## status
in progress

## credits
Daniela Limbeck <br/>
Yana Martin
