#!/usr/bin/env python
import sys
sys.path.insert(0, '/anaconda3/lib/python3.7/site-packages')
from apscheduler.schedulers.background import BackgroundScheduler
import twitter

#enter your credentials here.
statistics_bot = ["credentials"]
api = twitter.Api(consumer_key=statistics_bot[0],consumer_secret=statistics_bot[1],access_token_key = statistics_bot[2], access_token_secret= statistics_bot[3])

def my_job(status=None):
    job = api.PostUpdate(build)

def daily_summary(status=None):
    run()


build = "Good morning everybody!☀️ Remember to take some time out of ur busy schedule to catch up on the latest COVID-19 developments written by us, yesterday late at night! 🌜😴. Also, remember to check out the latest COVID-19 numbers at https://covid-19-au.com! https://twitter.com/covid19augithub/status/1252952546919854087"


sched = BackgroundScheduler()
job = sched.add_job(my_job, 'interval', hours=7)
sched.start()
input("Press enter to exit.")
sched.shutdown()
