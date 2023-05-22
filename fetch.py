from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
def fetch_data(s):
    link='https://www.deepl.com/en/translator#ja/en/'+s
    driver.get(link)
    sol=WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
        (By.XPATH,"//div[@title='Click a word to see alternative translations']")
        )
        )
    return sol.text

# print(fetch_data('体力が回復したわけではあるまい？'))