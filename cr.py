from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("user-data-dir=C:\\use_data\\insta1")
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

url = 'https://www.instagram.com/'
driver.get(url)


time.sleep(5)

# 웹 페이지 열기
url = 'https://www.instagram.com/katarinabluu/'  # 테스트용 URL
driver.get(url)
time.sleep(5)

elem = driver.find_element(By.CLASS_NAME, '_aagu')
elem.click()
time.sleep(3)


love = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.x1rg5ohu.xp7jhwk .x1ypdohk [role="button"]'))
)
driver.execute_script("arguments[0].click();", love)


input("Press Enter to close the browser...")
driver.quit()


