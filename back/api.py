from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
from pathlib import Path
import hashlib
import pandas as pd
from score import score


app = Flask(__name__)

dataFolder = Path.cwd() / 'data' / 'data.csv'
solutionsFolder = Path.cwd() / 'data' / 'solutions.csv'


@app.route('/accountcreation/', methods=['POST'])
def accountCreation():
    if request.method == 'POST':

        data = request.get_json()

        if data is None:
            return json.dumps({error: "Error"})

        if request.headers.get('x-api-token') == 'jria':

            email = data['username']
            password = data['password']

            df = pd.read_csv(str(dataFolder))

            user = df.loc[df["username"] == email]

            h = hashlib.md5(password.encode())

            # If the user doesn't exist yet, put them in!
            if user.empty:

                df = df.append({'username' : email , 'password' : h.hexdigest()} , ignore_index=True)

                df.to_csv(str(dataFolder), index=False)

                return jsonify(exists= "True")

            else:
                return jsonify(exists= "True")

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':

        data = request.get_json()

        if data is None:
            return jsonify(error= "Error")

        if request.headers.get('x-api-token') == 'jria':

            email = data['username']
            password = data['password']

            df = pd.read_csv(str(dataFolder))

            user = df.loc[df["username"] == email]

            # If the user exists
            if not user.empty:
                h = hashlib.md5(password.encode())
                i = df[df["username"] == email].index.values.astype(int)[0]
                if h.hexdigest() == df.at[i, 'password']:
                    first_name = df.at[i, "first_name"]
                    last_name = df.at[i, "last_name"]
                    exists = True
                    return jsonify(first_name = first_name, last_name=last_name, exists=exists)
                else:
                    return jsonify(exists = False)

            else:
                return jsonify(exists = False)


@app.route('/demographics/', methods=['POST'])
def demographics():
    if request.method == 'POST':
        data = request.get_json()

        if data is None:
            return json.dumps({error: "Error"})

        if request.headers.get('x-api-token') == 'jria':
            first_name = data['first_name']
            last_name = data['last_name']
            middle_name = data['middle_name']
            date_of_birth = data['date_of_birth']
            gender = data['date_of_birth']
            marital_status = data['marital_status']
            spanish_origin = data['spanish_origin']
            country_of_origin = data['country_of_origin']
            racial_group = data['racial_group']

            english_second_lang = data['english_second_lang']
            native_lang = data['native_lang']

            address = data['address']
            city = data['city']
            state = data['state']
            zip_code = data['zip_code']
            home_phone = data['home_phone']
            cell_phone = data['cell_phone']
            emergency_contact_name = data['emergency_contact_name']
            emergency_contact_num = data['emergency_contact_num']
            emergency_contact_relation = data['emergency_contact_relation']

            max_grade_completed = data['max_grade_completed']
            school_type = data['school_type']
            date_last_enrolled = data['date_last_enrolled']
            num_school_years_completed = data['num_school_years_completed']

            occupation = data['occupation']
            employer_name = data['employer_name']
            employer_address = data['employer_address']
            employment_status = data['employment_status']

            hours_per_week = data['hours_per_week']
            work_phone = data['work_phone']

            num_dependents_minor = data['num_dependents_minor']
            num_dependents_other = data['num_dependents_other']
            yearly_income = data['yearly_income']
            public_assistance = data['public_assistance']
            public_assistance_number = data['public_assistance_number']
            disability = data['disability']

            living_area = data['living_area']
            how_hear_about = data['how_hear_about']
            add_student_info = data['add_student_info']
            add_student_info2 = data['add_student_info2']

            children = data['children']
            num_children = data['num_children']
            age_children = data['age_children']
            school_type = data['school_type']
            take_care_of_kids = data['take_care_of_kids']
            immigration_status = data['immigration_status']
            government_aid = data['government_aid']

            checking_acc = data['checking_acc']
            savings_acc = data['savings_acc']
            library_card = data['library_card']

            english_classes = data['english_classes']
            english_class_details = data['english_class_details']

            work = data['work']
            work_benefits = data['work_benefits']

            house_or_rent = data['house_or_rent']

            smartphone = data['smartphone']
            tablet = data['tablet']
            computer = data['computers']
            internet = data['internet']
            internet_access = data['internet_access']
            internet_access_elsewhere = data['internet_access_elsewhere']

            why_learn_english = data['why_learn_english']


            df = pd.read_csv(str(dataFolder))
            i = df[data["username"] == df["username"]].index.values.astype(int)[0]


            if i is not None:
                df.at[i, 'first_name'] = first_name
                df.at[i, 'last_name'] = last_name
                df.at[i, 'middle_name'] = middle_name
                df.at[i, 'date_of_birth'] = date_of_birth
                df.at[i, 'date_of_birth'] = gender
                df.at[i, 'marital_status'] = marital_statuss
                df.at[i, 'spanish_origin'] = spanish_origin
                df.at[i, 'country_of_origin'] = country_of_origin
                df.at[i, 'racial_group'] = racial_group

                df.at[i, 'english_second_lang'] = english_second_lang
                df.at[i, 'native_lang'] = native_lang

                df.at[i, 'address'] = address
                df.at[i, 'city'] = city
                df.at[i, 'state'] = state
                df.at[i, 'zip_code'] = zip_code
                df.at[i, 'home_phone'] = home_phone
                df.at[i, 'cell_phone'] = cell_phone
                df.at[i, 'emergency_contact_name'] = emergency_contact_name
                df.at[i, 'emergency_contact_num'] = emergency_contact_num
                df.at[i, 'emergency_contact_relation'] = emergency_contact_relation

                df.at[i, 'max_grade_completed'] = max_grade_completed
                df.at[i, 'school_type'] = school_type
                df.at[i, 'date_last_enrolled'] = date_last_enrolled
                df.at[i, 'num_school_years_completed'] = num_school_years_completed

                df.at[i, 'occupation'] = occupation
                df.at[i, 'employer_name'] = employer_name
                df.at[i, 'employer_address'] = employer_address
                df.at[i, 'employment_status'] = employment_status

                df.at[i, 'hours_per_week'] = hours_per_week
                df.at[i, 'work_phone'] = work_phone

                df.at[i, 'num_dependents_minor'] = num_dependents_minor
                df.at[i, 'num_dependents_other'] = num_dependents_other
                df.at[i, 'yearly_income'] = yearly_income
                df.at[i, 'public_assistance'] = public_assistance
                df.at[i, 'public_assistance_number'] = public_assistance_number
                df.at[i, 'disability'] = disability

                df.at[i, 'living_area'] = living_area
                df.at[i, 'how_hear_about'] = how_hear_about
                df.at[i, 'add_student_info'] = add_student_info
                df.at[i, 'add_student_info2'] = add_student_info2

                df.at[i, 'children'] = children
                df.at[i, 'num_children'] = num_children
                df.at[i, 'age_children'] = age_children
                df.at[i, 'school_type'] = school_type
                df.at[i, 'take_care_of_kids'] = take_care_of_kids
                df.at[i, 'immigration_status'] = immigration_status
                df.at[i, 'government_aid'] = government_aid

                df.at[i, 'checking_acc'] = checking_acc
                df.at[i, 'savings_acc'] = savings_acc
                df.at[i, 'library_card'] = library_card

                df.at[i, 'english_classes'] = english_classes
                df.at[i, 'english_class_details'] = english_class_details

                df.at[i, 'work'] = work
                df.at[i, 'work_benefits'] = work_benefits

                df.at[i, 'house_or_rent'] = house_or_rent

                df.at[i, 'smartphone'] = smartphone
                df.at[i, 'tablet'] = tablet
                df.at[i, 'computers'] = computer
                df.at[i, 'internet'] = internet
                df.at[i, 'internet_access'] = internet_access
                df.at[i, 'internet_access_elsewhere'] = internet_access_elsewhere

                df.at[i, 'why_learn_english'] = why_learn_english

                df.to_csv(str(dataFolder), index=False)

                return "200 - OK"

            else:
                return '405 - Method Not Allowed'

@app.route('/test/', methods=['POST'])
def test_solution():
    if request.method == 'POST':
        data = request.get_json()

    if data is None:
        return json.dumps({error: "Error"})

    if request.headers.get('x-api-token') == 'jria':
        question_1 = data['question_1']
        question_2 = data['question_2']
        question_3 = data['question_3']
        question_4 = data['question_4']
        question_5 = data['question_5']
        question_6 = data['question_6']
        question_7 = data['question_7']
        question_8 = data['question_8']
        question_9 = data['question_9']
        question_10 = data['question_10']
        question_11 = data['question_11']
        question_12 = data['question_12']
        question_13 = data['question_13']
        question_missed = data['question_missed']
        question_14 = data['question_14']
        question_15 = data['question_15']
        question_16 = data['question_16']
        question_17 = data['question_17']
        question_18 = data['question_18']
        question_19 = data['question_19']
        question_20 = data['question_20']
        question_21 = data['question_21']
        question_22 = data['question_22']
        question_23 = data['question_23']
        question_24 = data['question_24']
        question_25 = data['question_25']
        question_26 = data['question_26']
        question_27 = data['question_27']
        question_28 = data['question_28']
        question_29 = data['question_29']
        question_30 = data['question_30']
        question_31 = data['question_31']
        question_32 = data['question_32']
        question_33 = data['question_33']
        question_34 = data['question_34']
        question_35 = data['question_35']
        question_36 = data['question_36']
        question_37 = data['question_37']
        question_38 = data['question_38']
        question_39 = data['question_39']

        i = df.index[data["username"] == df["username"]]
        df = pd.read_csv(str(dataFolder))

    if i is not None:
        df.at[i, 'question_1'] = question_1
        df.at[i, 'question_2'] = question_2
        df.at[i, 'question_3'] = question_3
        df.at[i, 'question_4'] = question_4
        df.at[i, 'question_5'] = question_5
        df.at[i, 'question_6'] = question_6
        df.at[i, 'question_7'] = question_7
        df.at[i, 'question_8'] = question_8
        df.at[i, 'question_9'] = question_9
        df.at[i, 'question_10'] = question_10
        df.at[i, 'question_11'] = question_11
        df.at[i, 'question_12'] = question_12
        df.at[i, 'question_13'] = question_13
        df.at[i, 'question_missing'] = question_missing
        df.at[i, 'question_14'] = question_14
        df.at[i, 'question_15'] = question_15
        df.at[i, 'question_16'] = question_16
        df.at[i, 'question_17'] = question_17
        df.at[i, 'question_18'] = question_18
        df.at[i, 'question_19'] = question_19
        df.at[i, 'question_20'] = question_20
        df.at[i, 'question_21'] = question_21
        df.at[i, 'question_22'] = question_22
        df.at[i, 'question_23'] = question_23
        df.at[i, 'question_24'] = question_24
        df.at[i, 'question_25'] = question_25
        df.at[i, 'question_26'] = question_26
        df.at[i, 'question_27'] = question_27
        df.at[i, 'question_28'] = question_28
        df.at[i, 'question_29'] = question_29
        df.at[i, 'question_30'] = question_30
        df.at[i, 'question_31'] = question_31
        df.at[i, 'question_32'] = question_32
        df.at[i, 'question_33'] = question_33
        df.at[i, 'question_34'] = question_34
        df.at[i, 'question_35'] = question_35
        df.at[i, 'question_36'] = question_36
        df.at[i, 'question_37'] = question_37
        df.at[i, 'question_38'] = question_38
        df.at[i, 'question_39'] = question_39

        df.to_csv(str(dataFolder), index=False)

        score(df, df['username'])

        return "200 - OK"
    else:
        return '405 - Method Not Allowed'

@app.route('/careerinterests/', methods=['POST'])
def careerInterests():
    if request.method == 'POST':

        data = request.get_json()

        if data is None:
            return json.dumps({error: "Error"})

        if request.headers.get('x-api-token') == 'jria':

            career_interest = data['career_interest']

            # If the user doesn't exist yet, put them in!
            df = pd.read_csv(str(dataFolder))
            i = df[data["username"] == df["username"]].index.values.astype(int)[0]

            if i is not None:
                df.at[i, 'career_interest'] = career_interest

                df.to_csv(str(dataFolder), index=False)

                return "200 - OK"

            else:
                return '405 - Method Not Allowed'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
