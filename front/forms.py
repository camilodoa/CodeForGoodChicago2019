import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, BooleanField, SelectField, SelectMultipleField, validators
from wtforms.validators import DataRequired, Email, Length, input_required, optional
class AccountCreationForm(FlaskForm):
    '''
    Flask form used to create an account
    '''
    username = StringField('Email Address', validators=[validators.input_required(), Email()])
    password = StringField('Password', validators=[validators.input_required(), Length(min = 6, message = "Password should be at least 6 characters.")])
    submit = SubmitField('Submit')

class DemographicForm(FlaskForm):

    username = StringField('Email Address', validators=[validators.input_required(), Email()])
    first_name = StringField(u'First Name:', validators=[input_required()])
    last_name  = StringField(u'Last Name:', validators=[input_required()])
    middle_name  = StringField(u'Middle Name:', validators=[optional()])
    date_of_birth = StringField(u'Date of Birth:', validators=[input_required()])
    gender = SelectField(u'Gender', choices=[('Female', 'Female'), ('Male', 'Male')]) #gender
    marital_status = SelectField(u'Marital Status:', choices=[('Single', 'Single'),
    ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow')])
    spanish_origin = BooleanField();  #Are you hispanic or latino?
    country_of_origin = StringField(u'Country of origin:', validators=[optional()])
    racial_group = SelectField(u'Are you from one or more of the following racial groups?',
    choices=[('American Indian or Alaska Native', 'American Indian or Alaska Native'),
    ('Asian', 'Asian'), ('Black or African American', 'Black or African American'),
    ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander'),
    ('White', 'White')])

    english_second_lang = BooleanField()
    native_lang = StringField(u'If yes, record native language', validators=[validators.optional()])

    #contact info
    email = StringField('Email Address', validators=[validators.input_required(), Email()])
    address = StringField('Address', validators=[validators.input_required()])
    city = StringField('City', validators=[validators.input_required()])
    state = StringField('State', validators=[validators.input_required()])
    zip_code = StringField('Zip Code', validators=[validators.input_required()])
    home_phone = StringField('Home Phone', validators=[validators.optional()])
    cell_phone = StringField('Cell Phone', validators=[validators.optional()])
    emergency_contact_name = StringField('Emergency contact name', validators=[validators.input_required()])
    emergency_contact_num = StringField('Emergency contact phone number', validators=[validators.input_required()])
    emergency_contact_relation = StringField('Emergency contact relationship', validators=[validators.input_required()])

    #education
    max_grade_completed = StringField('Maximum grade of education completed', validators=[validators.input_required()])
    school_type = SelectField(u'Schooling Type', choices=[('US-based school', 'US-based school'), ('non-US based school', 'non-US based school')])
    date_last_enrolled = StringField('Month/Year when last enrolled', validators=[validators.input_required()])
    num_school_years_completed = SelectField(u'Number of school years completed',
    choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3'),
    ('Grade 4', 'Grade 4'), ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6'), ('Grade 7', 'Grade 7'),
    ('Grade 8', 'Grade 8'), ('Grade 9', 'Grade 9'), ('Grade 10', 'Grade 10'), ('Grade 11', 'Grade 11'),
    ('Grade 12', 'Grade 12'), ('High School Diploma', 'High School Diploma'), ('GED', 'GED'),
    ('Some college', 'Some college'), ('College Degree', 'College Degreee')])

    #employment
    occupation = StringField('If employed, what is your occupation?', validators=[validators.optional()])
    employer_name = StringField('Employer name', validators=[validators.optional()])
    employer_address = StringField('Employer address', validators=[validators.optional()])
    employment_status = SelectField('Employment status', choices=[('Not in labor force', 'Not in labor force'),
    ('Employed part-time', 'Employed part-time'), ('Unemployed', 'Unemployed'), ('Employed full time', 'Employed full time')])

    hours_per_week = StringField('If Employed, hours per week', validators=[validators.optional()])
    work_phone = StringField('Work Phone#', validators=[validators.optional()])

    #Student status
    num_dependents_minor = StringField('Number of Dependents-minor children', validators=[validators.optional()])
    num_dependents_other = StringField('Number of Dependents-other', validators=[validators.optional()])
    yearly_income = StringField('Yearly household income', validators=[validators.input_required()])
    public_assistance = BooleanField() #do you recieve public assistance?
    public_assistance_number = StringField('If yes, public assistance number', validators=[validators.optional()])
    disability = SelectField(u'Do you have a disability?', choices=[('Not Disabled','Not Disabled'), ('Physical Impairment', 'Physical Impairment'),('Mental Impairment', 'Mental Impairment'), ('Learning Impairment', 'Learning Impairment'), ('Multiple disabilities', 'Multiple disabilities')])

    living_area = SelectField(u'What area do you live in?', choices=[('Rural Area', 'Rural Area'), ('Urban Area', 'Urban Area (with high unemployment)'), ('Neither', 'Neither')])
    how_hear_about = SelectField(u'How did you hear about us?', choices=[('Friend or Relative', 'Friend or Relative'), ('TV, radio, newspaper', 'TV, radio, newspaper'), ('Flyer', 'Flyer'), ('Other', 'Other')])
    add_student_info = SelectMultipleField(u'Additional Student information', choices=[('Low income', 'Low income'), ('Displaced Homemaker', 'Displaced Homemaker'), ('Single Parent', 'Single Parent'), ('Dislocated worker', 'Dislocated worker'), ('Veteran', 'Veteran')])
    add_student_info2 = SelectMultipleField(u'Please check all that apply', choices=[('Participant in a work based learner project', 'Participant in a work based learner project'), ('Participant in a Family Literacy Program', 'Participant in a Family Literacy Program'),
    ('Participant in a WorkPlace Literacy program', 'Participant in a WorkPlace Literacy program'), ('Participant in a Volunteer Literacy program','Participant in a Volunteer Literacy program'), ('In Program for the homeless', 'In Program for the homeless'),
    ('In a correctional facility', 'In a correctional facility'), ('In a community correctional program', 'In a community correctional program'), ('In other institutional setting', 'In other institutional setting')])

    children = BooleanField() #Do you have children?
    num_children = StringField(u'How many children do you have?', validators=[validators.optional()])
    age_children = StringField(u'How old are they?', validators=[validators.optional()])
    school_type = SelectField(u'What type of school do they attend?', choices=[('Public', 'Public'), ('Private', 'Private'), ('Charter', 'Charter'), ('None', 'None')])
    take_care_of_kids = BooleanField() #Do you take good care of your kids?
    immigration_status = SelectField(u'Immigration status', choices=[('Citizen', 'Citizen'), ('Resident', 'Resident'), ('Visitor', 'Visitor'), ('None', 'None')])
    government_aid = SelectMultipleField(u'If you recieve aid from the government, which ones are they?', choices=[('TANF', 'TANF'), ('Tax Credit', 'Tax Credit'), ('SNAP/Link', 'SNAP/Link'), ('WIC', 'WIC'), ('Medical Card', 'Medical Card'), ('Medicare', 'Medicare'), ('others', 'others')])

    checking_acc = BooleanField() #Do you have a checkign account?
    savings_acc = BooleanField() #Do you have a savings account?
    library_card = BooleanField() #Do you have a library card?

    english_classes = BooleanField() #Have you taken english language classes?
    english_class_details = StringField(u'Where and what year?', validators=[validators.optional()])

    work = StringField(u'If you work, what is your job?', validators=[validators.optional()])
    work_benefits = SelectMultipleField(u'If you work, whar benefits do you recieve?', choices=[('Medical Insurance', 'Medical Insurance'), ('Vacations/Holidays/Sickeness/Maternity/Personal', 'Vacations/Holidays/Sickeness/Maternity/Personal'), ('Flexiible hours', 'Flexible hours'), ('Retirement plan', 'Retirement plan'), ('Other', 'Other')])

    house_or_rent = BooleanField() #Do you own a house or pay rent?

    smartphone = BooleanField() #Do you have a smartphone
    tablet = BooleanField() #Do you have a tablet
    computer = BooleanField() #Do you have a computer
    internet = BooleanField() #Have you ever used the internet?
    internet_access = BooleanField() #Do you have internet access at home?
    internet_access_elsewhere = BooleanField() #Do you have internet access elsewhere?

    why_learn_english = SelectMultipleField('Why do you want to learn english?', choices=[('GED', 'GED'), ('Job', 'Job'), ('Citizenship', 'Citizenship'), ('To get an education', 'To get an education'), ('Move forward at work', 'Move forward at work'), ('Help kids at school', 'Help kids at school')])
    submit = SubmitField('Submit')

class CareerInterest(FlaskForm):
    career_interest = SelectField('Select one field that is a career cluster you are interested in pursuing', choices= [
    ('Agriculture Food & Natural Resources', 'Agriculture Food & Natural Resources'),
    ('Architecture & Construction', 'Architecture & Construction'),
    ('Arts, A/V Technology & Communication', 'Arts, A/V Technology & Communication'),
    ('Business Management & Administration', 'Business Management & Administration'),
    ('Education & Training', 'Education & Training'),
    ('Finance', 'Finance'),
    ('Government & Public Administration', 'Government & Public Administration'),
    ('Health Sciences', 'Health Sciences'),
    ('Hospitality and Tourism', 'Hospitality & Tourism'),
    ('Human Services', 'Human Services'),
    ('Information Technology', 'Information Technology'),
    ('Law, Public Safety, Corrections & Security', 'Law, Public Safety, Corrections & Security'),
    ('Manufacturing', 'Manufacturing'),
    ('Marketing', 'Marketing'),
    ('Science, Technology, Engineering & Mathematics', 'Science, Technology, Engineering & Mathematics'),
    ('Transportation, Distribution & Logistics','Transportation, Distribution & Logistics')
    ])
    start_date_fall = datetime.datetime(2019, 8, 26)
    start_date_spring = datetime.datetime(2020, 1, 1)
    start_date_summer = datetime.datetime(2020, 5, 10)

    today = datetime.datetime.now()

    possible_dates = []
    while (today <= start_date_fall + datetime.timedelta(days=70)):
        possible_dates.append((str(today), str(today)))
        today += datetime.timedelta(days = 1)
    orientation = SelectMultipleField('Select the dates you are available for orientation', choices=possible_dates)
    submit = SubmitField('Submit')

class PlacementTest(FlaskForm):
    question_1 = SelectField("What's the mother's name?", choices=[('a', 'His name is Pilar.'), ('b', 'Her name is Pilar.'), ('c', 'Their name is Pilar.'), ('d', 'Your name is Pilar.')])
    question_2 = SelectField("There are three ___ on the table.", choices=[('a', 'cup'), ('b', 'cups'), ('c', 'cake'), ('d', 'plate')])
    question_3 = SelectField("Is Ramona happy?", choices=[('a', 'Yes, she is.'), ('b', 'Yes, we are.'), ('c', 'Yes, he is.'), ('d.', 'Yes, they are.')])
    question_4 = SelectField("Carmina's Restaurant is open ___.", choices=[('a', 'on Sunday'), ('b', 'on Tuesday'), ('c', 'on Saturday'), ('d', 'on Monday')])
    question_5 = SelectField("How many people work at the day-care center?", choices = [('a', 'three'), ('b', 'four'), ('c', 'five'), ('d', 'six')])
    question_6 = SelectField("Who works until 8:00 p.m. on Tuesday and Thursday?", choices = [('a', 'Dan'), ('b', 'Juan'), ('c', 'Megan'), ('d', 'Sally')])
    question_7 = SelectField("The post office is ___ the parking lot.", choices = [('a', 'on'), ('b', 'across from'), ('c', 'on the corner of'), ('d', 'next to')])
    question_8 = SelectField("What are Katia and Sara doing? They ____", choices = [('a', 'talking'), ('b', 'are talking'), ('c', 'is talking'), ('d', 'talk')])
    question_9 = SelectField("Does Lee ___ a fever?", choices= [('a', 'had'), ('b', 'has'), ('c', 'have'), ('d', 'having')])
    question_10 = SelectField("When do you eat lunch? ___ 12:30", choices = [('a', 'In'), ('b', 'On'), ('c', 'At'), ('d', 'From')])
    question_11 = SelectField("How many ___ do we have? Three.", choices = [('a', 'tea'), ('b', 'onions'), ('c', 'milk'), ('d', 'bread')])
    question_12 = SelectField("Yolanda is a teacher now. She ___ a teacher's assistant before.", choices = [('a', 'is'), ('b', 'are'), ('c', 'was'), ('d', 'were')])
    question_13 = SelectField("Yesterday, Dan ____ groceries after work.", choices=[('a', 'bought'), ('b', 'buying'), ('c', 'buy'), ('d', 'buys')])
    question_missed = SelectField("What will you learn in Ms. Cuevas's class?", choices =[('a', 'math'),('b', 'TV repair'), ('c', 'computer repair'), ('d', 'American history')])
    question_14 = SelectField("Which course meets on Mondays and Tuesdays?", choices=[('a', 'GED'), ('b', 'TV and DVD repair'), ('c', 'Introduction to Computers'), ('d', 'Citizenship')])
    question_15 = SelectField("What did Joe buy Sylvia? He bought ___ a cake.", choices=[('a', 'to her'), ('b', 'them'), ('c', 'she'), ('d', 'her')])
    question_16 = SelectField("Leon has a test tomorrow. He ___ study tonight.", choices = [('a', 'is'), ('b', 'does'), ('c', 'will'), ('d', 'are')])
    question_17 = SelectField("When do Mr. and Mrs. Yamada usually eat dinner? They usually ___ at 7 p.m.", choices = [('a', 'eat'), ('b', 'eats'), ('c', 'ate'), ('d', 'eating')])
    question_18 = SelectField("Marcia's back is hurting. She ___ to see a doctor.", choices = [('a', 'have'), ('b', 'has'), ('c', 'having'), ('d', 'had')])
    question_19 = SelectField("How long does it take to drive to Philadelphia? It takes ____.", choices = [('a', 'every day'), ('b', 'often'), ('c', 'about two hours'), ('d', 'twice a month')])
    question_20 = SelectField("The white refrigerator is large. But the gray refrigerator is ____.", choices= [('la', 'larger than'), ('b', 'smaller'), ('c', 'larger'), ('d', 'large')])
    question_21 = SelectField("Ravi cleaned his room, ___ he didn't make his bed.", choices = [('a', 'or'), ('b', 'but'), ('c', 'and'), ('d', 'now')])
    question_22 = SelectField("Keiko's father used to ___.", choices = [('a', 'take naps every afternoon'), ('b', 'eat too much sugar and salt'), ('c', 'get sick a lot'), ('d', 'do volunteer work')])
    question_23 = SelectField("Recently, Keiko's father has ___.", choices = [('a', 'slept well'), ('b', 'lost weight'), ('c', 'had a lot of energy'), ('d', 'seen his doctor')])
    question_24 = SelectField("Connie likes going out as ____ staying home.", choices = [('a', 'much'), ('b', 'much as'), ('c', 'more than'), ('d', 'less than')])
    question_25 = SelectField("David ____ well lately.", choices = [('a', 'have slept'), ('b', "haven't slept"), ('c', "hasn't slept"), ('d', 'sleeps')])
    question_26 = SelectField("Arturo intents ____ history in college.", choices = [('a', 'to study'), ('b', 'studying'), ('c', 'studies'), ('d', 'will study')])
    question_27 = SelectField("Michael always turns off his computer ___ the office.", choices = [('a', 'before he leaves'), ('b', 'he leaves'), ('c', 'after he left'), ('d', 'when he left')])
    question_28 = SelectField("I'm tired of ___ TV. Let's go out.", choices = [('a', 'watching'), ('b', 'watches'), ('c', 'to watch'), ('d', 'watched')])
    question_29 = SelectField("Walter is practicing the piano. He ____ since 9:00.", choices = [('a', 'is practicing'), ('b', 'practiced'), ('c', 'practices'), ('d', 'has been practicing')])
    question_30 = SelectField("While we were driving to school, ____.", choices = [('a', 'it started to rain'), ('b', 'it starts to rain'), ('c', "it's raining"), ('d', 'it is rain')])
    question_31 = SelectField("The Pinheiros ____.", choices = [('a', 'coordinate all the volunteers at the food bank'), ('b', 'volunteer at the food bank'), ('c', 'donate groceries to the food bank'), ('d', 'are customers at the food bank')])
    question_32 = SelectField("The Pinheiros feel ____.", choices = [('a', 'closer to other people'), ('b', 'ungrateful for other people'), ('c', 'compassionate toward other people'), ('d', 'as lucky as other people')])
    question_33 = SelectField("Do you believe ____?", choices= [('a', 'will Helen be artisitic'), ('b', 'that Helen is artistic'), ('c', 'is Helen artistic'), ('d', 'that Helen is artistic')])
    question_34 = SelectField("She used to be a fast driver. Since her accident, she drives _____.", choices = [('a', 'careful'), ('b', 'more carefully'), ('c', 'more careful'), ('d', 'the most careful')])
    question_35 = SelectField("____ at your school?", choices = [('a', 'Is financial aid offered'), ('b', 'Financial aid is offered'), ('c', 'Financial aid offers'), ('d', 'Does financial aid offer')])
    question_36 = SelectField("A: My boyfriend took me out for dinner last night. B: Really? Tell me where ____.", choices = [('a', 'did you go'), ('b', 'you go'), ('c', 'you went'), ('d', 'you have gone')])
    question_37 = SelectField("Mary drives her daughter to school ____.", choices = [('a', 'every day last year'), ('b', 'four times a week'), ('c', 'when she was small'), ('d', 'twice so far')])
    question_38 = SelectField("Sona doesn't use her air conditioning often ____ it's too expensive.", choices = [('a', 'although'), ('b', 'even though'), ('c', 'because of'), ('d', 'because')])
    question_39 = SelectField("These days, nobody wants to buy a car ____ a lot of gas.", choices = [('a', 'that uses'),('b', "it doesn't use"), ('c', "that it doesn't use"), ('d', 'who uses')])
    submit = SubmitField('Submit')


class ScheduleOrientation(FlaskForm):
    start_date_fall = datetime.datetime(2019, 8, 26)
    start_date_spring = datetime.datetime(2020, 1, 1)
    start_date_summer = datetime.datetime(2020, 5, 10)
    today = datetime.datetime.now()
    possible_dates = []
    while (today <= start_date_fall + datetime.timedelta(days=70)):
        possible_dates.append((str(today), str(today)))
        today += datetime.timedelta(days = 1)
    orientation = SelectMultipleField('Select the dates you are available for orientation', choices=possible_dates) #to_display
    submit = SubmitField('submit')

class printUpcomingDates(FlaskForm):
    start_date_fall = datetime.datetime(2019, 8, 26)
    start_date_spring = datetime.datetime(2020, 1, 1)
    start_date_summer = datetime.datetime(2020, 5, 10)
    today = datetime.datetime.now()
    #print out upcoming class dates
    #can change const 7 ddepending if class is weekly, biweekly, daily, etc
    upcoming_class_dates = []
    class_date = start_date_fall

    while (class_date <= start_date_spring):
        if class_date > today:
            upcoming_class_dates.append(str(class_date))
        class_date += datetime.timedelta(days = 7)

    file = open("orientationDate.txt", "r")
    orientation = file.read()
    orientation_date = TextField('Upcoming orientation date: ' + orientation)
    output_classes = TextField('Upcoming classes are on dates: ' + str(upcoming_class_dates))
