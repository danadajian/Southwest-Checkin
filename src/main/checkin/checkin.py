from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

path = '/opt/python/lib/python3.7/site-packages/'
url = 'https://mobile.southwest.com/check-in'


def handler(input, context):
    options = Options()
    options.binary_location = path + 'headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(path + 'chromedriver', chrome_options=options)
    driver.get(url)

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, 'recordLocator')))
    recordLocator = driver.find_element_by_name('recordLocator')
    firstName = driver.find_element_by_name('firstName')
    lastName = driver.find_element_by_name('lastName')
    retrieveReservationButton = driver.find_element_by_css_selector('button')

    recordLocator.send_keys(input.get('recordLocator'))
    firstName.send_keys(input.get('firstName'))
    lastName.send_keys(input.get('lastName'))
    retrieveReservationButton.click()

    try:
        WebDriverWait(driver, 10).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'button'), 'Check in'))
        checkInButton = driver.find_element_by_css_selector('button')
        checkInButton.click()
    except TimeoutException:
        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'popup')))
        except TimeoutException:
            return 'Something went wrong.'
        return driver.find_element_by_class_name('popup-title').text

    WebDriverWait(driver, 20).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'button'), 'View boarding pass'))
    driver.close()
    driver.quit()
    return 'Successfully checked in!'
