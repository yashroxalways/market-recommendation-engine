from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (replace 'chromedriver' with the path to your WebDriver)
driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs')

try:
    # Open Google
    driver.get("https://www.google.com")

    # Locate the search box, enter a query, and press ENTER
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("OpenAI ChatGPT")
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(2)

    # Get and print titles of search results
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for idx, result in enumerate(results[:5], start=1):  # Limit to first 5 results
        print(f"{idx}. {result.text}")

finally:
    # Close the browser
    driver.quit()
