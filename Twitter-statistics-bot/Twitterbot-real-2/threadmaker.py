from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.common.exceptions import StaleElementReferenceException



import time



class TwitterBot:
    def __init__(self,username,password,message):
        self.username = username
        self.password = password
        args = [
                '--ignore-certificate-errors',
                '--disable-dev-shm-usage',

                '--disable-extensions',
                '--disable-gpu',
                '--no-sandbox',
                ]
        chrome_options = wd.ChromeOptions()
        for arg in args:
            chrome_options.add_argument(arg)
        self.bot = wd.Chrome(options=chrome_options)
        self.bot.set_window_size(1400, 1050)
        self.elements = "elements"
        self.element = "element"
        self.classfind = "classfind"
        self.message = message



    def trytillfail(self,node,request,type):
        attempt = 0
        while attempt != 10:
            try:
                if type == self.elements:
                    return node.find_elements_by_xpath(request)
                if type == self.element:
                    return node.find_element_by_xpath(request)
                if type == self.classfind:
                    node.find_element_by_class_name(request)
            except exceptions.NoSuchElementException:
                continue
            finally:
                attempt+=1
        return False



    def find_postbutton(self,bot):
        try:
            reply = self.trytillfail(bot, ".//div[@data-testid='reply']", self.element)
            if reply != False:
                print("got post")
                self.post_thread(bot,reply)
        except exceptions.NoSuchElementException:
            pass


    def post_thread(self,bot,node):
        ActionChains(bot).move_to_element(node).click(node).perform()
        WebDriverWait(bot, 200, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@aria-label = 'Add emoji']")))
        hello = bot.find_element_by_xpath("//div[@aria-label = 'Add emoji']")
        ActionChains(bot).move_to_element(hello).click(hello).perform()
        WebDriverWait(bot, 200, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@aria-label = 'Grinning face']")))
        emoji = bot.find_element_by_xpath("//div[@aria-label = 'Grinning face']")
        ActionChains(bot).move_to_element(emoji).click(emoji).perform()
        image = bot.find_element_by_xpath("//div[@aria-label = 'Add photos or video']")
        ActionChains(bot).move_to_element(image).click(image).perform()

        WebDriverWait(bot, 200, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'DraftEditor-root']")))
        hello = bot.find_element_by_xpath("//div[@class = 'DraftEditor-root']")
        ActionChains(bot).move_to_element(hello).click(hello).perform()
        ActionChains(bot).send_keys(self.message).perform()
        WebDriverWait(bot, 200, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@data-testid = 'tweetButton']")))
        tweetbutton = bot.find_element_by_xpath("//div[@data-testid = 'tweetButton']")
        try:
            ActionChains(bot).move_to_element(tweetbutton).click(tweetbutton).perform()
            ActionChains(bot).move_to_element(tweetbutton).click(tweetbutton).perform()
            ActionChains(bot).move_to_element(tweetbutton).click(tweetbutton).perform()
        except exceptions.WebDriverException:
            pass
        self.bot.close()


    def bodycode (self,bot):
        self.find_postbutton(bot)


    def login (self,id):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(10)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.get("https://twitter.com/covid_au/status/"+str(id))
        WebDriverWait(bot, 200, ignored_exceptions=[StaleElementReferenceException]).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@data-testid='tweet']")))
        self.bodycode(bot)

