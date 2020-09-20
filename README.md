# The Debug Ducky
A twitter bot that automatically retweets, likes, and replies on matters related to Harvard's CS50 course. The bot is available at [@thedebugducky](https://twitter.com/thedebugducky) on Twitter.

![](https://raw.githubusercontent.com/eduardoltorres/the-debug-ducky/master/the-debug-ducky.png)

## Features & Functionalities
- Automatically retweets:
    * tweets with one or more of the following hashtags: [#CS50](https://twitter.com/hashtag/CS50?src=hashtag_click) or [#CS50x](https://twitter.com/hashtag/CS50x?src=hashtag_click)
    * tweets with one or more of the following words: "CS50" or "CS50x"
    * [@davidjmalan](https://twitter.com/davidjmalan)'s latest tweet, if it hasn't been retweeted already 
    * [@cs50](https://twitter.com/cs50)'s latest tweet, if it hasn't been retweeted already 
- Automatically likes [@davidjmalan](https://twitter.com/davidjmalan)'s and [@cs50](https://twitter.com/cs50)'s latest tweet, if they haven't been liked already.
- Replies in thread to mentions with:
    * a random greeting;
    * or "This is CS50!", if the tweet in which it is mentioned contains the word "CS50".

In addition to the previous functionalities, while the application is running, the application writes to a `.log` file for information and errors. For example, it logs whenever any of the previously mentioned actions is in progress, has been tried, has succeeded or has failed. Even though the application is configured to catch and process all errors, uncaught errors will also be logged.

## Technologies
The bot is built with Python. It uses the Tweepy package to connect to the Twitter API; more specifically, it uses the Cursor and the Stream Listener functionalities. For logging, it uses Python's logging module.
