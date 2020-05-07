
Description: 


A simple script which automates the transfer of data from the website https://covid-19-au.com/ to a google spreadsheet. 
Then in a semi-automated way, google sheets can be used to quickly transfer data to psd files.

Example work shown at: 

https://twitter.com/covid19augithub/status/1258013461511991297/photo/1
https://www.facebook.com/photo?fbid=132870975029156&set=a.105117371137850


How to use 

Follow this tutorial to set up the google sheet:  https://www.youtube.com/watch?v=cnPlKLEGR7E 

1) Download json file to store credentials for google drive and also enable google sheets API. 
2) Paste email from credentials into google sheet 
3) pip install gspread oauth2client
4) run the daily_summary.py  module 
5) sort today's state statistics in alphabetical order using google's sort function 
6) manually update today and yesterday's death totals to sheet1. 
7) manually update national annoucements on total sheet (National, or the last cell). 
8) manually update each state annoucements on "annoucement - facebook" sheet 
9) download confirmed, testing, total, announcements-facebook, twitter1 and twitter2 sheets as csv files. 
10) open each photoshop file. 
11) go to image > variables > datasets > import.. then select the csv file that serves as the dataset of each page ,then press apply. 

  Daily - total.csv = dailyreport-1.psd
  Daily - annoucements - facebook.csv = dailyreport-2.psd
  Daily - confirmed.csv = dailyreportsmall-confirmed.psd
  Daily - testing.csv = dailyreportsmall-tested.psd
  Daily - twitter1.csv = Twitter-1.psd
  Daily - twitter2.csv = twitter-1.psd

  12) adjust arrows and change plus signs. 
  13) export each psd file as a pdf. 
