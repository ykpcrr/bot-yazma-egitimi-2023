from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Build the browser in one line
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# go to our internet page
driver.get("https://teknolojiaihl.meb.k12.tr/")
driver.maximize_window()

# Select a Dom with id
element = driver.find_element(By.ID, "araTextBox")

# print some values of element
print(element.text)
print(element.id)

# Get attributes

print(element.get_attribute("type"))

# Get screenshot of element
element.screenshot("./images/taihl_arama.png")

# Enter a value to input
element.send_keys("Hello World")
sleep(1)

# Clear the value
element.clear()
element.send_keys("teknoloji")

# select a dom with name
driver.find_element(By.NAME, "sa2").click()  # opens in a new page
sleep(1)

# Go to the page
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])  # moved to the last tab opened
print(tabs)

# Select the elements on the web page with the tag name

h3s = driver.find_elements(By.TAG_NAME, "h3")
print(h3s)
for h3 in h3s:
    print(h3.text)

# get back to first page

driver.switch_to.window(tabs[0])

# Select the elements on the web page with the class name
print(driver.find_elements(By.CLASS_NAME, "menu-item"))

# Select the elements on the web page with the Css selector
menu_items = driver.find_elements(By.CSS_SELECTOR, "li.menu-item")
for menu_item in menu_items:
    print(menu_item.get_attribute("class"))
    if "dropdown" in menu_item.get_attribute("class"):
        menu_item.click()
    # Select element in web page with xpath
    try:
        menu_link = menu_item.find_element(By.XPATH, "./a[@href!='#' and @href!='']")
        print(menu_link.get_attribute("href"))
    except:
        pass

# Select element in web page with link text
meb_link = driver.find_element(By.LINK_TEXT, "444 0 MEB")

# Events with actionsChains
ActionChains(driver).key_down(Keys.CONTROL).click(meb_link).key_up(Keys.CONTROL).perform()
sleep(2)

# Select elements with partial link text in our web page

links = driver.find_elements(By.PARTIAL_LINK_TEXT, "MEB")
for link in links:
    print(link.get_attribute("href"))
# Close browser
driver.close()
