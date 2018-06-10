# my_homepage
This is my project of building a webpage with Python and the framework Flask. Please download to run it.
Before running it, you need to install Python, Flask, and a virtual environment.
Suppose you already have Python on your computer:
    1. Download this repository to your computer;
    2. Download 'virtualenv' by entering the following command in the terminal:
       $ sudo easy_install virtualenv
    3. Go to the directory "my_homepage",and create a virtual environment with the following command:
       $ virtualvenv venv
    4. Activate the virtual environment by the following command:
       $ source venv/bin/activate
    5. After entering the virtual environment, a (venv) should exist before the $ in the terminal. After the virtual envoronment is created and activated, Flask can be installed in it:
       (venv) $ pip install flask
    6. A small hint to check if Flask is installed successfully: start the Python interpreter and import Flask into it by:
       >>> import flask
       If the statement does not return any errors then the Flask is installed.
    7. Set the environment variable 'FLASK_APP' by the following command:
       (venv) $ export FLASK_APP=homepage.py
    8. Run the web application:
       (venv) $ flask run
       
 Done!



