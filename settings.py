from os import getenv


SITE_NAME = 'سایت آزمایشی'
SECRET_KEY = 'aaa'
MONGO_URI = getenv('MONGO_URI', default='mongodb://127.0.0.1:27017/flasket')
MONGODB_SETTINGS = dict(host=MONGO_URI)
