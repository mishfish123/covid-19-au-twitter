import sys
sys.path.insert(0, '/anaconda3/lib/python3.7/site-packages')
import twitter



test_bot= ["oB6jL9lgaEPLhPeC2Woy5K4Gq", "X609XEPU7x73hZKoCmy6NUAoVrVkumoSaJSf5vwCoZkQNWfjvS","1245930358920470532-aYFSmht8QRdBTIxUYPL5czJXXItCIH","GERrtEtEv3YCWTP3tJIBv3PXh415badiU4pHo9Q3hyGXu"]
statistics_bot = ["YiqjOkcj3HXOtHReQTCn2sEKN","kH4gnpRuf4wOvO8L19WFh24vAdODVzp7fKFQfh8QTnOWHPM3Cd","1245601545984413698-oFO91891vAdAdG04Bv7ED0SOvaHfzN","kNZdjigOjmv3Nv0wT6S20KVXr02h705jt8pQYdcHB51V6"]
def getApi(flag):
    if flag == "statistics":
        return twitter.Api(consumer_key=statistics_bot[0],consumer_secret=statistics_bot[1],access_token_key = statistics_bot[2], access_token_secret= statistics_bot[3])
