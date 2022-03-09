from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

E_MAIL = 'YOUR MAIL'
PASSWORD = 'YOUR PASSWORD'

chrome_driver_path = 'chromedriver--path'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


tinder_url = 'https://tinder.com/app/recs'
driver.get(tinder_url)

base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

login = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                                     'div/div[2]/div[2]/button')
login.click()

try:
    time.sleep(2)
    facebook = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    # print(facebook.text)
    facebook.click()

except NoSuchElementException:
    time.sleep(2)
    more = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/button')
    more.click()

time.sleep(1)
facebook = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[2]/button')
# print(facebook.text)
facebook.click()

fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

email = driver.find_element_by_id('email')
email.send_keys(E_MAIL)

password = driver.find_element_by_id('pass')
password.send_keys(PASSWORD)

enter = driver.find_element_by_id('loginbutton')
enter.click()

time.sleep(2)
continue_window = driver.window_handles[2]
driver.switch_to.window(continue_window)
continue_as_purush = driver.find_element_by_xpath('//*[@id="u_0_4_bI"]/div[2]/div[2]/div[1]/button')
continue_as_purush.click()
