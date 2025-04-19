from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Configure Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Create CSV file and write the header
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Image URL"])  # CSV Header

    # Loop through 50 pages
    for page in range(1, 16):
        url = f'https://www.noon.com/egypt-en/search?page={page}&q=camera'
        print(f"🔍 Scraping page {page}: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        titles = driver.find_elements(By.CLASS_NAME, "ProductDetailsSection_title__JorAV")
        prices = driver.find_elements(By.CLASS_NAME, "Price_sellingPrice__HFKZf")
        img_urls = driver.find_elements(By.CLASS_NAME, "ProductImageCarousel_productImage__jtsOn")

        # Write each product to the CSV file
        for title, price, img in zip(titles, prices, img_urls):
            writer.writerow([title.text, price.text, img.get_attribute("src")])

print("✅ Done! All data from 15 pages has been saved to products.csv.")
driver.quit()
