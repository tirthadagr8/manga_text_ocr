from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

brave_path = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"
# Define Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path
chrome_options.add_argument('headless')

# Initialize the webdriver without specifying executable path
driver = webdriver.Chrome(options=chrome_options)
def fetch_data(s):
    link='https://www.deepl.com/en/translator#ja/en/'+s
    driver.get(link)
    sol=WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
        (By.XPATH,"//div[@lang='en-US']/p/span")
        )
        )
    # print(len(sol))
    temp=driver.find_elements(By.XPATH,"//div[@lang='en-US']")
    s=''
    for t in temp:
        s+=t.text
    return s

# print(fetch_data('．．．やっぱここは異世界で'))
