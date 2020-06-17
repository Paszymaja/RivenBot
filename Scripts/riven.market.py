import time
from dataclasses import dataclass

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def wait_until_loaded():
    while True:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        loading_elem = soup.find_all('center')
        time.sleep(0.05)
        if not loading_elem:
            break


def web_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options, executable_path='data/driver/chromedriver.exe')
    driver.get('https://riven.market/list/PC')

    wait_until_loaded()

    return webdriver


@dataclass
class Weapon:
    name: str
    stats = []
    errors = []


class Rivenmarket:
    def __init__(self, weapon):
        self.web_driver = web_driver()
        self.weapon = weapon
