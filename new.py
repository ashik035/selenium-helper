from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from bs4 import BeautifulSoup

# Set Chrome options
try:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--enable-javascript')


    # Set the path to the ChromeDriver executable
    webdriver_path = 'C:/chromedriver/chromedriver.exe'

    # Create a new ChromeDriver service
    service = Service(webdriver_path)

    # Create a new ChromeDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the URL
    url = 'https://allegro.pl/listing?string=nike'
    # url = 'https://gmail.com'
    driver.get(url)

    element = driver.find_element(By.XPATH, '//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div/div[2]/button[2]')
    element.click()

    time.sleep(1)
    # Get the page source
    # page_source = driver.page_source

    # # Use BeautifulSoup to parse the HTML
    # soup = BeautifulSoup(page_source, 'html.parser')

    # # Extract the text from the parsed HTML
    # text = soup.get_text()

    # Print the extracted text
    # print(text)



    parent_element = driver.find_element(By.XPATH, '//*[@id="search-results"]/div[5]/div/div/div/div[1]/div/div/div/section[1]/article[2]/div/div/div[1]/div[1]/div')

    # Find all the anchor tags under the parent element
    anchor_tags = parent_element.find_elements(By.TAG_NAME, 'a')

    # Extract the href attribute value of each anchor tag
    href_values = [tag.get_attribute('href') for tag in anchor_tags]

    # Print the href values
    for href in href_values:
        print(href)



except Exception as e:
    print("An error occurred:", str(e))
