from selenium import webdriver
import requests


driver = webdriver.Chrome(executable_path= "C:\chromedriver.exe")

driver.get("https://sandbox.divercity.io/")

#load page fully
driver.implicitly_wait(3)

#target footer section
footer_links = driver.find_elements_by_xpath("//footer//a")

#print links with status code
for links in footer_links:
    l = requests.head(links.get_attribute("href"))
    print(links.get_attribute('href'), l.status_code)

#status code 999 = LinkedIn Page
#status code 403 = Broken links

