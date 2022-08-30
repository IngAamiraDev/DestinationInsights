from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

exePath = r".\chromedriver\chromedriver.exe"
submitPath = '/html/body/div[1]/div[24]/div[1]/div/div[5]/button'

driver = webdriver.Chrome(executable_path=exePath)

def Submit():    
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
print('Submit is Ready!')