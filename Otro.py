from sqlite3 import Time
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
primary_country_list = ['Germany','Argentina','Australia','Austria','Belgium','Canada','Czechia','China','Cyprus','Colombia','South Corea','Croatia','Denmark','Egypt','United Arab Emirates','Spain','United States','Finland','France','Greece','India','Ireland','Israel','Italy','Japan','Morocco','Mexico','Norway','Netherlands','Poland','Portugal','United Kingdom','Russia','Sweden','Switzerland','Tunisia','Turkey']
primary_country_id = ['select_option_637','select_option_565','select_option_568','select_option_569','select_option_575','select_option_593','select_option_612','select_option_600','select_option_611','select_option_603','select_option_761','select_option_608','select_option_614','select_option_619','select_option_790','select_option_763','select_option_792','select_option_630','select_option_631','select_option_640','select_option_656','select_option_660','select_option_662','select_option_663','select_option_665','select_option_701','select_option_695','select_option_718','select_option_707','select_option_729','select_option_730','select_option_791','select_option_736','select_option_768','select_option_769','select_option_782','select_option_783']

#Compare to Country Download Process 1
compare_country_list_1 = ['Germany', 'Cyprus', 'Croatia', 'Egypt', 'Spain', 'France', 'Greece', 'Italy', 'Morocco', 'Portugal']
compare_country_id_1 = ['select_option_887', 'select_option_861', 'select_option_858', 'select_option_869', 'select_option_1013', 'select_option_881', 'select_option_890', 'select_option_913', 'select_option_951', 'select_option_980']

#Compare to Country Download Process 2
compare_country_list_2 = ['United Kingdom','Tunisia','Turkey']
compare_country_id_2 = ['select_option_1041', 'select_option_1032','select_option_1033']

#Demand Category
demand_category_list = ['Air','Accommodation']
demand_category_id = ['select_option_47', 'select_option_48']

#Date Range
date_range_list = ['Click','Last 30 days']
date_range_id = ['select_39','select_option_49']



#Countries Compare Click
def countries_compare_click():     
    click_category = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_33'))
    driver.implicitly_wait(3)
    click_category.click()


#Select to Demand Category Click
def demand_category_click():     
    click_category = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_36'))
    driver.implicitly_wait(3)
    click_category.click()


#Primary Country Click
def primary_country_click():
    country_click = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_30'))
    driver.implicitly_wait(3)
    country_click.click()


#Download click
def download_click():
    download = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR,download_css_selector))           
    driver.implicitly_wait(3)
    download.click()
    time.sleep(10)


#Select Countries to Compare Download Process 1
def countries_compare_1():
    countries_compare_click()
    for i in range(len(compare_country_list_1)):
        driver.implicitly_wait(3)
        while True:
            try:      
                countries = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,compare_country_id_1[i]))
                countries.click()
                print('Country to compare is: ' + compare_country_list_1[i])
                break
            except:
                print('Failed to click Countries to Compare')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


#Select Countries to Compare Download Process 2
def countries_compare_2():
    countries_compare_click()
    for i in range(len(compare_country_list_2)):
        driver.implicitly_wait(3)
        while True:
            try:      
                countries = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,compare_country_id_2[i]))
                countries.click()
                print('Country to compare is: ' + compare_country_list_2[i])
                break
            except:
                print('Failed to click Countries to Compare')
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def demand_category_air():
    demand_category_click()
    clear_accom = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_48'))
    driver.implicitly_wait(3)
    clear_accom.click()
    air = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_47'))
    driver.implicitly_wait(3)
    air.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def demand_category_accomm():
    demand_category_click()
    clear_air = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_47'))
    driver.implicitly_wait(3)
    clear_air.click()
    accomm = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_48'))
    driver.implicitly_wait(3)
    accomm.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def date_range():
    for i in range(len(date_range_list)): 
        click_range = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,date_range_id[i]))
        driver.implicitly_wait(3)
        click_range.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


#Submit
def submit():
    submit = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.XPATH,submit_path))
    for i in range(3):
        driver.implicitly_wait(3)
        try:            
            submit.click()            
        except:
            print("Click submit is failed")
            break
    time.sleep(10)


def submit_validation():
    while True:
        try:
            time.sleep(8)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,submit_path)))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,demand_from_css_selector)))            
            break
        except:
            print("Continue to Run")
            driver.refresh()
            download_process_1()
            download_process_2()
print("Click Submit is ready!")


#Download Process 1
def download_process_1():
    page_validation()
    initial_process()
    date_range()
    countries_compare_1()  
    for i in range(len(primary_country_list)): #len(primary_country_list)
        while True:
            try:
                primary_country_click()
                Country = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,primary_country_id[i]))
                time.sleep(0.3)
                Country.click()
                print('Primary Country is: ' + primary_country_list[i])
                submit()                
                submit_validation()              
                download_click()
                print('Download Accom ok: ' + primary_country_list[i]) 
                demand_category_air()
                submit()                
                submit_validation()              
                download_click()
                print('Download Air ok: ' + primary_country_list[i])
                demand_category_accomm()
                break
            except:
                print("Failed to click primary country")
    print('Download Process 1 Ok')


#Download Process 2
def download_process_2():
    driver.refresh()
    page_validation()
    date_range()
    countries_compare_2()   
    for i in range(len(primary_country_list)): #len(primary_country_list)
        while True:
            try:
                primary_country_click()
                Country = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,primary_country_id[i]))
                time.sleep(0.3)
                Country.click()
                print('Primary Country is: ' + primary_country_list[i])
                submit()                
                #submit_validation()            
                download_click()
                print('Download Accom ok: ' + primary_country_list[i]) 
                demand_category_air()
                submit()                
                #submit_validation()           
                download_click()
                print('Download Air ok: ' + primary_country_list[i])
                demand_category_accomm()
                break
            except:
                print("Failed to click primary country")
    print('Download Process 2 Ok')


def page_validation():
    while True:
        try:
            driver.implicitly_wait(3)
            page_ready = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID,'select_30'),'Spain'))
            print("Page is ready!")
            break 
        except TimeoutException:
            print("Loading took too much time!-Try again")
            driver.refresh()


def initial_process():
    for i in range(len(initial_process_list)):
        process = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.XPATH,initial_process_path[i]))        
        driver.implicitly_wait(3)
        process.click()


def load():
    start_time = time.strftime("%H:%M:%S")
    print('Start Time: ' + start_time)
    driver.get('https://destinationinsights.withgoogle.com')
    driver.maximize_window()


def run():
    load()
    download_process_1()
    download_process_2()
    finished()


def finished():
    end_time = time.strftime("%H:%M:%S")
    print('End Time ' + end_time)
    print('Finished Process')


if __name__ == '__main__':
    run()
