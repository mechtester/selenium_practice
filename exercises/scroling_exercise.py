from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
url="https://www.worldometers.info/geography/alphabetical-list-of-countries/"
url1="https://www.google.com/search?channel=fs&client=ubuntu&q=googl"
#url getting
driver.get(url)
#maximize windows
driver.maximize_window()
#scroll by pixcel to specific location
#driver.execute_script("window.scrollBy(0,2000)","")
#scroll by end of the webpage
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time sleep
time.sleep(4)
print("sucess")

