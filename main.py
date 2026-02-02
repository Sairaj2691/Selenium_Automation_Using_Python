from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pdb
import time

options = Options()
options.add_argument("--start-maximized")
website = "https://www.investec.com"

driver = webdriver.Chrome(options=options)
# driver.get("https://www.google.com")
#
# print(driver.title)
#

driver.get(website)
driver.implicitly_wait(10)
time.sleep(5)
#pdb.set_trace()

accept_button = driver.find_element(By.XPATH, "//button[text()='Accept all cookies']")
if (accept_button.is_displayed()):
    accept_button.click()

# Locators
close_alert = driver.find_element(
    By.XPATH,
    "//div[@class='alerts-popup__container']/div[@class='alerts-popup__close js-alerts-close']"
)
close_alert.click()


assert driver.current_url == 'https://www.investec.com/en_in.html','PASS'
location = driver.find_element(By.XPATH, "(//button[@class='territory-selector-dropdown-toggle']/div/div)[2]")
assert location.text == "India"

about_us = driver.find_element(By.XPATH, '//a[@title="About us"]')
about_us.click()

# explicit wait for find out more
find_out_more = driver.find_element(By.XPATH, "//span[text()='Find out more']")
find_out_more.click()

# define wait for page load mothod
header = driver.find_element(By.XPATH, '//h1[text()="Welcome to Investec"]')
assert header.text == 'Welcome to Investec'

our_history = driver.find_element(By.XPATH, "//span[contains(text(), 'Explore our history')]")
our_history.click()

gif = driver.find_element(By.XPATH, "//img[contains(@alt,'50 year')]")
assert gif.is_displayed()

#pdb.set_trace()
frame_switch = driver.find_element(By.XPATH, "//iframe[@title='Interactive or visual content']")
driver.switch_to.frame(frame_switch)
element_to_see = driver.find_element(By.XPATH, "//p[starts-with(normalize-space(text()), '1988')]")
driver.execute_script("arguments[0].scrollIntoView(true);", element_to_see)
time.sleep(5)
assert element_to_see.is_displayed()
text = element_to_see.text
print(text)

driver.quit()
