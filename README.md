# Django Login System



## Setup Instructions

### Installation
- Clone the Repository:
   - git clone https://github.com/abhiram7605/DjangoProject.git

- Install Django:
   - pip install django

- Set Up the Django Project:
   - django-admin startproject Login_System
   - python manage.py startapp Loginify

- Configure Settings:
   - Add `Loginify` to `INSTALLED_APPS` in `Login_System/settings.py`:

- Create a Superuser:
   - python manage.py createsuperuser



## Project Structure
- Views:
- created multiple views in the views.py file.
  - hello view: which test the basic Httpresponse and print Hello World
  - Signup view: this allows users to enter their details like Username, Email, Password
  - Signin view: Allows users to signin and check the user is present or not
  - all_data view: it retrives the data present in the database
  - single_user view: it allows the users to perform CRUD operations on the data base

- Models:
- Created a model UserDetails which has 3 objects, Username, Email, Password

- Template:
Created a custom template where it gets forms data from views and creates the fields dinamiccaly as per views


- Forms:
- created 2 forms model form and and a normal form
  - Model form is for signup page
  - Normal form is used for signin page

- Serializer:
- created a serializer that serializes teh input data and it is named as UDserializer


- URLs:
    - Defined in `Loginify/urls.py` to map views to endpoints.
  

- Django Shell: 
  - Used for managing user data via command-line operations.


## Usage
- Signup:
   - Navigate to `/signup/` to access the signup form.
   - Enter a unique username, email, and password.

- Login:
   - Navigate to `/login/` to access the login form.
   - Enter your email and password.

- CRUD Operations:
   - Use `/all-users/` to view all user details.
   - Use `/user/<email>/` to retrieve, update, or delete a specific user by email.


- Admin Interface:
   - Log in with the superuser credentials at `/admin/` to manage users.


## Testing
- Postman:
  - Test CRUD operations by sending HTTP requests to the defined endpoints.


