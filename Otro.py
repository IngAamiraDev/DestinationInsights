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

#Demand Category
demandCategoryList = ['Click', 'Air', 'Accommodation']
demandCategoryId = ['select_36', 'select_option_47', 'select_option_48']

#Date Range
dateRangeList = ['Click','Last 30 days']
dateRangeId = ['select_value_label_9','select_option_49']

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

def loadingProcess():

    #Select to Primary Country
    for i in range(len(primaryCountryList)):
        while True:
            try:
                driver.implicitly_wait(10)
                primaryCountry = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,primaryCountryId[i]))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,primaryCountryId[i])))
                driver.implicitly_wait(10)
                primaryCountry.click()
                print('Primary Country is: ' + primaryCountryList[i])
                break # it will break from the loop once the specific element will be present. 
            except:
                print("Failed to click primary country")
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    #Select Countries to Compare
    for i in range(len(compareCountryList)):
        while True:
            try:      
                driver.implicitly_wait(10)
                countries = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,compareCountryId[i]))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,compareCountryId[i])))
                driver.implicitly_wait(10)
                countries.click()
                print('Country to compare is: ' + compareCountryList[i])
                break
            except:
                print('Failed to click Countries to Compare')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
 
    #Select to Demand Category
    for i in range(len(demandCategoryList)): # 1:Click DemandCategoryId - 2:Deseable Accommodation - 3:Active Flight        
        driver.implicitly_wait(10)
        demandCategory = driver.find_element(By.ID,demandCategoryId[i])
        driver.implicitly_wait(10)
        demandCategory.click()
    print('Select Demand Category is Ready!')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    #Select to Date Range
    for i in range(len(dateRangeId)):
        driver.implicitly_wait(10)
        daterange = driver.find_element(By.ID,dateRangeId[i])
        driver.implicitly_wait(10)
        daterange.click()
    print('Select Date Range is Ready!')
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