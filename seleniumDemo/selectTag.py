from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/inty/Downloads/chromedriver')
driver.fullscreen_window()
driver.get('https://www.timeanddate.com/')

selectElements = driver.find_element_by_id('month')

months = Select(selectElements)

months.select_by_visible_text('December')

countriesElemets = driver.find_element_by_id('country')

conutries = Select(countriesElemets)

conutries.select_by_visible_text('Taiwan')

driver.find_element_by_xpath("//form[@id='cf']//input[@value='View Calendar']").click()
