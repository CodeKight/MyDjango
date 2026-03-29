# step 1: install virtual environment 

pip install virtualenv 

# step 2: create virtual environment 
python -m venv envvironment_name
or, 
virtualenv environment_name 

# step 3: activate virtual environment
env\Scripts\activate (windows/cmd)
source  env/Scripts/activate (mac/gitbash)
source env/bin/activate (linux)

# step 4: install django 
pip install django 

# step 5: create django project 
django-admin startproject project_name .  # dot(.) create project in the current folder 

# step 6: run the server
python manage.py runserver 
or, 
py manage.py runserver 

# step 7: explore 'manage.py' file 
python manage.py

# step 8: create an app 
python manage.py startapp app_name 

# step 9: add the apps in the settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo', 'note',   # <--- This was added here 
]






# Q. django vs drf -------------------------------------------------
- Question: Is Django and DRF the same?

- Answer: No, they are not the same—they are related but different.

## Django
- A full web framework for building websites and web apps

- Handles:
    - Frontend templates (HTML)
    - Backend logic
    - Database (*ORM*)
    - Authentication, admin panel, etc.

- You can build a complete website using only Django

## Django REST Framework (DRF)
- A toolkit built on top of Django
- Used specifically to create REST APIs

- Handles:
    - JSON responses
    - Serialization (convert data ↔ JSON)
    - API authentication
    - API views, viewsets, routers
    
🔥 Simple Analogy
        Django = Full restaurant 🍽️
        DRF    = Online food delivery system 📦 (API layer)

🧠 Key Difference
        Feature 	Django	                     DRF
        Purpose	        Full web development	     API development
        Output	        HTML pages	             JSON data
        Built on  	Python	                     Django
        Use case	Websites	             Backend for frontend (React, mobile apps, etc.)

💡 Final Understanding
        DRF cannot exist without Django
        Django can exist without DRF

