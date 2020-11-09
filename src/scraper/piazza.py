from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile

import time
import csv

path = webdriver.FirefoxProfile(r'C:\Users\dukyo\AppData\Roaming\Mozilla\Firefox\Profiles\jcv6d137.scraper')
url = "https://piazza.com/class/kd9bsy3vb5a2v3"
driver = webdriver.Firefox(path)
driver.get(url)

csv_file = open('C:\\Users\\dukyo\\Desktop\\CS\\Fundies Helpers\\fundies-helper-react\\src\\scraper\\piazza_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title'])

# html_source = driver.page_source
# print(html_source)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page_main"))
    )

    time.sleep(1)

    items = main.find_elements_by_class_name('feed_item')

    for item in items:
        title = item.find_element_by_class_name('title_text').text

        csv_writer.writerow([title])

finally:
    csv_file.close()
    driver.quit()

# -----------------------------------------------------------------------------

import pandas as pd

piazza_scrape = pd.read_csv(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\piazza_scrape.csv')
piazza_scrape.dropna(inplace=True)
piazza_scrape.to_csv(r'C:\Users\dukyo\Desktop\CS\Fundies Helpers\fundies-helper-react\src\scraper\piazza_scrape.csv', index=False)
