from ast import Import
from lib2to3.pgen2.driver import Driver
import random
from selenium import webdriver #Se usa para el driver de Selenium con Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Esperas explícitas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep #Se usa para el sleep

exePath = r".\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=exePath)
url = 'https://destinationinsights.withgoogle.com'
cookiesPath = '//*[@id="cookieBar"]/div/span[2]/a[2]'
flightAccommodationPath = '/html/body/div[1]/div[24]/div[2]/div/div[1]/div[1]/p'
demandCategoryId = 'select_36'
accommodationId = 'select_option_48'
airId = 'select_option_47'
daterangeId = 'select_value_label_9'
lastdaysId = 'select_option_49'
primaryCountryId = 'select_30'
countriesCompareId = 'select_33'
#Países Principales
argentinaId = 'select_option_565'
#Países Comparar
germanyId = 'select_option_887'
cyprusId = 'select_option_861'
croatiaId = 'select_option_858'
egyptId = 'select_option_869'
spainId = 'select_option_1013'
franceId = 'select_option_881'
greeceId = 'select_option_890'
italyId = 'select_option_913'
moroccoId = 'select_option_951'
portugalId = 'select_option_980'
submitPath = '/html/body/div[1]/div[24]/div[1]/div/div[5]/button'

driver.get(url)
driver.maximize_window()

while True:
    try:
        driver.implicitly_wait(3)
        pageReady = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID,primaryCountryId),'Spain'))
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present. 
    except TimeoutException:
        print("Loading took too much time!-Try again")
        driver.refresh()

#Aceptar cookies
driver.implicitly_wait(10)
cookies = driver.find_element(By.XPATH,cookiesPath)
cookies.click()

def loadingProcess():

    #Mover a Flight & Accommodation Demand Sizing Tool
    driver.implicitly_wait(10)
    flightAccommodation = driver.find_element(By.XPATH,flightAccommodationPath)
    flightAccommodation.click()

    #Primary Country
    driver.implicitly_wait(10)
    primaryCountry = driver.find_element(By.ID,primaryCountryId)    
    driver.implicitly_wait(10)
    primaryCountry.click()
    print("Primary country is ready!")

    #Primary Country = Argentina
    while True:
        try:
            driver.implicitly_wait(10)
            argentina = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,argentinaId))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,argentinaId)))
            driver.implicitly_wait(10)
            argentina.click()
            print("Click Argentina is ready!")
            break # it will break from the loop once the specific element will be present. 
        except:
            print("Failed to click Argentina")

    #Countries to Compare
    driver.implicitly_wait(10)
    countriesCompare = driver.find_element(By.ID,countriesCompareId)
    driver.implicitly_wait(10)
    countriesCompare.click()

    #Germany
    driver.implicitly_wait(10)
    germany = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,germanyId))
    driver.implicitly_wait(10)
    germany.click()

    #Cyprus
    driver.implicitly_wait(10)
    cyprus = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,cyprusId))
    driver.implicitly_wait(10)
    cyprus.click()

    #Croatia
    driver.implicitly_wait(10)
    croatia = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,croatiaId))
    driver.implicitly_wait(10)
    croatia.click()

    #Egypt
    driver.implicitly_wait(10)
    egypt = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,egyptId))
    driver.implicitly_wait(10)
    egypt.click()

    #Spain
    driver.implicitly_wait(10)
    spain = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,spainId))
    driver.implicitly_wait(10)
    spain.click()

    #France
    driver.implicitly_wait(10)
    france = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,franceId))
    driver.implicitly_wait(10)
    france.click()

    #Greece
    driver.implicitly_wait(10)
    greece = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,greeceId))
    driver.implicitly_wait(10)
    greece.click()

    #Italy
    driver.implicitly_wait(10)
    italy = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,italyId))
    driver.implicitly_wait(10)
    italy.click()

    #Morocco
    driver.implicitly_wait(10)
    morocco = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,moroccoId))
    driver.implicitly_wait(10)
    morocco.click()

    #Portugal
    driver.implicitly_wait(10)
    portugal = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,portugalId))
    driver.implicitly_wait(10)
    portugal.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #Exit menu

    #Demand Category
    driver.implicitly_wait(10)
    demandCategory = driver.find_element(By.ID,demandCategoryId)
    driver.implicitly_wait(10)
    demandCategory.click()

    #Deseable Accommodation
    driver.implicitly_wait(10)
    accommodation = driver.find_element(By.ID,accommodationId)
    driver.implicitly_wait(10)
    accommodation.click()

    #Active Flight
    driver.implicitly_wait(10)
    air = driver.find_element(By.ID,airId)
    driver.implicitly_wait(10)
    air.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    #Date Range
    driver.implicitly_wait(10)
    daterange = driver.find_element(By.ID,daterangeId)
    driver.implicitly_wait(10)
    daterange.click()

    #Active Last 30 days
    driver.implicitly_wait(10)
    lastdays = driver.find_element(By.ID,lastdaysId)
    driver.implicitly_wait(10)
    lastdays.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    #Submit
    driver.implicitly_wait(10)
    submit = driver.find_element(By.XPATH,submitPath)
    for i in range(3):
        try:
            submit.click()
            driver.implicitly_wait(10)
            submit = driver.find_element(By.XPATH,submitPath)
        except:
            break
    return print("Process to Submit!")
    
loadingProcess()

while True:
    try:
        driver.implicitly_wait(10)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,submitPath)))
        print("Click Submit is ready!")
        break # it will break from the loop once the specific element will be present. 
    except:
        print("Continue to loadingProcess")
        driver.refresh()
        loadingProcess()

print("Continue to download")
print("Ready!")