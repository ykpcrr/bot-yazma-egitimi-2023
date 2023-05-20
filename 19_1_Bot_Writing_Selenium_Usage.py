# Selenium webdriver import
from selenium import webdriver

# import chrome service in selenium chrome
from selenium.webdriver.chrome.service import Service

# The ChromeDriverManager in the web driver manager,
# which will check and manage the chrome webriver versions, is imported
from webdriver_manager.chrome import ChromeDriverManager

# import sleep to slow down the speed
from time import sleep

# chrome driver install
chrome_driver = ChromeDriverManager().install()

# chromes service is created
chrome_service = Service(chrome_driver)

# browser object is created and browser is created
driver = webdriver.Chrome(service=chrome_service)
sleep(1)

# Get browser size and set a new one
print(driver.get_window_size())
driver.set_window_size(500, 300)
sleep(1)

# Get browser position and set a new one
print(driver.get_window_position())
driver.set_window_size(500, 500)
sleep(1)

# minimize window
driver.minimize_window()
sleep(1)


# Fullscreen mode
driver.fullscreen_window()
sleep(1)

# maximize command
driver.maximize_window()
sleep(1)

# this is our adress
driver.get("https://teknolojiaihl.meb.k12.tr/")
sleep(1)

# refresh the page
driver.refresh()
sleep(1)

# save a screenshot
driver.save_screenshot("./images/taihl.png")

# go to a new address
driver.get("https://google.com.tr")

# get back

driver.back()
sleep(1)

# go forward
driver.forward()
sleep(1)


# Close browser after all done
driver.quit()
