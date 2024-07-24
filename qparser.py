from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Выберите браузер и введите его номер: 1.Chrome 2.Firefox")
a = int(input())
if(a == 1):
 driver = webdriver.Chrome()
else:
     if(a == 2):
      driver = webdriver.Firefox()
     else:
      print("Ошибка, вы ввели не верное значение! Попробуйте снова")

driver.get('https://2gis.kz/astana?m=71.437475%2C51.139526%2F11.93')  
time.sleep(4)
h1_element = driver.find_element(By.CLASS_NAME, "_x4ac6o")
