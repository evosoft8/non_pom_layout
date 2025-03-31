import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#TC-2 Parabank
def test_navegacion_browser():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)
    web_element = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/ul[1]/li[2]/a')
    time.sleep(2)
    web_element.click()
    time.sleep(2)
    driver.save_screenshot('./test_screenshots/withdraw_funds.png')

    time.sleep(5)


#web_element = driver.find_element(By.ID,"field2")

#TC-3 Parabank | Home Page
def test_navegacion_browser_transfer_funds():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)
    web_element = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/ul[1]/li[3]/a')
    time.sleep(2)
    web_element.click()
    time.sleep(2)
    driver.save_screenshot('./test_screenshots/transfer_funds.png')

    time.sleep(5)


#TC-4- Parabank | Home Page
def test_navegacion_browser_check_balance():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)
    web_element = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/ul[1]/li[4]/a')
    time.sleep(2)
    web_element.click()
    time.sleep(2)
    driver.save_screenshot('./test_screenshots/check_balance.png')

    time.sleep(5)


#TC-5- Parabank | Home Page
def test_navegacion_browser_make_deposits():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)
    web_element = driver.find_element(By.XPATH, '//*[@id="rightPanel"]/ul[1]/li[5]/a')
    time.sleep(2)
    web_element.click()
    time.sleep(2)
    driver.save_screenshot('./test_screenshots/make_deposits.png')
    time.sleep(5)


#TC-15- Parabank | Customer Login-register
def test_login_register():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)
    web_element = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/p[2]/a')
    web_element.click()
    time.sleep(3)

    name_textbox = driver.find_element(By.ID,'customer.firstName')
    name_textbox.send_keys('luiggi')

    time.sleep(2)

    last_textbox = driver.find_element(By.ID, 'customer.lastName')
    last_textbox.send_keys('mera')

    time.sleep(2)

    address_textbox = driver.find_element(By.ID, 'customer.address.street')
    address_textbox.send_keys('123 abc st')
    time.sleep(2)

    city_textbox = driver.find_element(By.ID, 'customer.address.city')
    city_textbox.send_keys('miami')
    time.sleep(2)

    state_textbox = driver.find_element(By.ID, 'customer.address.state')
    state_textbox.send_keys('florida')
    time.sleep(2)


    zipcode_textbox = driver.find_element(By.ID, 'customer.address.zipCode')
    zipcode_textbox.send_keys('33123')
    time.sleep(2)

    phone_textbox = driver.find_element(By.ID, 'customer.phoneNumber')
    phone_textbox.send_keys('3051234567')
    time.sleep(2)

    ssn_textbox = driver.find_element(By.ID, "customer.ssn")
    ssn_textbox.send_keys('1234567890')
    time.sleep(2)

    user_textbox = driver.find_element(By.ID, 'customer.username')
    user_textbox.send_keys('luiggitest')
    time.sleep(2)

    pass_textbox = driver.find_element(By.ID, 'customer.password')
    pass_textbox.send_keys('123456')
    time.sleep(2)

    pass2_textbox = driver.find_element(By.ID, 'repeatedPassword')
    pass2_textbox.send_keys('123456')
    time.sleep(2)

    register = driver.find_element(By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
    register.click()
    time.sleep(3)

    driver.save_screenshot('./test_screenshots/login_register.png')
    time.sleep(5)



#if driver.find_elementlement(By.ID('customer.address.state') drive.getText() == "":
 #   print('field is empty')

#else:
#   print('field filled up with data')

#TC-16- Parabank | Customer Login-succesful
def test_login_successful():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)

    user_textbox = driver.find_element(By.NAME, 'username')
    user_textbox.send_keys('luiggitest')
    time.sleep(2)

    pass_textbox = driver.find_element(By.NAME,'password')
    pass_textbox.send_keys('123456')
    time.sleep(2)

    login = driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[3]/input')
    login.click()
    time.sleep(3)

    driver.save_screenshot('./test_screenshots/sign_in.png')
    time.sleep(3)