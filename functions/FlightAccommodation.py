from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

exePath = r".\chromedriver\chromedriver.exe"
flightAccommodationPath = '/html/body/div[1]/div[24]/div[2]/div/div[1]/div[1]/p'
driver = webdriver.Chrome(executable_path=exePath)

def FlightAccommodation():
    #Mover a Flight & Accommodation Demand Sizing Tool
    driver.implicitly_wait(10)
    flightAccommodation = driver.find_element(By.XPATH,flightAccommodationPath)
    flightAccommodation.click()
print("FlightAccommodation is Ready!")