# -*- coding: utf-8 -*-

from selenium import webdriver
import time, pickle

driver = webdriver.Chrome('./chromedriver')
print "Se esta abriendo una ventana en chrome."
driver.get("http://www.plus.google.com")
mode=raw_input('Presiona enter cuando te hayas registrado.')
# esperar a que se inicie session

pickle.dump( driver.get_cookies() , open("cookies2.pkl","wb"))