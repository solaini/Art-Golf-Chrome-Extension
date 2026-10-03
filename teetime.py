import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pause
from datetime import datetime

# Initiate the browser
# Selenium Manager (built into Selenium 4.6+) downloads a matching chromedriver automatically.
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)

# ======= Setting =============
# Your Mediterra credentials, read from the environment so they are never committed:
#   export MEDITERRA_USER=... MEDITERRA_PASS=...
med_name = os.environ["MEDITERRA_USER"]
med_pass = os.environ["MEDITERRA_PASS"]
# =============================
# Open the Website
browser.get('https://www.mediterraliving.com/Club/Login/')
# =============================
# Filling in the Mediterra Credentials
browser.find_element(By.NAME, "p$lt$ContentWidgets$pageplaceholder$p$lt$zoneContent$CHO_Widget_LoginFormWithFullscreenBackground_XLarge$loginCtrl$BaseLogin$UserName").send_keys(med_name)
browser.find_element(By.NAME, "p$lt$ContentWidgets$pageplaceholder$p$lt$zoneContent$CHO_Widget_LoginFormWithFullscreenBackground_XLarge$loginCtrl$BaseLogin$Password").send_keys(med_pass)
# Click on the Mediterra log-in button
browser.find_element(By.ID, 'p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_LoginButton').click()
# =============================
#Migrate to Foretees
browser.find_element(By.ID, 'p_lt_ContentWidgets_pageplaceholder_p_lt_zoneSM30_CHO_Widget_QuickLinkMenu_Small_rptItems_ctl03_hrefLink').click()
#==============================
#Foretees Actions
#Go to Foretees Tee times
browser.find_element(By.XPATH, '//a[@href="https://www1.foretees.com/v5/mediterra_golf_m32/Member_select"]')

topnav = browser.find_element(By.XPATH, "//li[@class='topnav_item']")
subMenu = browser.find_element(By.XPATH, "//li[@class='topnav_item']//a[@href='#']")
course = browser.find_element(By.XPATH, "//a[@href='Member Portal']")
action = ActionChains(browser)
action.move_to_element(topnav).perform()
action.move_to_element(subMenu).perform()
action.move_to_element(course).click().perform()

#Wait until
