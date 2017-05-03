# RegistrationForm-Django
This project made by my friend and I. I designed and made a web from django and my friend designed and made the android app of it. This is just Registration Form (ex: for an event), so the participants only need registration and the admin can view the list of participants via android or desktop. For database use mysql so for the first install :
> sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev

> pip install django mysqlclient

# How do I run this project ?
1. Make a database (ex:formku) then exit.
2. Go to /var/www/html
3. Start django project with this command :
    > django-admin startproject formku
4. Enter the formku directory
5. Start app in project use this command :
    > python manage.py startapp users
6. Copy the directories from this repo to your directory and adjust them.
7. In formku directory, edit the settings.py file and add this to INSTALLED_APPS section
    > 'users.apps.UsersConfig',
8. 
