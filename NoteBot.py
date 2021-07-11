import os, time
from selenium import webdriver
from bs4 import BeautifulSoup


#Loggin in to LinkedIn

#os.getcwd()
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/uas/login")
driver.find_element_by_id('username').send_keys('mishalksa@hotmail.com')
word= driver.find_element_by_id('password')
word.send_keys('Mishal@1245')
word.submit()
time.sleep(6)
#Click 'Not Now' button when asked to remember user profile
try:
    driver.find_element_by_xpath('//button[text()="Not now"]').click()
except:
    print('Button Not now not found')
    pass



#Setting up keywords, message and number of pages to visit
keywords="Data Analysis,Data Engineering,Hiring,Data Science"
pages = 10


#Initialize/Open the visited profiles file
file = open('visited.txt')
visited = file.readlines()
queued = []



#Function to get profile links on a page
def getProfiles(soup, queued):
    profiles = []
    results = soup.find('ul', {'class': 'reusable-search__entity-results-list list-style-none'})
    photo = results.findAll('a', {'class':'app-aware-link','aria-hidden': 'false'})
    for link in photo:
        href = link.get('href')
        if ((href not in visited) and (href not in queued)): profiles.append(href)
    return profiles
    



for page in range(1, pages):
    #Searching for the industry to connect with people
    driver.get("https://www.linkedin.com/search/results/people/?keywords="+keywords+"&origin=GLOBAL_SEARCH_HEADER&page="+str(pages))
    queued.extend(getProfiles(BeautifulSoup(driver.page_source), queued))
    
    while queued:
        try:
            visiting = queued.pop()
            visited.append(visiting)
            #visiting profile
            driver.get(visiting)
            name = driver.find_element_by_class_name("text-heading-xlarge").get_attribute('innerHTML')
            message = "Hi "+name.split()[0]+"!\nMy name is Mishal and I am a recent Data Science Grad looking for my next opportunity.\nThis message was sent using a LinkedIn Bot I created with Python. Check it out on https://github.com/thebadcoder96 or my resume here: bit.ly/3xxEdV9"

            #Connecting and sending the personalized note
            #driver.find_element_by_xpath('//button[text()="Connect"]').click()
            driver.find_element_by_class_name('pvs-profile-actions__action').click()
            time.sleep(5)
            driver.find_element_by_class_name('artdeco-button--secondary').click()
            driver.find_element_by_id('custom-message').send_keys(message)
            driver.find_element_by_class_name('ml1').click()

            #saving visited profile
            with open('visited.txt', 'a') as f:
                f.write(str(visiting)+'\n')
            f.close()
            time.sleep(7)

            if (len(visited)%50==0):print('Profiles Visited: ', len(visited))
        except:
            print("Unable to connect with profile" + visiting)