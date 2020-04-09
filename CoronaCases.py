import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.worldometers.info/coronavirus/country/us/"
# url = "https://www.worldometers.info/coronavirus/country/india/"

us_cases = 0
us_deaths = 0
us_recovered = 0

while True:

    is_updated = False

    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    all_numbers = soup.find_all('div', class_='maincounter-number')

    for index, x in enumerate(all_numbers):
        y = x.get_text().strip()
        if index == 0:
            if us_cases != y:
                is_updated = True
                us_cases = y
        elif index == 1:
            if us_deaths != y:
                is_updated = True
                us_deaths = y
        elif index == 2:
            if us_recovered != y:
                is_updated = True
                us_recovered = y
    if is_updated:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), us_cases, us_deaths, us_recovered)

    time.sleep(300)
