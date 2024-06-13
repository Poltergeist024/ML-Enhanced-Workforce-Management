*ML-Enhanced Workforce Management*
<br><br>

*Introduction*<br><br>
This is a project made to make workforce management for HR employees easier by predicting important employee information such as attrition rates and performance.<br>
The project includes creation of a HTML website for HR employees to log in and comprises of  2 ML models and their basic deployment on local server.<br>
The 2 models are for attrition prediction and performance prediction.<br>
It provides HR employees to derive actionable insights by predciting employee attrition and employee performance and appraisal eligibility.<br><br>

*Technology used*<br><br>
ML models created using python and various libraries such as Pandas, Scikit-learn, etc.<br>
Used python 3.8 for coding.<br>
Website design created using HTML and CSS.<br>
All HTML code is in the Templates file. <br>
Flask is used for server configuration and deployment.<br>
mysite.py is the main application comprising of all functions.<br>
To run the website use localserver on port 5000.<br><br>

*Project Flow*<br><br>
On running webiste on browser, the Home page is displayed to the users and the users have the option to either login or register themselves on the website.<br>
The information input in the registration form is sent to a users.csv and secrets.csv file from where it is used to confirm login details.<br>
On login, the user has options to use both models where one has to input the employee details in a form to get prediction results.<br>
User can also add new employees on the website in a database by filling out 'Add employee' form. The filled data can be seen on the website and employee details can also be searched using Employee ID.<br>
The Logout option sends the user to the initial home page.<br>
