# The Debug Ducky

_**Update (March 31st, 2023)**: due to Twitter API's [update on access tiers and pricing](https://twittercommunity.com/t/announcing-new-access-tiers-for-the-twitter-api/188728), The Debug Ducky will remain offline for the time being._

A twitter bot that automatically retweets, likes, and replies on matters related to [Harvard's CS50](https://cs50.harvard.edu/x/2020/) course. The bot is available at [@thedebugducky](https://twitter.com/thedebugducky) on Twitter.

![](https://raw.githubusercontent.com/eduardoltorres/the-debug-ducky/master/the-debug-ducky.png)

## Features & Functionalities
- Automatically retweets:
    * tweets with one or more of the following hashtags: [#CS50](https://twitter.com/hashtag/CS50?src=hashtag_click) or [#CS50x](https://twitter.com/hashtag/CS50x?src=hashtag_click)
    * [@davidjmalan](https://twitter.com/davidjmalan)'s latest tweet, if it hasn't been retweeted already 
    * [@cs50](https://twitter.com/cs50)'s latest tweet, if it hasn't been retweeted already 
- Automatically likes [@davidjmalan](https://twitter.com/davidjmalan)'s and [@cs50](https://twitter.com/cs50)'s latest tweet, if they haven't been liked already.
- Replies in thread to mentions with:
    * a random greeting, if the tweet contains "Hello";
    * or "This is CS50!", if the tweet contains "This is CS50".

In addition to the previous functionalities, while the application is running, the application writes to a `.log` file for information and errors. For example, it logs whenever any of the previously mentioned actions is in progress, has been tried, has succeeded or has failed. Even though the application is configured to catch and process all errors, uncaught errors will also be logged.

## Technologies
The bot is built with Python. It uses the Tweepy package to connect to the Twitter API; more specifically, it uses the Cursor and the Stream Listener functionalities. For logging, it uses Python's logging module. It is hosted in [PythonAnywhere](https://www.pythonanywhere.com/).

## License
Thise project is licensed under the MIT License - see the [LICENSE](https://github.com/eduardoltorres/the-debug-ducky/blob/master/LICENSE) file for details.
