import tweepy
from time import time, sleep
from api_config import create_api
from logger_config import logger
from random import randrange

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.retweeted and status.user.screen_name != "thedebugducky":
            try:
                status.retweet()
                logger.info(f"RT successful from @{status.user.screen_name}. Status ID: {status.id}.")
            except tweepy.TweepError as e:
                if e.args[0][0]['code'] == 327:
                    logger.info(f"Tweet from @{status.user.screen_name} already RT'd.")
                else:
                    logger.error(f"Error {e} on listener.", exc_info=True)

    def on_error(self, status_code):
        if status_code == 420:
            logger.error(f"Error {status_code} on listener.", exc_info=True)
            return False
        else:
            logger.error(f"Error {status_code} on listener.", exc_info=True)

def reply_to_mentions(api, since_id):
    recent_since_id = since_id
    replies = ["Hi there! The debugging ducky here. How can I help you? 8)",
                "Hiya! How's it going? :)",
                "Did you just call The Debug Ducky?",
                "Hey there! How can I help?",
                "Quack, quack!!!"]
    for status in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        random_idx = randrange(5)
        recent_since_id = max(status.id, recent_since_id)
        if "this is cs50" in status.text.lower():
            logger.info(f"Replying 'This is CS50!' to @{status.user.screen_name}...")
            try:
                api.update_status(status=f"This is CS50! @{status.user.screen_name}", in_reply_to_status_id=status.id)
                logger.info(f"Replied 'This is CS50!' to @{status.user.screen_name}.")
            except Exception as e:
                logger.info(f"{e} while replying 'This is CS50!'.")
                return recent_since_id 
        elif "hello" in status.text.lower():
            logger.info(f"Replying to @{status.user.screen_name}...")
            try:
                api.update_status(status=f"{replies[random_idx]} @{status.user.screen_name}", in_reply_to_status_id=status.id)
                logger.info(f"Replied {replies[random_idx]} to @{status.user.screen_name}.")
            except Exception as e:
                logger.error(f"{e} while replying.", exc_info=True)
                return recent_since_id 
    return recent_since_id

def get_latest_mention_id(api):
    for status in tweepy.Cursor(api.mentions_timeline).items(1):
        return status.id

def favorite_and_retweet_user_status(api, user):
    for status in api.user_timeline(screen_name=user, count=1):
        if not status.favorited:
            try:
                status.favorite()
                logger.info(f"@{user}'s latest status has been successfully liked.")
            except Exception as e:
                logger.error(f"{e} while attempting to favorite @{user}'s latest status.", exc_info=True)

        if not status.retweeted:
            try:
                status.retweet()
                logger.info(f"@{user}'s latest status has been successfully retweeted.")
            except Exception as e:
                logger.error(f"{e} while attempting to retweet @{user}'s latest status.", exc_info=True)

def main(keywords):
    api = create_api()
    myStreamListener = MyStreamListener(api)
    myStream = tweepy.Stream(api.auth, myStreamListener)

    logger.info("Connecting to Stream...")
    myStream.filter(track=keywords, languages=['en'], is_async=True)
    logger.info("Connected to Stream.")

    since_id = get_latest_mention_id(api) + 1
    while True:
        logger.info("Checking mentions...")
        since_id = reply_to_mentions(api, since_id)

        logger.info("Checking @davidjmalan's tweets...")
        favorite_and_retweet_user_status(api, "davidjmalan")

        logger.info("Checking @cs50's tweets...")
        favorite_and_retweet_user_status(api, "cs50")

        logger.info("Sleeping for 1 minute...")
        sleep(60)
    logging.info("main has returned.")

if __name__ == '__main__':
    try:
        main(['#CS50','#CS50x'])
    except Exception as e:
        logger.error(f"{e} on main.", exc_info=True)
