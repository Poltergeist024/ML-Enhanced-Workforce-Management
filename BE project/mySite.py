from flask import Flask, render_template, redirect, url_for, request,session,Response, jsonify
from werkzeug import secure_filename
import sqlite3
import pandas as pd
from datetime import datetime
from supportFile import *
import matplotlib.pyplot as plt
from attrition import *


app = Flask(__name__)


app.secret_key = '1234'
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def landing():
	return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/home1', methods=['GET', 'POST'])
def home1():
	return render_template('home1.html')

@app.route('/eda', methods=['GET', 'POST'])
def eda():
	return render_template('eda.html')

def validate_email(email):
    import re
    email_pattern = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
    return email_pattern.match(email) is not None

def validate_age(age):
    return age.isdigit() and 18 <= int(age) <= 70

def validate_contact(num):
    return num.isdigit() and len(num) == 10

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        if request.form['sub'] == 'Submit':
            num = request.form['num']
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            age = request.form['age']
            gender = request.form['gender']

            if not validate_email(email):
                return render_template('input.html', error="Invalid email address.")
            if not validate_age(age):
                return render_template('input.html', error="Age must be an integer between 18 and 70.")
            if not validate_contact(num):
                return render_template('input.html', error="Contact number must be a 10-digit number.")

            users = {'Name': name, 'Email': email, 'Contact': num}
            df = pd.DataFrame(users, index=[0])
            df.to_csv('users.csv', mode='a', header=False)

            sec = {'num': num}
            df = pd.DataFrame(sec, index=[0])
            df.to_csv('secrets.csv')

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            con = sqlite3.connect('mydatabase.db')
            cursorObj = con.cursor()
            cursorObj.execute("CREATE TABLE IF NOT EXISTS Users (Date text, Name text, Contact text, Email text, Password text, Age text, Gender text)")
            cursorObj.execute("INSERT INTO Users VALUES(?,?,?,?,?,?,?)", (dt_string, name, num, email, password, age, gender))
            con.commit()

            return redirect(url_for('login'))

    return render_template('input.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	global name
	if request.method == 'POST':
		name = request.form['name']
		password = request.form['password']
		con = sqlite3.connect('mydatabase.db')
		cursorObj = con.cursor()
		cursorObj.execute(f"SELECT Name from Users WHERE Name='{name}' AND password = '{password}';")

	
		if(cursorObj.fetchone()):
			return redirect(url_for('home1'))
		else:
			error = "Invalid Credentials Please try again..!!!"
	return render_template('login.html',error=error)

@app.route('/performance', methods=['GET', 'POST'])
def performance():
	global name
	if request.method == 'POST':
		name = request.form['name']
		gender = request.form['gender']
		ed = int(request.form['ed'])
		ej = int(request.form['ej'])
		es = int(request.form['es'])
		sh = int(request.form['sh'])
		lb = int(request.form['lb'])
		ex = int(request.form['ex'])
		exr = int(request.form['exr'])
		yp = int(request.form['yp'])
		ym = int(request.form['ym'])
		test_sample = [[ed,ej,es,sh,lb,ex,exr,yp,ym]]
		test_sample = sc.transform(test_sample)
		pred = predictPerformance(test_sample)
		if(pred>=3):
			appraisal = 'Yes'
		else:
			appraisal = 'No'
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")	
		con = sqlite3.connect('mydatabase.db')
		cursorObj = con.cursor()
		cursorObj.execute("CREATE TABLE IF NOT EXISTS Performance (Date text,Name text,Rating text)")
		cursorObj.execute("INSERT INTO Performance VALUES(?,?,?)",(dt_string,name,str(pred)))
		con.commit()
		return render_template('performance.html',pred=pred,appraisal=appraisal)
	return render_template('performance.html')

@app.route('/attrition', methods=['GET', 'POST'])
def attrition():
	global idx
	if request.method == 'POST':
		idx = int(request.form['id'])
		age = int(request.form['age'])
		travel = int(request.form['travel'])
		distance = int(request.form['distance'])
		education = int(request.form['education'])
		gender = int(request.form['gender'])
		job = int(request.form['job'])
		joblevel = int(request.form['joblevel'])
		jobsatisfaction = int(request.form['jobsatisfaction'])
		marital = int(request.form['marital'])
		income = int(request.form['income'])
		companies = int(request.form['companies'])
		overtime = int(request.form['overtime'])
		hike = int(request.form['hike'])
		performance = int(request.form['performance'])
		relationship = int(request.form['relationship'])
		stock = int(request.form['stock'])
		experience = int(request.form['experience'])
		training = int(request.form['training'])
		life = int(request.form['life'])
		companyex = int(request.form['companyex'])
		roleex = int(request.form['roleex'])
		promotion = int(request.form['promotion'])
		manager = int(request.form['manager'])
		test_sample = [[age, travel, distance, education, gender, job, joblevel, jobsatisfaction, marital, income, companies, overtime, hike, performance, relationship, stock, experience, training, life, companyex, roleex, promotion, manager]]
		pred = predictAttrition(test_sample)
		if pred[0] == 0:
			pred = 'No'
		else:
			pred = 'Yes'
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")	
		con = sqlite3.connect('mydatabase.db')
		cursorObj = con.cursor()
		cursorObj.execute("CREATE TABLE IF NOT EXISTS Attrition (Date text, Rating text)")
		cursorObj.execute("INSERT INTO Attrition (Date, Rating) VALUES(?,?)", (dt_string, str(pred)))
		con.commit()
		return render_template('attrition.html', pred=pred)
	return render_template('attrition.html')


#edit

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(f"Received data: {data}") 

            required_keys = [
                'EmpID', 'Age', 'Gender', 'MaritalStatus', 'BusinessTravelFrequency', 
                'DistanceFromHome', 'EmpEducationLevel', 'EmpEnvironmentSatisfaction', 
                'EmpHourlyRate', 'EmpJobInvolvement', 'EmpJobLevel', 'EmpJobSatisfaction', 
                'NumCompaniesWorked', 'OverTime', 'EmpLastSalaryHikePercent', 
                'EmpRelationshipSatisfaction', 'TotalWorkExperienceInYears', 
                'TrainingTimesLastYear', 'EmpWorkLifeBalance', 'ExperienceYearsAtThisCompany', 
                'ExperienceYearsInCurrentRole', 'YearsWithCurrManager', 'Attrition', 
                'PerformanceRating', 'EmpDepartment'
            ]

            for key in required_keys:
                if key not in data:
                    raise KeyError(f"Missing required key: {key}")

            conn = sqlite3.connect('data.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS employee_data
                         (EmpID VARCHAR(10), 
                          Age INTEGER, 
                          Gender INTEGER, 
                          MaritalStatus INTEGER, 
                          BusinessTravelFrequency INTEGER, 
                          DistanceFromHome INTEGER, 
                          EmpEducationLevel INTEGER, 
                          EmpEnvironmentSatisfaction INTEGER, 
                          EmpHourlyRate INTEGER, 
                          EmpJobInvolvement INTEGER, 
                          EmpJobLevel INTEGER, 
                          EmpJobSatisfaction INTEGER, 
                          NumCompaniesWorked INTEGER, 
                          OverTime INTEGER, 
                          EmpLastSalaryHikePercent INTEGER, 
                          EmpRelationshipSatisfaction INTEGER, 
                          TotalWorkExperienceInYears INTEGER, 
                          TrainingTimesLastYear INTEGER, 
                          EmpWorkLifeBalance INTEGER, 
                          ExperienceYearsAtThisCompany INTEGER, 
                          ExperienceYearsInCurrentRole INTEGER, 
                          YearsWithCurrManager INTEGER, 
                          Attrition INTEGER, 
                          PerformanceRating INTEGER, 
                          EmpDepartment INTEGER)''')

            sql_query = '''
                INSERT INTO employee_data 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            
            values = [data[key] for key in required_keys]

            c.execute(sql_query, values)

            conn.commit()
            conn.close()


            return render_template('submit.html', message="Form submitted successfully!")
        except KeyError as e:
            print(f"KeyError: {e}")
            return render_template('submit.html', error=f"Missing required field: {e}"), 400
        except Exception as e:
            print(f"An error occurred: {e}")
            return render_template('submit.html', error=f"An error occurred: {e}"), 500
    else:
        print("GET request received at /submit")
        return render_template('submit.html', error="Invalid request method. Please use POST.")



@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
    search_result = None
    latest_rows = None
    error = None
    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        if request.method == 'POST':
            emp_id = request.form.get('emp_id')
            c.execute("SELECT * FROM employee_data WHERE EmpID = ?", (emp_id,))
            search_result = c.fetchone()

        c.execute("SELECT * FROM employee_data ORDER BY rowid DESC LIMIT 5")
        latest_rows = c.fetchall()
        
        column_names = [description[0] for description in c.description]

        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        error = f"An error occurred: {e}"

    return render_template('show_data.html', 
                           search_result=search_result, 
                           latest_rows=latest_rows, 
                           column_names=column_names,
                           error=error)




@app.route('/record', methods=['GET', 'POST'])
def record():
	global name
	conn = sqlite3.connect('mydatabase.db', isolation_level=None,
						detect_types=sqlite3.PARSE_COLNAMES)
	db_df = pd.read_sql_query(f"SELECT * from Performance", conn)
	df = db_df
	df['Rating'] = df['Rating'].apply(pd.to_numeric)
	db_df.plot(x="Name", y="Rating", kind="bar")
	plt.savefig('static/images/rating.jpg')
	plt.close()
	
	return render_template('record.html',tables=[db_df.to_html(classes='w3-table-all w3-hoverable w3-padding')], titles=db_df.columns.values)


@app.after_request
def add_header(response):
	# response.cache_control.no_store = True
	response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '-1'
	return response


if __name__ == '__main__' and run:
	app.run(host='localhost', debug=True, threaded=True)
	#edit host='0.0.0.0'
	#app.run(port=5000)
