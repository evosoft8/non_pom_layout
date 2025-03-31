# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get("https://google.com/")
# web_element = driver.find_element(By.NAME, 'q')
# web_element.send_keys("Selenium Webdriver" + Keys.ENTER)

# time.sleep(30)
from pytest import  mark

@mark.api
def test_prueba01():
    assert True

@mark.data
def test_prueba02():
    assert True

def test_prueba03():
    assert True == True


