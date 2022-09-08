from select import select
from selenium import webdriver #Se usa para el driver de Selenium con Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Esperas explícitas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome(executable_path=r".\chromedriver\chromedriver.exe")
submit_path = '/html/body/div[1]/div[24]/div[1]/div/div[5]/button'
download_css_selector = 'body > div:nth-child(2) > div.glue-mod-spacer-6-bottom.glue-mod-spacer-6-top > div.compare.glue-mod-spacer-5-bottom > div > div.demand__from > div.charts__header > div > svg.geographic-demand__export.ng-scope > use'
demand_from_css_selector = 'body > div:nth-child(2) > div.glue-mod-spacer-6-bottom.glue-mod-spacer-6-top > div.compare.glue-mod-spacer-5-bottom > div > div.demand__from > div.demand__from--canva > svg > g > g:nth-child(23) > text:nth-child(1)'

#Initial Process
initial_process_list = ['Cookies','FlightAccommodation']
initial_process_path = ['//*[@id="cookieBar"]/div/span[2]/a[2]','/html/body/div[1]/div[24]/div[2]/div/div[1]/div[1]/p']

#Primary Country
primary_country_list = ['Argentina','Germany','Australia','Austria','Belgium']
primary_country_id = ['select_option_565','select_option_637','select_option_568','select_option_569','select_option_575']

#Compare to Country
compare_country_list = ['Click','Germany', 'Cyprus', 'Croatia', 'Egypt', 'Spain', 'France', 'Greece', 'Italy', 'Morocco', 'Portugal']
compare_country_id = ['select_33','select_option_887', 'select_option_861', 'select_option_858', 'select_option_869', 'select_option_1013', 'select_option_881', 'select_option_890', 'select_option_913', 'select_option_951', 'select_option_980']

#Demand Category
demand_category_list = ['Air','Accommodation']
demand_category_id = ['select_option_47', 'select_option_48']

#Date Range
date_range_list = ['Click','Last 30 days']
date_range_id = ['select_39','select_option_49']

driver.get('https://destinationinsights.withgoogle.com')
driver.maximize_window()


#Select Countries to Compare
def countries_compare():
    for i in range(len(compare_country_list)):
        time.sleep(0.3)
        while True:
            try:      
                countries = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,compare_country_id[i]))
                countries.click()
                print('Country to compare is: ' + compare_country_list[i])
                break
            except:
                print('Failed to click Countries to Compare')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


#Select to Demand Category
def demand_category_click():     
    click_category = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_36'))
    time.sleep(0.3)
    click_category.click()

def demand_category_air():
    demand_category_click()
    clear_accom = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_48'))
    time.sleep(0.3)
    clear_accom.click()
    click_air = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_47'))
    time.sleep(0.3)
    click_air.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def demand_category_accomm():
    demand_category_click()
    clear_air = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_47'))
    time.sleep(0.3)
    clear_air.click()
    click_accomm = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_48'))
    time.sleep(0.3)
    click_accomm.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#Submit
def submit():
    time.sleep(3)
    submit = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.XPATH,submit_path))
    for i in range(3):
        time.sleep(0.3)
        try:
            submit.click()            
            submit = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.XPATH,submit_path))     
        except:
            break
    time.sleep(10)


#Download
def download_click():
    click_download = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR,download_css_selector))           
    time.sleep(3)
    click_download.click()
    time.sleep(10)


#Primary country click
def primary_country_click():
    country_click = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_30'))
    time.sleep(0.3)
    country_click.click()


def validation_submit():
    while True:
        try:
            time.sleep(3)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,submit_path)))
            print("Click Submit is ready!")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,demand_from_css_selector)))
            break # it will break from the loop once the specific element will be present. 
        except:
            print("Continue to loadingProcess")
            driver.refresh()
            run()


#Select to Primary Country
def primary_country():
    for i in range(2): #len(primary_country_list)
        primary_country_click()
        while True:
            try:
                Country = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,primary_country_id[i]))
                Country.click()
                print('Primary Country is: ' + primary_country_list[i])
                submit()                
                validation_submit()              
                download_click()
                demand_category_air()
                submit()                
                validation_submit()              
                download_click()
                demand_category_accomm()      
                break # it will break from the loop once the specific element will be present.
            except:
                print("Failed to click primary country")
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def run():
    while True:
        try:
            time.sleep(0.3)
            pageReady = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID,'select_30'),'Spain'))
            print("Page is ready!")
            break # it will break from the loop once the specific element will be present. 
        except TimeoutException:
            print("Loading took too much time!-Try again")
            driver.refresh()
    # Select to Initial Process
    for i in range(len(initial_process_list)):
        time.sleep(0.3)
        initial_process = driver.find_element(By.XPATH,initial_process_path[i])
        initial_process.click()
    countries_compare()
    primary_country()
     
if __name__ == '__main__':
    run()
    print("Ready!")