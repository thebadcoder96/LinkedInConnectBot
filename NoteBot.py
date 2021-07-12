import os, time
from selenium import webdriver
from bs4 import BeautifulSoup


#Loggin in to LinkedIn

#os.getcwd()
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/uas/login")
#Enter your email
driver.find_element_by_id('username').send_keys('Enter Email')
word= driver.find_element_by_id('password')
#Enter your password
word.send_keys('Enter Password')
word.submit()
print("Login Sucessful")
time.sleep(6)
#Click 'Not Now' button when asked to remember user profile
try:
    driver.find_element_by_xpath('//button[text()="Not now"]').click()
except:
    print('Button Not now not found')
    pass




#Enter keywords and number of pages to visit
keywords="Enter Keywords here"
pages = 100 #Enter number of pages to stop at



#Initialize/Open the visited profiles file
file = open('visited.txt')
visited = file.readlines()
visited = visited[0].split()
queued = []



#Function to get profile links
def getProfiles(soup, queued):
    profiles = []
    results = soup.find('ul', {'class': 'reusable-search__entity-results-list list-style-none'})
    photo = results.findAll('a', {'class':'app-aware-link','aria-hidden': 'false'})
    for link in photo:
        href = link.get('href')
        if ((href not in visited) and (href not in queued)): profiles.append(href)
    return profiles



for page in range(1, pages+1):
    #Searching for the industry to connect with people
    driver.get("https://www.linkedin.com/search/results/people/?keywords="+keywords+"&origin=CLUSTER_EXPANSION&page="+str(page))
    queued.extend(getProfiles(BeautifulSoup(driver.page_source), queued))
    
    print('Profiles Visited: ', len(visited))
    
    while queued:
        try:
            visiting = queued.pop()
            visited.append(visiting)
            #visiting profile
            driver.get(visiting)
            #getting the name of the profile
            name = driver.find_element_by_class_name("text-heading-xlarge").get_attribute('innerHTML')
            
            #ENTER THE PERSONALIZED NOTE
            message = "Hi "+name.split()[0]+"!\n\n Enter you personalized note here."
            
            #Connecting and sending the personalized note
            #driver.find_element_by_xpath('//button[text()="Connect"]').click()
            driver.find_element_by_class_name('pvs-profile-actions__action').click()
            time.sleep(5)
            
            #If there is error while connecting using the blue connect button, try to connect using the "More" dropdown button
            try:
                driver.find_element_by_class_name('artdeco-button--secondary').click()
            except:
                print("Error connecting with " + name + ". Trying with More button")
                try:
                    driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[3]/div/div/button').click()
                except:
                    driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[3]/div/div/button').click()
                #driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[3]/div/div/div/div/ul/li[4]/div').click()
                finally:
                    time.sleep(2)
                    driver.find_element_by_xpath('//div[@data-control-name="connect"]').click()
                    time.sleep(2)
                    driver.find_element_by_class_name('mr2').click()
                    driver.find_element_by_class_name('artdeco-button--secondary').click()
            finally:
                #Sending the message
                driver.find_element_by_id('custom-message').send_keys(message)
                time.sleep(3)
                driver.find_element_by_class_name('ml1').click()
                time.sleep(5)
                
            #saving visited profile
            with open('visited.txt', 'a') as f:
                f.write(str(visiting)+" ")
            f.close()
            
        except:
            print("Unable to connect with profile: " + name)
            
print('Completed!! Profiles Visited: ', len(visited))
driver.quit()
