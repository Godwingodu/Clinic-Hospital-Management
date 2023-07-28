
# Clinic Hospital Management 

The web application allows for basic CRUD operations (Create, Read, Update, Delete) for patients' records. It includes a user authentication system for user registration, login, and logout, ensuring data privacy and security.



## Setup Instructions
1 . Clone the repository git clone https://github.com/Godwingodu/Clinic-Hospital-Management

2 . Navigate to the working directory

3 . Open the project from the code editor

4 . Create virtual environment python -m venv env

5 . Activate the virtual environment source env/Scripts/activate

6 . Install the required packages to run the project pip install -r requirements.txt

7 . Run the server python manage.py runserver
## Features

1. User Authentication: Users can register, log in, and log out securely.
2. Patient Records: I implemented a Django model for patients' records, capturing their full name, Date of Birth (DOB),Gender, Contact Number, Address, and Medical Condition.
3. Functionalities: The application provides views and templates for listing all patients' records, creating a new patient record,viewing a patient's details, updating a patient's record, and deleting a patient's record.
4. Form Validation: Proper form validation is in place to ensure that required fields are validated before submission.
##
Extra Features:
As an optional addition, I also implemented the following bonus features:
1. Search Functionality: Users can search for patients based on their names or medical conditions.
2. Pagination: Patient list pages are paginated to display a limited number of patients per page, improving the user experience.
3. Data Export: We can export the patient's data into Excel, CSV and pdf format.
4. Filter: I included a Filter option so we can filter the patient's data into certain entries like 5,10,15
5. Unit Tests: I included unit tests for critical parts of the application to ensure its stability and
reliability.

## Screenshots

Front-page:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/c5f82f52-98cb-4916-a83c-4614d3da97a1)

Home-page:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/ea90b983-87bd-4939-87c0-1ebea0ba3f81)

View-Patient:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/1f7ab138-c6b0-4b2a-acdf-aceda9d1f0ae)

User-Registration:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/6ab88553-c2ad-4359-ba16-6473263b1d5c)

Add-Patient:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/05ef82b1-8913-4025-b34d-6e5d99ccd15c)

User-Login:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/2c6d3f36-f0b8-449b-9515-871f37846545)

Delete-Patient
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/b747f902-57d6-4ea0-80fa-18f63b063f1b)

Update-Patient:-
![image](https://github.com/Godwingodu/Clinic-Hospital-Management/assets/108955514/fccdbff2-f8b0-4491-9c07-a1bd82e2c37d)
