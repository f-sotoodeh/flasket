from os import getenv


APP_TITLE = 'سایت آزمایشی'
APP_NAME = 'flasket'
SECRET_KEY = 'aaa'
LANGUAGE = 'farsi'

MONGO_URI = getenv('MONGO_URI', default=f'mongodb://127.0.0.1:27017/{APP_NAME}')
MONGODB_SETTINGS = dict(host=MONGO_URI)
