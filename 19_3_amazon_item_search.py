from module.browser import Browser

driver = Browser(True).get()

# Move to amazon page

driver.get("https://www.amazon.com.tr/")
print(driver.current_url)
print(driver.title)