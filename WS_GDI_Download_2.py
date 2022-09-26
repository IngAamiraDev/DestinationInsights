from selenium import webdriver #Se usa para el driver de Selenium con Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Esperas explícitas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import glob
import collections


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r".\chromedriver\chromedriver.exe")
submit_path = '/html/body/div[1]/div[24]/div[1]/div/div[5]/button'
download_css_selector = 'body > div:nth-child(2) > div.glue-mod-spacer-6-bottom.glue-mod-spacer-6-top > div.compare.glue-mod-spacer-5-bottom > div > div.demand__from > div.charts__header > div > svg.geographic-demand__export.ng-scope > use'
demand_from_css_selector = 'body > div:nth-child(2) > div.glue-mod-spacer-6-bottom.glue-mod-spacer-6-top > div.compare.glue-mod-spacer-5-bottom > div > div.demand__from > div.demand__from--canva > svg'
demand_from_css_selector_initial = 'body > div:nth-child(3) > div.glue-mod-spacer-6-bottom.glue-mod-spacer-6-top > div.compare.glue-mod-spacer-5-bottom > div > div.demand__from > div.demand__from--canva'

#Initial Process
initial_process_list = ['Cookies','FlightAccommodation']
initial_process_path = ['//*[@id="cookieBar"]/div/span[2]/a[2]','/html/body/div[1]/div[24]/div[2]/div/div[1]/div[1]/p']

#Primary Country
primary_country_name = ['Germany','Argentina','Australia','Austria','Belgium','Canada','Czechia','China','Cyprus','Colombia','South Corea','Croatia','Denmark','Egypt','United Arab Emirates','Spain','United States','Finland','France','Greece','India','Ireland','Israel','Italy','Japan','Morocco','Mexico','Norway','Netherlands','Poland','Portugal','United Kingdom','Russia','Sweden','Switzerland','Tunisia','Turkey']
primary_country_id = ['select_option_637','select_option_565','select_option_568','select_option_569','select_option_575','select_option_593','select_option_612','select_option_600','select_option_611','select_option_603','select_option_761','select_option_608','select_option_614','select_option_619','select_option_790','select_option_763','select_option_792','select_option_630','select_option_631','select_option_640','select_option_656','select_option_660','select_option_662','select_option_663','select_option_665','select_option_701','select_option_695','select_option_718','select_option_707','select_option_729','select_option_730','select_option_791','select_option_736','select_option_768','select_option_769','select_option_782','select_option_783']
primary_country_cod = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']

#Compare to Country Download Process 2
compare_country_name_2 = ['United Kingdom','Tunisia','Turkey']
compare_country_id_2 = ['select_option_1041', 'select_option_1032','select_option_1033']

#Demand Category
demand_category_list = ['Air','Accommodation']
demand_category_id = ['select_option_47', 'select_option_48']

#Date Range
date_range_list = ['Click','Last 30 days']
date_range_id = ['select_39','select_option_49']

file_source = 'C:\\Users\\user\\Downloads\\'
file_flight = 'C:\\Users\\user\\Downloads\\Vuelos'
file_accomm = 'C:\\Users\\user\\Downloads\\Alojamientos'


def load():
    start_time = time.strftime("%H:%M:%S")
    start_date = time.strftime("%d/%m/%Y")
    print('Download process 2 started: ' + start_date + ' ' + start_time)
    driver.get('https://destinationinsights.withgoogle.com')
    driver.maximize_window()


def page_validation(j):
    i = 1
    while True:
        try:
            driver.implicitly_wait(3)
            page_ready = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID,'select_30'),'Spain'))
            if (j == 1):
                graphics_ready = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,demand_from_css_selector_initial)))
            else:
                graphics_ready = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,demand_from_css_selector)))
            if ((page_ready == True) and (graphics_ready != any)):
                print("Page is ready!")
            break
        except:
            i += 1
            if (i == 8):
                print("Loading took too much time!-try again")     
                driver.close()                
                print('Try again later')
                exit()
    print('Finish page validation')


def initial_process():
    for i in range(len(initial_process_list)):
        process = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.XPATH,initial_process_path[i]))        
        driver.implicitly_wait(3)
        process.click()
        time.sleep(0.05)


def date_range():
    for i in range(len(date_range_list)): 
        click_range = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,date_range_id[i]))
        driver.implicitly_wait(3)
        click_range.click()
        time.sleep(0.05)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


#Countries Compare Click
def countries_compare_click():     
    click_category = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_33'))
    driver.implicitly_wait(3)
    click_category.click()
    time.sleep(0.05)


#Select to Demand Category Click
def demand_category_click():
    click_category = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_36'))
    driver.implicitly_wait(3)
    click_category.click()
    time.sleep(0.05)


#Primary Country Click
def primary_country_click():
    country_click = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_30'))
    driver.implicitly_wait(3)
    country_click.click()
    time.sleep(0.05)


#Download click
def download_click():
    download = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR,download_css_selector))           
    driver.implicitly_wait(3)
    download.click()
    print('Download process ok')
    time.sleep(10)


#Select Countries to Compare Download Process 2
def countries_compare_2():
    countries_compare_click()
    print('Country to compare is:')
    for i in range(len(compare_country_name_2)):
        driver.implicitly_wait(3)
        while True:
            try:      
                countries = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,compare_country_id_2[i]))
                countries.click()
                print(compare_country_name_2[i])
                break
            except:
                pass
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def demand_category_air():
    demand_category_click()
    clear_accom = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_48'))
    driver.implicitly_wait(3)
    clear_accom.click()
    time.sleep(0.05)
    air = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_47'))
    driver.implicitly_wait(3)
    air.click()
    time.sleep(0.05)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def demand_category_accomm():
    demand_category_click()
    clear_air = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_47'))
    driver.implicitly_wait(3)
    clear_air.click()
    time.sleep(0.05)
    accomm = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select_option_48'))
    driver.implicitly_wait(3)
    accomm.click()
    time.sleep(0.05)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


#Submit
def submit():
    time.sleep(3)
    submit = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.XPATH,submit_path))
    driver.implicitly_wait(3)
    submit.click()
    time.sleep(10)


def submit_validation(x):
    while True:
        try:
            time.sleep(6)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,submit_path)))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,demand_from_css_selector)))            
            break
        except:
            print("Continue to run")
            driver.refresh()
            page_validation(2)
            status()
            download_process_2(x)
    print("Click submit is ready!")


def delete_last_file():
    get_files = os.listdir(file_source)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    if len(accom_csv) > len(flight_csv):
        files_path = os.path.join(file_source, '*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        os.remove(files[0])
    elif len(flight_csv) > len(accom_csv):
        files_path = os.path.join(file_source, '*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        os.remove(files[0])
    else: 
        pass


def extract_cod_country(list):
        if len(list) == 47:
            return list[28:-17]
        else:
            return list[28:-24]


def len_country_missing():
    get_files = os.listdir(file_source)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [i for i in primary_country_cod if i not in download_file]    
    kick_off = len(primary_country_name) - len(download_missing)
    return kick_off


def download_status():
    get_files = os.listdir(file_source)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [i for i in primary_country_cod if i not in download_file]
    if (collections.Counter(download_file) == collections.Counter(primary_country_cod)):
        print('Download process 2 Ok')
    else:
        print('Downloaded countries: ' + str(download_file))
        print('Pending countries: ' + str(download_missing))


def status():
    delete_last_file()
    download_status()


def finished():
    end_time = time.strftime("%H:%M:%S")
    end_date = time.strftime("%d/%m/%Y")
    print('Finished process download 2: ' + end_date + ' ' + end_time)
    driver.close()


#Download Process 2
def download_process_2(x):
    date_range()
    countries_compare_2()
    print('Primary Country is:')
    for i in range(x,len(primary_country_name)):
        while True:
            try:
                primary_country_click()
                Country = WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,primary_country_id[i]))
                time.sleep(0.3)
                Country.click()
                print(primary_country_name[i])
                demand_category_air()
                submit() 
                submit_validation(x)         
                download_click()
                demand_category_air()
                submit()               
                submit_validation(x)              
                download_click()
                demand_category_accomm()
                x += 1
                break
            except:
                print("Failed to primary country")
                if (x < len(primary_country_name)):
                    driver.refresh()
                    page_validation(2)
                    status()
                    download_process_2(x)
                    exit()
    print('Process 2 Ok')


def run():
    load()
    page_validation(1)
    initial_process()
    status()
    download_process_2(x = len_country_missing())
    finished()


if __name__ == '__main__':   
    run()