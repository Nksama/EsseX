import os
class Config(object):
    LOGGER = True
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN" , Nome)
    DB_URI = os.environ.get("DB" , None)
    LOG_CHANNEL = 0 # if you want a logging channel you can add this, else logs will go into Owner's PM

class Development(Config):
    TEST_DEVELOP = True
    LOGGER = True
