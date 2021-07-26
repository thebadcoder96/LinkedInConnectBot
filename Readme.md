# LinkedIn Bot to Connect and Send Personalized Note

This is a python bot made to search for people in the certain industries and connect with them inlcuding sending a personalized note.

### Motivation
Job search is a long a tidious process and its often not very rewarding. So, I decided to brush up some python and make a bot to autoconnect with people in similar industries as I was interested in to make some part of the process easier by using my skills.

### Frameworks
- Selenium -Framework to control web browsers
- BeautifulSoup - Library for parsing HTML documents

**NOTE :** You must also install the webdriver for your browser.

### Installation
Using python's package manager pip to install the dependencies
``` sh
pip install selenium
pip install beautifulsoup4
```
You can install the **webdriver** for Chrome browser [here](https://chromedriver.chromium.org/downloads). Be sure to install the webdriver according to your chrome browser version. You can google and find the webdrivers for other browsers as well. 

**NOTE :** 
- If you are on **Mac**, you have to move the webdriver to ```/usr/local/bin``` folder (*Go -> Go to Folder* then paste the path) to run the code. 
- If you are on PC, you can just put the webdriver's path in the line ```driver = webdriver.Chrome(INSERT_PATH_TO_WEBDRIVER) ``` inside the *NoteBot.py* file.


### How to run 

**Before runnning the code:** Please enter the LinkedIn email, password, pages to stop at, keywords to search (be sure to include 'Hiring' if you are jobseeking), the personalized message to run the program. I have commented the parts to fill in the **NoteBot.py** file. 

Run the *NoteBot.py* file on any Python IDE or Execute the following command on the terminal:
``` sh
!python3 NoteBot.py 
```


***PLEASE DO NOT MISSUSE THIS CODE***
