from selenium import webdriver

driver = webdriver.Chrome('/Users/inty/Downloads/chromedriver')
driver.fullscreen_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('this is Inty,youtube demo 大家好')

driver.save_screenshot('/Users/inty/desktop/截图.png')

driver.close()



# this is code from another coworker
# def ........


