import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://grabpdf.in/schoolacad.html"
r = requests.get(url,verify=False)
driver.get(url)

a=driver.find_element_by_class_name("classwise").find_elements_by_tag_name("a") 
la=[]
for l in a:
    c=(l.get_attribute("href"))
    la.extend(c.split(" "))
print(la)
# for j in la:
#     sleep(2)
#     driver.get(j)