import logging
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

# logging
logging.basicConfig(filename='out.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def save_profile_photo(driver, profile_url, alt_text, file_name):

    try:
        driver.get(profile_url)
        driver.implicitly_wait(5)
        logging.info(f"Attempting to access profile: {profile_url}")

        photo = driver.find_element(By.XPATH, f"//img[@alt='{alt_text}' and contains(@class, 'profile-picture__image')]")
        photo_url = photo.get_attribute("src")
        logging.info(f"Profile image URL from {profile_url}: {photo_url}")

        image_data = requests.get(photo_url).content
        with open(file_name, 'wb') as handler:
            handler.write(image_data)
        logging.info(f"Profile image saved as '{file_name}'.")

    except Exception as e:
        logging.error(f"Profile image from {profile_url} not found or access blocked.")
        logging.error(f"Error details: {e}")

# ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    logging.info("Opened LinkedIn login page")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)
    logging.info("Submitted login credentials")
    time.sleep(3)

    profiles = [
        {"url": "https://www.linkedin.com/in/williamhgates", "alt": "Bill Gates", "file_name": "profile_photo_1.jpg"},
        {"url": "https://www.linkedin.com/in/dmytro-skoryi", "alt": "Dmytro Skoryi", "file_name": "profile_photo_2.jpg"},
        {"url": "https://www.linkedin.com/in/schm1tt/?trk=public_profile_browsemap-profile", "alt": "Patrick Schmitt", "file_name": "profile_photo_3.jpg"}
    ]

    for profile in profiles:
        save_profile_photo(driver, profile["url"], profile["alt"], profile["file_name"])

finally:
    driver.quit()
    logging.info("Driver closed")
