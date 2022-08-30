from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

exePath = r".\chromedriver\chromedriver.exe"
primaryCountryId = 'select_30'

driver = webdriver.Chrome(executable_path=exePath)

def LoadPage():
    while True:
        try:
            driver.implicitly_wait(3)
            pageReady = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID,primaryCountryId),'Spain'))
            print("Page is ready!")
            break # it will break from the loop once the specific element will be present. 
        except TimeoutException:
            print("Loading took too much time!-Try again")
            driver.refresh()
print('LoadPage is Ready!')