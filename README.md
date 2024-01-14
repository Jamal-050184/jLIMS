Chapter -1 : Starting
--------------------------

1. Check python version by command line// if not install first
	C:\Users\Admin>py --version

2. Check that PIP is installed. // PIP is package of python // if not install first
	C:\Users\Admin>pip --version

3. Create a folder where your project will be created.//my directory [ E:\E_Group_A\DEV_DEVELOPING\django ]

4. In that folder create a vertual environment // VE is used for project package identification // if not download and install first (pip install virtualenv)
	E:\E_Group_A\DEV_DEVELOPING\django\jlims>py -m venv venv_jlims // IT will create some folder and files with package
	
5. Activate the created virtual environment
	E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims>Scripts\activate.bat

6. Install Django in that virtual environment
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims>pip install django

7. Check that Django installed successfully
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims>django-admin
	
8. Check Django version
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims>django-admin --version

9. Create a Project in that virtual environment
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims>django-admin startproject proj_jlims // here proj_jlims is project name.

10. Navigate to the project name and run the project 
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims\proj_jlims>py manage.py runserver // It will return a ip. browse the IP in browser. it will show django default page. Now your project is ready for developing

Chapter-2 : template
-----------------------
1. Create a app inside project // it will create some folders and files
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims\proj_jlims>py manage.py startapp app_jlims

2. By using VS Code open the project

3. In setting.py inside the project add the app name where django default application already 

4. In views.py write a function

5. Create a file named urls.py in the same folder as the views.py file

6. In that urls.py include the function name that created in views.py

7. In the main urls.py include the app name

8. Now run the server and browse the ip. it will return the function that created in views.py

9. create a template folder inside project directory

10. Make html file in that template folder

11. run the command 
	py manage.py migrate

12. In settings.py below BASE_DIR write the code [TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')]

13. In settings.py , TEMPLATES --> inside 'DIRS': [TEMPLATE_DIR]

14. Create a ststic folder where template created. 

15. In setting.py write [STATIC_DIR = os.path.join(BASE_DIR,'static')]  and below write [STATICFILES_DIRS = [STATIC_DIR, ]]

Chapter- 3: ORM / Model
---------------------
1. In Model.py create a model 
2. Show migrations
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims\proj_jlims>py manage.py showmigrations
3. Make migrations
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims\proj_jlims>py manage.py makemigrations app_jlims
4. Migrate
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims\proj_jlims>py manage.py migrate
5. Call the model from views and urls
6. Create a Super User like Admin
7. In admin app show the library model
	In admin.py write functions

Capter -4: Form/Login/Logout/user creation
------------------------
1. Inside app directory create a new file named forms.py
2. In forms file write class for Login and User Creation
3. Create 2 html file for Login and registration
4. In views.py write functions for login, logout and registration

Chapter -5: Django Rest Framework
----------------------------
1. Install Django rest framework [ pip install djangorestframework ]
2. Create a app for api
	(venv_jlims) E:\E_Group_A\DEV_DEVELOPING\django\jlims\venv_jlims\proj_jlims>py manage.py startapp api_jlims
3. Register the app into Installes app inside setting.py
4. Include the app into urls.py of main project  [path('api/',include('api_jlims.urls')),]
5. Create a file named serializers.py and write desired code
6. Create urls.py insode api app and write desired code 
7. Run server and test the api [http://127.0.0.1:8000/api]
