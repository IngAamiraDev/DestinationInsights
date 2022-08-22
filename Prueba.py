import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(".\chromedriver\chromedriver.exe")

driver.get('https://destinationinsights.withgoogle.com/')

driver.maximize_window()
driver.implicitly_wait(10)

exp_countries = ['Argentina']
act_countries = []

click_cookieBar = driver.find_elements_by_xpath('/html/body/div[2]/div[24]/div[1]/div/div[5]/button').click()

select_primaryCountry = Select(driver.find_element_by_id("select_30"))

click_search = driver.find_elements_by_xpath('//*[@id="cookieBar"]/div/span[2]/a[2]').click()
