from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
a=1
try:
    driver = webdriver.Chrome()
    driver.get('PUT THE LINK OF LOGIN PAGE OF GMAIL')
    driver.maximize_window()
    time.sleep(2)
    username_field = driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    username_field.send_keys('SENDER_MAIL_ID')
    username_field.send_keys(Keys.RETURN)
    time.sleep(2)
    password_field = driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    password_field.send_keys('PUT THE PASSWORD HERE')
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)
    popUp=driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    popUp.send_keys(Keys.RETURN)
    print('!! Logged In !!')
except Exception as e:
    print('!! Retry Again !!', e)
time.sleep(3)

#Write the recipient, subject and attach the image
try:
    composeButton = driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    composeButton.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE').click()
    print('!! Ready To Write Mail !!')
    time.sleep(5)
    receiver=driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    receiver.send_keys('RECEIVER_MAIL_ID')
    print('ok0')
    subject = driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    subject.send_keys('SUBJECT')
    time.sleep(5)
    print('ok1')
    # For uploading the image or file
    upload_field = driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    upload_field.send_keys('PATH_OF_THE_IMAGE')
    time.sleep(5)
    print('File Uploaded')
    sendButton = driver.find_element(By.XPATH, 'PUT_THE_XPATH_HERE')
    sendButton.send_keys(Keys.RETURN)
    time.sleep(3)
    print('File Sent')
except Exception as e:
    print('!! ERROR !!', e)
