from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = 'suk7707ss'
pwd = 'ryqhansrh22'

path = "C:/Users/suk93/Desktop/project/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)
driver.get("http://www.kyobobook.co.kr/login/login.laf")

# assert "KYOBO" in driver.title

elem = driver.find_element_by_id("memid")
elem.send_keys(usr)
elem = driver.find_element_by_id("pw")
elem.send_keys(pwd)
# elem.send_keys(Keys.RETURN)