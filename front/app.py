from flask import Flask, render_template, request, redirect
from config import Config
import threading, webbrowser
import requests
import json

from forms import AccountCreationForm, DemographicForm, CareerInterest, PlacementTest, printUpcomingDates, ScheduleOrientation



app = Flask(__name__)
app.config.from_object(Config)

#Static variable used to keep track of current user. Should be cached instead.
cached_username = None

@app.route('/home/', methods=['GET','POST'])
def renderHome():
    '''
    Renders a viewable web application on your port:
    http://127.0.0.1:5000/home
    '''

    return (render_template('home.html') )

@app.route('/currentstudents/', methods=["GET"])
def renderCurrentStudents():
    if request.method == "GET":
        return(render_template('currentstudents.html'))


@app.route('/calendar/', methods=["GET", "POST"])
def renderCalendar():
    if request.method == "GET":
        form = printUpcomingDates()
        return(render_template('calendar_page.html', form = form))


@app.route('/scheduleOrientation/', methods=["GET", "POST"])
def renderSchedule():
    if request.method == "GET":
        form = ScheduleOrientation()
        return(render_template('scheduleOrientation.html', form = form))
    elif request.method == "POST":
        orientation = request.form['orientation']
        file = open("orientationDate.txt", "w")
        file.write(orientation)

        url = "http://0.0.0.0:8080/scheduleOrientation/"
        headers = {
            'content-type': 'application/json',
            'x-api-token': 'jria'
        }

        payload = {
                'orientation': orientation
        }

        requests.post(url, headers=headers, data=json.dumps(payload))

        return(redirect("http://127.0.0.1:5000/currentstudents/"))


@app.route('/grades/', methods=["GET"])
def renderGrades():
    if request.method == "GET":
        return(render_template('grades.html'))

@app.route('/resources/', methods=['GET','POST'])
def renderResources():
        return(render_template('resources.html'))

@app.route('/editprofile/', methods=["GET"])
def renderEditProfile():
    if request.method == "GET":
        return(render_template('editprofile.html'))

@app.route('/accountcreation/', methods=['GET', 'POST'])
def renderAccountCreation():
    if request.method == "GET":
        form = AccountCreationForm()
        return (render_template('accountcreation.html', form = form))

    elif request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password']

        url = "http://0.0.0.0:8080/accountcreation/"

        # Yes, the x-api-token is weird. No, I don't know why I picked it.
        headers = {
            'content-type': 'application/json',
            'x-api-token': 'jria'
        }

        payload = {
                'username': username,
                'password': password
        }

        requests.post(url, headers=headers, data=json.dumps(payload))

        cached_username = username

        return(redirect("http://127.0.0.1:5000/demographics/"))

@app.route('/login/', methods=['GET', 'POST'])
def renderLogin():
    if request.method == "GET":
        form = AccountCreationForm()
        return (render_template('login.html', form = form))

    elif request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password']

        url = "http://0.0.0.0:8080/login/"

        # Yes, the x-api-token is weird. No, I don't know why I picked it.
        headers = {
            'content-type': 'application/json',
            'x-api-token': 'jria'
        }

        payload = {
                'username': username,
                'password': password
        }

        response = requests.get(url, headers=headers, data=json.dumps(payload)).json()

        try:
            if response['exists']:
                return(redirect("http://127.0.0.1:5000/currentstudents/"))
            else:
                return(redirect("http://127.0.0.1:5000/loginfail/"))
        except:
                return(redirect("http://127.0.0.1:5000/loginfail/"))


@app.route('/loginfail/', methods=['GET', 'POST'])
def renderLoginFail():
    if request.method == "GET":
        form = AccountCreationForm()
        return (render_template('failedlogin.html', form = form))

    elif request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password']

        # Yes, the x-api-token is weird. No, I don't know why I picked it.
        headers = {
            'content-type': 'application/json',
            'x-api-token': 'jria'
        }

        url = "http://0.0.0.0:8080/login/"
        payload = {
                'username': username,
                'password': password
        }

        response = requests.get(url, headers=headers, data=json.dumps(payload)).json()

        try:
            if response['exists']:
                return(redirect("http://127.0.0.1:5000/currentstudents/"))
            else:
                return(redirect("http://127.0.0.1:5000/loginfail/"))
        except:
                return(redirect("http://127.0.0.1:5000/loginfail/"))


@app.route('/demographics/', methods=["GET", "POST"])
def renderDemographicForm():
    if request.method == "GET":
        form = DemographicForm()
        return(render_template('demographic.html', form = form))

    elif request.method == "POST":
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['date_of_birth']
        marital_status = request.form['marital_status']
        spanish_origin = request.form['spanish_origin']
        country_of_origin = request.form['country_of_origin']
        racial_group = request.form['racial_group']

        english_second_lang = request.form['english_second_lang']
        native_lang = request.form['native_lang']

        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        home_phone = request.form['home_phone']
        cell_phone = request.form['cell_phone']
        emergency_contact_name = request.form['emergency_contact_name']
        emergency_contact_num = request.form['emergency_contact_num']
        emergency_contact_relation = request.form['emergency_contact_relation']

        max_grade_completed = request.form['max_grade_completed']
        school_type = request.form['school_type']
        date_last_enrolled = request.form['date_last_enrolled']
        num_school_years_completed = request.form['num_school_years_completed']

        occupation = request.form['occupation']
        employer_name = request.form['employer_name']
        employer_address = request.form['employer_address']
        employment_status = request.form['employment_status']

        hours_per_week = request.form['hours_per_week']
        work_phone = request.form['work_phone']

        num_dependents_minor = request.form['num_dependents_minor']
        num_dependents_other = request.form['num_dependents_other']
        yearly_income = request.form['yearly_income']
        public_assistance = request.form['public_assistance']
        public_assistance_number = request.form['public_assistance_number']
        disability = request.form['disability']

        living_area = request.form['living_area']
        how_hear_about = request.form['how_hear_about']
        add_student_info = request.form['add_student_info']
        add_student_info2 = request.form['add_student_info2']

        children = request.form['children']
        num_children = request.form['num_children']
        age_children = request.form['age_children']
        school_type = request.form['school_type']
        take_care_of_kids = request.form['take_care_of_kids']
        immigration_status = request.form['immigration_status']
        government_aid = request.form['government_aid']

        checking_acc = request.form['checking_acc']
        savings_acc = request.form['savings_acc']
        library_card = request.form['library_card']

        english_classes = request.form['english_classes']
        english_class_details = request.form['english_class_details']

        work = request.form['work']
        work_benefits = request.form['work_benefits']

        house_or_rent = request.form['house_or_rent']

        smartphone = request.form['smartphone']
        tablet = request.form['tablet']
        computer = request.form['computers']
        internet = request.form['internet']
        internet_access = request.form['internet_access']
        internet_access_elsewhere = request.form['internet_access_elsewhere']

        why_learn_english = request.form['why_learn_english']


        url = "http://0.0.0.0:8080/demographics/"

        # Yes, the x-api-token is weird. No, I don't know why I picked it.
        headers = {
            'content-type': 'application/json',
            'x-api-token': 'jria'
        }

        payload = {
                'username':username,'first_name':first_name,'last_name':last_name,
                'middle_name':middle_name,'date_of_birth':date_of_birth,
                'gender':gender,'marital_status':marital_status,'spanish_origin':spanish_origin,
                'country_of_origin':country_of_origin,'racial_group':racial_group,
                'english_second_lang':english_second_lang,'native_lang':native_lang,
                'address':address,'city':city,'state':state,'zip_code':zip_code,
                'home_phone':home_phone,'cell_phone':cell_phone,'emergency_contact_name':emergency_contact_name,
                'emergency_contact_num':emergency_contact_num,'emergency_contact_relation':emergency_contact_relation,
                'max_grade_completed':max_grade_completed,'school_type':school_type,
                'date_last_enrolled':date_last_enrolled,'num_school_years_completed':num_school_years_completed,
                'occupation':occupation,'employer_name':employer_name,
                'employer_address':employer_address,'employment_status':employment_status,
                'hours_per_week':hours_per_week,'work_phone':work_phone,
                'num_dependents_minor':work_phone,'num_dependents_other':num_dependents_other,
                'yearly_income':yearly_income,'public_assistance':public_assistance,
                'public_assistance_number':public_assistance_number,'disability':disability,
                'living_area':living_area,'how_hear_about':how_hear_about,
                'add_student_info':add_student_info,'add_student_info2':add_student_info2,
                'children':children,'num_children':num_children,'age_children':age_children,
                'school_type':school_type,'take_care_of_kids':take_care_of_kids,
                'immigration_status':immigration_status,'government_aid':government_aid,
                'checking_acc':checking_acc,'savings_acc':savings_acc,'library_card':library_card,
                'english_classes':english_classes,'english_class_details':english_class_details,
                'work':work,'work_benefits':work_benefits,'house_or_rent':house_or_rent,
                'smartphone':smartphone,'tablet':tablet,'computer':computer,internet:'internet',
                'internet_access':internet_access,'internet_access_elsewhere':internet_access_elsewhere,
                why_learn_english:'why_learn_english'
        }

        requests.post(url, headers=headers, data=json.dumps(payload))

        return(redirect("http://127.0.0.1:5000/careerinterests/"))

@app.route('/careerinterests/', methods=["GET", "POST"])
def renderCareerInterest():
    if request.method == "GET":
        form = CareerInterest()
        return(render_template('careerinterest.html', form = form))


@app.route('/test/', methods=["GET", "POST"])
def renderTestForm():
    if request.method == "GET":
        form = PlacementTest()
        return(render_template('test.html', form = form))


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/home'
    app.run()

 # Pizarron
