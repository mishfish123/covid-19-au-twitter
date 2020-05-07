__Description__: 

An promotional twitter bot which scrapes the website covid-19-au.com for basic statistics about the development of COVID-19 in Australia. 

__Credits__: 
I would like to thank the following code examples which helped me assemble this bot: 

* https://github.com/mcyph/covid_19_au_grab for giving me the right attributes to solve my  headless selenium chrome problems
* https://github.com/superjke/twitter-bot/blob/master/TwitterBot.py giving the idea and template code to scrape the website (as well as make the thread maker, which however, didn't make it to production because twitter blocked login in)
* https://github.com/joyzoursky/docker-python-chromedriver for the docker image, which allowed me to seamlessly put my code onto a EC2 instance, so it was free to use!
* https://gist.github.com/glamp/74188691c91d52770807 shows you how to modify docker files 

__How to run the bot on a cloud server__:

1. docker run -it -w /usr/workspace -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:3.7 bash
2. run pip install selenium
3. run pip install python-twitter
4. exit the bash terminal
5. find the container id by running docker ps -a
6. run docker commit [options] [container ID] twitterbot-python:1
7. set up a cron job and run twitter.sh every hour (alter repository:tag)

__Experimental__:

threadmaker.py :uses selenium and emoji to make threads on twitter. 



