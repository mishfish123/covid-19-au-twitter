import sys
sys.path.insert(0, '/anaconda3/lib/python3.7/site-packages')
import twitter



statistics_bot = ["code"]
def getApi(flag):
    if flag == "statistics":
        return twitter.Api(consumer_key=statistics_bot[0],consumer_secret=statistics_bot[1],access_token_key = statistics_bot[2], access_token_secret= statistics_bot[3])
