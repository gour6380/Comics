from selenium import webdriver
import requests
from time import sleep
import os
import tarfile

try:
    #Here you can use Firefox, Chrome, Safari as per requirement
    browser = webdriver.Firefox(executable_path=r'sel/geckodriver') #path to Geckodriver change as per your requirement
    browser.get('https://pdflake.com/nagraj-comics-pdf/')
except:
    download_url = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-macos.tar.gz" #this you can choose your version of geckodriver
    response = requests.get(download_url)
    if not os.path.exists('sel'):
        os.makedirs('sel')
    with open('sel/geckodriver.tar.gz', 'wb') as f:
        f.write(response.content)
    tar = tarfile.open("sel/geckodriver.tar.gz", "r:gz")
    tar.extractall("sel")
    tar.close()
    browser = webdriver.Firefox(executable_path=r'sel/geckodriver')
    browser.get('https://pdflake.com/nagraj-comics-pdf/')
    
elems = browser.find_elements("xpath","//a[@href]")

urls = []
for ele in elems:
    if "pdf" in ele.get_attribute("href")[-3:]:
        urls.append(ele.get_attribute("href"))
a = 0
for url in urls:
    a += 1
    response = requests.get(url)
    URL_names = url.split("/")
    name = URL_names[-1]
    if not os.path.exists('Nagraj'):
        os.makedirs('Nagraj')
    with open('Nagraj/'+name,'wb') as f:
        f.write(response.content)
    sleep(0.4)
    print("{0} file a is done".format(a))