from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url="https://demoqa.com/"
fullname="V.VIGNESHKUMAR"
email="kumarandroid@protonmail.com"
current_address="1/166 NORTH STREET,"
permenant_address="INDIA"
driver.get(url)
driver.maximize_window()
#time.sleep(3)
print("1=website opened")
print(driver.title)
#click elements icon in website
driver.find_element_by_xpath("//*[name()='path' and contains(@d,'M16 132h41')]").click()
#time.sleep(3)

# #text box section
# driver.find_element_by_xpath("//span[normalize-space()='Text Box']").click()
# #time.sleep(4)
# driver.find_element_by_xpath("//input[@id='userName']").send_keys(fullname)
# #time.sleep(2)
# driver.find_element_by_xpath("//input[@id='userEmail']").send_keys(email)
# #time.sleep(2)
# driver.find_element_by_xpath("//textarea[@id='currentAddress']").send_keys(current_address)
# #time.sleep(2)
# driver.find_element_by_xpath("//textarea[@id='permanentAddress']").send_keys(permenant_address)
# #time.sleep(1)
# submit=driver.find_element_by_xpath("//button[normalize-space()='Submit']")
# #actions=ActionChains(driver)
# driver.execute_script("arguments[0].scrollIntoView();",submit)
# driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
# print("ElEMENTS{Text box section completed}")

# #Radio Button section
# driver.find_element_by_xpath("//span[normalize-space()='Radio Button']").click()
# driver.find_element_by_xpath("//label[contains(text(),'Yes')]").click()
# print("yes Radio Button Clicked")
# driver.refresh()
# print("web site refreshed")
# driver.find_element_by_xpath("//label[contains(text(),'Impressive')]").click()
#
# #Web Table section
# driver.find_element_by_xpath("//div[@class='element-list collapse show']//li[@id='item-3']").click()
# print("web tables section opened")
# driver.find_element_by_xpath("//span[@id='delete-record-1']//*[local-name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]").click()
# driver.find_element_by_xpath("//span[@id='delete-record-2']//*[local-name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]").click()
# driver.find_element_by_xpath("//span[@id='delete-record-3']//*[local-name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]").click()
# driver.find_element_by_xpath("//button[normalize-space()='Add']").click()
# #details entering for person 1
# driver.find_element_by_xpath("//input[@id='firstName']").send_keys("VIGNESH")
# driver.find_element_by_xpath("//input[@id='lastName']").send_keys("KUMAR")
# driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("kumarandroid@protonmail.com")
# driver.find_element_by_xpath("//input[@id='age']").send_keys("24")
# driver.find_element_by_xpath("//input[@id='salary']").send_keys("10000")
# driver.find_element_by_xpath("//input[@id='department']").send_keys("SOFTWARE TESTER")
# driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
# driver.find_element_by_xpath("//button[normalize-space()='Add']").click()
# #details entering for person 2
# driver.find_element_by_xpath("//input[@id='firstName']").send_keys("MUTHU")
# driver.find_element_by_xpath("//input[@id='lastName']").send_keys("KUMAR")
# driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("muthuandroid@protonmail.com")
# driver.find_element_by_xpath("//input[@id='age']").send_keys("24")
# driver.find_element_by_xpath("//input[@id='salary']").send_keys("100000")
# driver.find_element_by_xpath("//input[@id='department']").send_keys("DOCTOR")
# driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
# #Re- entering  details for person 2
# driver.find_element_by_xpath("//span[@id='edit-record-2']//*[local-name()='svg']").click()
# depart=driver.find_element_by_xpath("//input[@id='department']")
# depart.click()
# depart.clear()
# depart.send_keys("IAS OFFICER")
# driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
# print("details re-entered successfully")
#
# #BUTTON SECTION OPEN
# button_section=driver.find_element_by_xpath("//span[normalize-space()='Buttons']")
# driver.execute_script("arguments[0].scrollIntoView();",button_section)
# driver.find_element_by_xpath("//span[normalize-space()='Buttons']").click()
# double_click=driver.find_element_by_xpath("//button[normalize-space()='Double Click Me']")
# right_click=driver.find_element_by_xpath("//button[normalize-space()='Right Click Me']")
# single_click=driver.find_element_by_xpath("//button[normalize-space()='Click Me']")
#
# actionchains=ActionChains(driver)
# actionchains.double_click(double_click).perform()
# actionchains.context_click(right_click).perform()
# actionchains.click(single_click).perform()
# print("BUTTON SECTION FINISHED")

# #LINK SECTION OPEN
# link_section=driver.find_element_by_xpath("//div[@class='element-list collapse show']//li[@id='item-5']")
# #commamnd for specified view in the webpage
# driver.execute_script("arguments[0].scrollIntoView();",link_section)
# link_section.click()
# current_window_handle=driver.window_handles
# print(current_window_handle)
# time.sleep(3)
# driver.find_element_by_xpath("//a[normalize-space()='Home']").click()
# time.sleep(2)
# new_windows_handle1=driver.window_handles
# print(new_windows_handle1)
# time.sleep(3)
# driver.switch_to.window(driver.current_window_handle)

# #up-load and download section
#
# upload_down_section=driver.find_element_by_xpath("//span[normalize-space()='Upload and Download']")
# driver.execute_script("arguments[0].scrollIntoView();",upload_down_section)
# upload_down_section.click()
# download_button=driver.find_element_by_xpath("//a[normalize-space()='Download']")
# driver.execute_script("arguments[0].scrollIntoView();",download_button)
# download_button.click()
#
# download_dir=("/home/vigneshkumar/Downloads")
# option=Options()
# option.set_preference("driver.download.folderList",2)
# option.set_preference("browser.download.manager.showWhenStarting", False)
# option.set_preference("driver.download.dir",download_dir)
# option.set_preference("driver.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")



