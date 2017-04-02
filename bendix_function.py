import time
import zipcode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


def init_driver(filepath):
    driver = webdriver.Chrome(executable_path = filepath)
    driver.wait = WebDriverWait(driver, 10)
    return(driver)
def navigate_to_website(driver, site):
    driver.get(site)
def select_data(driver,search_car, search_type_of_car):
    Select(driver.find_element_by_id("edit-manufacturer")).select_by_visible_text(search_car)
    Select(driver.find_element_by_id("edit-model")).select_by_visible_text(search_type_of_car)
def get_html(driver):
    output = driver.find_element_by_id("scrollableTable")
    return output
