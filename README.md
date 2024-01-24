# Challenge Amigo Tech

- <b>How to setup the environment - for Windows 10?</b><br>
  1. Install Python 
  2. Install VSCode/Intellij: 
  3. Install Chrome: 
  4. Install WebDriver (Chromedriver) for Chrome (be aware to choose between the Chromedriver Win64 or win32 version): https://googlechromelabs.github.io/chrome-for-testing/ <br>
     I used the https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip version, remember to add the chromedriver to your environment variable PATH
  5. Install the Selenium package for Python: go to https://pypi.org/project/selenium/
     In this case, you will have to execute the following command on PowerShell: <code>pip install selenium</code> Remember to add python to your environment variable PATH

- <b>How the folders are organized?</b>
  1. <b>pages folder</b>: this folder contains all the pages related to the challenge
  2. <b>config folder</b>: the configuration to run the tests, in this folder, you will find a file with some variables to run the tests, you don't have to change anything.
  3. <b>resources</b>: in this folder, you will find the locator file, which contains all the locators necessary to find the elements on the pages, these locators are being used by the tests
  3. <b>tests</b>: in this folder, 


- <b>How to run a test?</b>
  1. Go to the file that starts with the <b>test.</b> example: <b>test_.py</b>
  2. Inside the file you will find a __main__ block code, the only thing you will have to do to run the tests inside this file is to simply run the file.



