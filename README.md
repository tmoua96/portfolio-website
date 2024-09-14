Portfolio Website

A portfolio website built using:
- Python/Django
- PostgreSQL
- Javascript
- HTML/CSS/Bootstrap

Most of the layout is by Start Bootstrap's template(https://startbootstrap.com/theme/personal). The project's resume, projects, and contact sections are handled primarily through Django, PostgreSQL and Javascript.

The project startup follows the usual Django usage. From within the app directory with the manage.py file using the terminal, run the following command: (windows) 'py manage.py runserver', (mac/linux) 'python manage.py runserver'. If that doesn't work, try 'python3' as the command.

A '.env' file will need to be created so your configs can be loaded in the settings.py file. The file should look like the following:

SECRET_KEY = 'your_secret_key'
DATABASE_NAME = 'your_database_name'

You'll use key value pairs such as this. You should also make sure your .env file is in the gitignore file to keep credentials safe.