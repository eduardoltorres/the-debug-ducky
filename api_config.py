import tweepy
from logger_config import logger
from secrets import *

def create_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error(f"Error {e} creating API.", exc_info=True)
    logger.info("API successfully created.")

    return api
