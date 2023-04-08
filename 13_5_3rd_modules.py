import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep



response = requests.get("https://www.google.com/custom", {
    "q": "ramazan",
    "sitesearch": "https://teknolojiaihl.meb.k12.tr"
})

print(response.content)
chrome_install = ChromeDriverManager().install()
print(chrome_install)
chrome_service = Service(chrome_install)
browser = webdriver.Chrome(service=chrome_service)

# Full screen

browser.maximize_window()

# Go to the search address
browser.get("https://www.google.com/custom?q=ramazan&sitesearch=https://teknolojiaihl.meb.k12.tr")
print(browser.title)
browser.find_element(By.XPATH, "//textarea[@name = 'q']").send_keys("ramazan site:https://teknolojiaihl.meb.k12.tr")
browser.get("https://google.com.tr")
sleep(5)