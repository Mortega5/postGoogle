# -*- coding: utf-8 -*-

from selenium import webdriver
import time, pickle, sys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://plus.google.com/')
cookies = pickle.load(open("cookies.pkl", "rb"))


if not cookies:
  print "Es necesario un fichero con las cookies de session"
  print "Visita: http://stackoverflow.com/questions/15058462/how-to-save-and-load-cookies-using-python-selenium-webdriver"
  exit(-1)
  
for cookie in cookies:
    new_cookie={}
    new_cookie['name']=cookie['name']
    new_cookie['value']=cookie['value']
    driver.add_cookie(new_cookie)
    
driver.get('https://plus.google.com/')
time.sleep(1)

if (len(sys.argv)>1):
  text = sys.argv[1]
else:
  text = "Who needs a public API when you can 'hack' google plus to publish using selenium?"

xpath=".//*[contains(text(),'¿Tienes algo nuevo que contar?')]"
textbox = driver.find_element_by_xpath(xpath);

textbox.click()
time.sleep(0.8)

textInput = driver.find_element_by_id('XPxXbf')
textInput.send_keys(text)

sendButtonText ="//div[contains(@class, 'O0WRkf') and contains(@class, 'zZhnYe')]"

#sendButtonText=".//*[contains(text(),'Compartir') and contains(concat(' ', @class, ' '), 'd-k-l')]"

sendButton = driver.find_element_by_xpath(sendButtonText)

sendButton.click()

time.sleep(2)
driver.quit()