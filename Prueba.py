from selenium import webdriver #Se usa para el driver de Selenium con Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Esperas explícitas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path=r".\chromedriver\chromedriver.exe")
submitPath = '/html/body/div[1]/div[24]/div[1]/div/div[5]/button'

#Initial Process
initialProcessList = ['Cookies','FlightAccommodation']
initialProcessPath = ['//*[@id="cookieBar"]/div/span[2]/a[2]','/html/body/div[1]/div[24]/div[2]/div/div[1]/div[1]/p']

#Primary Country
primaryCountryList = ['Click','Argentina']
primaryCountryId = ['select_30','select_option_565']

#Compare to Country
compareCountryList = ['Click','Germany', 'Cyprus', 'Croatia', 'Egypt', 'Spain', 'France', 'Greece', 'Italy', 'Morocco', 'Portugal']
compareCountryId = ['select_33','select_option_887', 'select_option_861', 'select_option_858', 'select_option_869', 'select_option_1013', 'select_option_881', 'select_option_890', 'select_option_913', 'select_option_951', 'select_option_980']

#Date Range
dateRangeList = ['Click','Last 30 days']
dateRangeId = ['select_value_label_9','select_option_49']

demandCategoryList = ['Click','Accommodation','Air']
demandCategoryId = ['select_36','select_option_48','select_option_47']

driver.get('https://destinationinsights.withgoogle.com')
driver.maximize_window()

while True:
    try:
        driver.implicitly_wait(3)
        pageReady = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID,primaryCountryId[0]),'Spain'))
        print("Page is ready!")
        break # it will break from the loop once the specific element will be present. 
    except TimeoutException:
        print("Loading took too much time!-Try again")
        driver.refresh()

# Select to Initial Process
for i in range(len(initialProcessList)):
    driver.implicitly_wait(10)
    initialProcess = driver.find_element(By.XPATH,initialProcessPath[i])
    initialProcess.click()
print('Select Optional List is Ready!')

#Select to Demand Category (Air)
def selectAccomm():
    for j in range(len(demandCategoryList)):
        while True:
            try: 
                driver.implicitly_wait(10)
                demandCategory = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,demandCategoryId[j]))                
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,demandCategoryId[j])))
                driver.implicitly_wait(10)
                demandCategory.click()
                break
            except:
                print('Failed to Demand Category')
    print('Select Demand Category is Ready!')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#selectAir()
#print('Slect to Air ok')

selectAccomm()
print('Slect to Accomm ok')
