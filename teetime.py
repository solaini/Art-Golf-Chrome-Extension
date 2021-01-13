from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import pause
from datetime import datetime

# Initiate the browser
#browser = webdriver.Chrome('/usr/local/bin/chromedriver')
#browser  = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=options)

# Browser Test
#browser.get('https://www.google.com/')

# ======= Setting =============
# Your Mediterra credentials
med_name = "ajuedes"
med_pass = "Southbay1"
# =============================
# Open the Website
browser.get('https://www.mediterraliving.com/Club/Login/')
# click on Log in with Mediterra
#browser.find_element_by_class_name('MyProfile_Name').click()
# =============================
# Filling in the Mediterra Credentials
browser.find_element_by_name("p$lt$ContentWidgets$pageplaceholder$p$lt$zoneContent$CHO_Widget_LoginFormWithFullscreenBackground_XLarge$loginCtrl$BaseLogin$UserName").send_keys(med_name)
browser.find_element_by_name("p$lt$ContentWidgets$pageplaceholder$p$lt$zoneContent$CHO_Widget_LoginFormWithFullscreenBackground_XLarge$loginCtrl$BaseLogin$Password").send_keys(med_pass)
# Click on the Mediterra log-in button
browser.find_element_by_id('p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_LoginButton').click()
# =============================
#Migrate to Foretees
browser.find_element_by_id('p_lt_ContentWidgets_pageplaceholder_p_lt_zoneSM30_CHO_Widget_QuickLinkMenu_Small_rptItems_ctl03_hrefLink').click()
#==============================
#Foretees Actions
#Go to Foretees Tee times
#browser.find_element_by_xpath('//a[@href="Member Select"]').click()
browser.find_element_by_xpath('//a[@href="https://www1.foretees.com/v5/mediterra_golf_m32/Member_select"]')
#browser.get("https://www1.foretees.com/v5/mediterra_golf_m32/Member_select") 

topnav = browser.find_element_by_xpath("//class='topnav_item'")
subMenu = browser.find_element_by_xpath("//li[@class='topnav_item']//a[@href='#']")
course = browser.find_element_by_xpath("//a[@href='Member Portal'")
action = ActionChains(browser)
action.move_to_element(topnav).perform()
action.move_to_element(subMenu).perform()
action.move_to_element(course).click().perform()


#Select dropdown = new Select(driver.findElement(By.id("testingDropdown")));  
#dropdown.selectByVisibleText("Database Testing");  



# click shirt
#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-nav-tracking=men] a[data-subnav-label$=Shirts]"))).click()

#Wait until