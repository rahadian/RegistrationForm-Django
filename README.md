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
    
Change the DEBUG to False
8. In settings.py, edit the DATABASES and ALLOWED_HOSTS sections

    >DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'formku',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
    }
    
    
     > ALLOWED_HOSTS = ['192.168.37.6','127.0.0.1']
    
change the USER and PASSWORD with your mysql user and password. If you confused, you can copy settings.py in this repo to your directory.

9. Back to the formku project directory and do migrations with this command
    > python manage.py makemigrations users
10. Implement it to database use this command
    > python manage.py migrate
11. Make superuser use this command
    > python manage.py createsuperuser
12. Run the server 
    > python manage.py runserver
