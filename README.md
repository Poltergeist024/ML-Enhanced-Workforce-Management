This is a project made to make workforce management for HR employees easier by predicting important employee information such as attrition rates and performance.
The project includes creation of a HTML website for HR employees to log in and comprises of  2 ML models and their basic deployment on local server.
The 2 models are for attrition prediction and performance prediction.
It provides HR employees to derive actionable insights by predciting employee attrition and employee performance and appraisal eligibility.
Flask is used for server configuration and deployment.
All HTML code is in the Templates file. 
mysite.py is the main application comprising of all functions.
To run the website use localserver on port 5000.
/n
On running code on browser, the Home page is displayed to user and user has option to either login or register themselves on the website.
The information input in the registration form is sent to a users.csv and secrets.csv file from where it is used to confirm login details.
On login the user has options to use both models where one has to input the employee details in a from to get prediction results.
User can also add new employees in the website in a database my filling out 'Add employee' form. The filled data can be seen on the website and employee details can also be searched using Employee ID.
The Logout option sends the user to the initial home page.
