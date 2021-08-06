from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

# Gets the latest driver version for Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

#URL of website
driver.get("https://www.divercity.io/")

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

#End driver session
driver.quit()