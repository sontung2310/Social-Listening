from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("http://facebook.com")

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("0347100825") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("tungtung123")

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5 giây
sleep(5)