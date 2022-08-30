from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

exePath = r".\chromedriver\chromedriver.exe"
cookiesPath = '//*[@id="cookieBar"]/div/span[2]/a[2]'

driver = webdriver.Chrome(executable_path=exePath)

def Cookies():
    #Aceptar cookies
    driver.implicitly_wait(10)
    cookies = driver.find_element(By.XPATH,cookiesPath)
    cookies.click()
    return print('Cookies is Ready!')