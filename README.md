# Challenge Amigo Tech

Hi, this is a challenge to automate a simple e-commerce, here you can find the automation for some parts of the application.


# How to set up the environment - for Windows 10?

 1. **Install Python:**
	 In this case, I used the most updated Python version (3.12.1) https://www.python.org/downloads/
2. **Install Intellij or VSCode:** https://www.jetbrains.com/idea/download/?section=windows 
3. **Install Chrome or update:** 
your chrome needs to be in the 120.0.6099.225 version because different versions of Chromedriver work with specific versions of Chrome
4. **Install WebDriver (Chromedriver) for Chrome (be aware to choose between the Chromedriver Win64 or win32 version):** 
https://googlechromelabs.github.io/chrome-for-testing/
I used the https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip version, remember to add the chromedriver to your environment variable PATH
5. **Install the Selenium package for Python:** 
go to https://pypi.org/project/selenium/ OR you can install directly from your terminal

    <code>pip install selenium</code>
    
6. **If you are not able to install selenium**, you might have to install pip (it's a package installer for python, and it generally comes with python, if you installed python from python.org) https://pip.pypa.io/en/stable/installation/
7. Install pytest:
I'm using the pytest framework to do the testing, so you also have to install pytest for the code to run https://pypi.org/project/pytest/ or you can type the below command in your terminal:

    <code>pip install pytest</code>

9. **Known issues:**
Python 3.12.1 is having some issues related to packages not being installed, these packages were removed from Python, so you might have to install some things for this code to work. You can find more info about this, here: https://github.com/pypa/setuptools/issues/3661

    <code>pip install setuptools</code>


## How the folders are organized?

 - **pages**
 This folder contains all the pages related to the application. It contains classes representing those pages with different methods inside of them.
 - **tests**
 This folder contains all the test files, example: the test related to the cart functionality is test_cart.py
 - **utilities**
 This folder contains the files that will be utilized for all the tests, like the locators and test data.
 - **conftest**
 Not a folder but a file. This file contains a function related to the pytest framework. This function works as the setup and teardown for the tests.


## How to run the tests?
1. After doing the steps above, open the project folder
2. Go to the tests folder
3. Inside this folder, choose a file. Example: you can choose the **test_cart.py** file
4. Inside the chosen file you will see a class with all the tests related to that functionality, every function that starts with **test_** is a different test, for example: **def test_add_to_cart**
5. If you want to run all the tests related to the class, you can type the following command inside your project folder:

    <code>pytest -k ClassName</code>

Example: pytest -k TestCartPage

## Why Python + Selenium + Pytest + Page Object Model?
- Python is easy to use and easy to setup
- Selenium it's the framework that I have more knowledge of working with
- Pytest is a framework simple and easy to use, it also has the fixture functionality that lets us work sharing resources between the tests
- I developed the automation following the Page Object Model because I believe is very organized and easy to maintain the code 

