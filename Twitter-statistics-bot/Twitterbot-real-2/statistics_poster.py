from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.firefox.options import Options
from apibuilder import getApi
import json
import locale
from datetime import datetime
from threadmaker import TwitterBot
locale.setlocale(locale.LC_ALL, 'en_US')
locale.format_string("%d", 1255000, grouping=True)

today = str(datetime.today())
api = getApi("statistics")


class statisticsCatcher:
    def __init__(self):
        args = [
            '--ignore-certificate-errors',
            '--disable-dev-shm-usage',

            '--disable-extensions',
            '--disable-gpu',
            '--no-sandbox',
            '--headless',
        ]
        chrome_options = wd.ChromeOptions()
        for arg in args:
            chrome_options.add_argument(arg)
        self.bot = wd.Chrome(options=chrome_options)
        self.bot.set_window_size(1400, 1050)

    def catchdata (self):
        bot = self.bot
        bot.get('https://covid-19-au.com/')
        bot.save_screenshot("screenshot.png")
        WebDriverWait(bot, 200, ignored_exceptions=[StaleElementReferenceException]).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='number']")))
        numbers = bot.find_elements_by_xpath("//div[@class='number']")
        confirmed = "{:0,.0f}".format(int(numbers[0].text.rstrip("+")))
        deaths = "{:0,.0f}".format(int(numbers[1].text.rstrip("+")))
        recovered = "{:0,.0f}".format(int(numbers[2].text.rstrip("+")))
        tested = "{:0,.0f}".format(int(numbers[3].text.rstrip("+")))
        self.postdata(confirmed,deaths,recovered,tested)


    def postdata (self,confirmed,deaths,recovered,tested):
        string = "\U0001F4E2 Current COVID-19 numbers in Aus\U0001F998 \n"+"\n\U0001F912 "+confirmed+" cases\n"+"\u2620 "+deaths+" de$
        furtherbuild = string+"\n"+"Visit covid-19-au.com for:\n"+"\U0001F1E6\U0001F1FA State case maps\n"+"\U0001F4CA data trends\n"$
        job = api.PostUpdate(furtherbuild, media="screenshot.png")
        self.bot.close()

ed = statisticsCatcher()
ed.catchdata()
