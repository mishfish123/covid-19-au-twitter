import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver as wd
from datetime import datetime
import time


def run():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("secret-rope-273113-a2da891cdc1e.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Daily").sheet1  # Open the spreadsheet
    new_confirmed = []
    new_tested = []
    new_states = []

    # get old states and confirmed testing values stats
    old_states = sheet.col_values(3)[3:]
    old_confirmed_values = sheet.col_values(4)[3:]
    old_testing_values = sheet.col_values(11)[3:]
    old_death_total = sheet.cell(4, 15).value

    # get data from website


    bot = wd.Firefox()
    bot.get('https://covid-19-au.com/')
    bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)
    state_elements = bot.find_elements_by_xpath("//div[@class='area']")
    confirmed_elements = bot.find_elements_by_xpath("//div[@class='confirmed']//strong")
    tested_elements = bot.find_elements_by_xpath("//div[@class='tested']")
    # extract data and add into lists

    new_death_total = bot.find_elements_by_xpath("//div[@class='number']")[1].text
    for states in state_elements:
        new_states.append(states.text.strip('\n '))

    print(new_states)

    for confirmed in confirmed_elements:
        if confirmed.text.find("(")== -1:
            new_confirmed.append(confirmed.text.strip('\n '))
    print(new_confirmed)

    for testcase in tested_elements:
        if testcase.text.find("(")== -1:
            new_tested.append(testcase.text.strip('\n '))
    print(new_tested)


    # get time from website
    current_time = str(datetime.today())
    previous_time = sheet.cell(18, 13).value

    #swap previous values to old columns

    for i in range(8):
        sheet.update_cell(i+4,1, old_states[i])
        sheet.update_cell(i+4,2, old_confirmed_values[i])

    for i in range(8):
        sheet.update_cell(i+4,8, old_states[i])
        sheet.update_cell(i+4,9, old_testing_values[i])

    # Add new states and new columns


    for i in range(8):
        sheet.update_cell(i+4,3, new_states[i])
        sheet.update_cell(i+4,4, new_confirmed[i])

    for i in range(8):
        sheet.update_cell(i+4,10, new_states[i])
        sheet.update_cell(i+4,11, new_tested[i])


run()