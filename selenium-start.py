from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Options = Options()
Options.chrome_executable_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=Options)
driver.maximize_window()
#driver.get("https://www.google.com")
#driver.save_screenshot("google.png")
driver.get("https://dtm.stu.edu.tw/")
driver.save_screenshot("stu.png")
driver.close
