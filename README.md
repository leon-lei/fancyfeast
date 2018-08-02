# Instructions on set up

1. Copy the .env file from email into the root fancyfeast directory (one with Pipfile)
    1. Sets up some environmental variables like DJANGO_SECRET_KEY and email credentials
    2. Getting into the practice of excluding  sensitive information from the codebase

------------------------------------------------
2. In root fancyfeast directory
    1. Run command *pipenv install*
    2. This will create a virtual environment with specific versions of python packages installed
    3. Django version > 2.0.6 will break the login and logout views
    
------------------------------------------------
    
3. Run the following command to work in the virtual environment
    1. *pipenv shell*
    
------------------------------------------------

4. Run the following commands to set up the database tables and create an Admin user:
    1. *python manage.py makemigrations*
    2. *python manage.py migrate*
    3. *python manage.py createsuperuser*
        1. This lets you access the admin url (127.0.0.1:8000/admin)
        2. Enter a username and password to create the first user

------------------------------------------------       
        
5. Run the following command to create some dummy data (users, tribes, events)
    1. *python manage.py populate_ff.py*
