from os import getenv


APP_TITLE = 'سایت آزمایشی'

# Avalable languages: farsi, arabic, english
LANGUAGE = 'farsi'


APP_NAME = 'flasket'
SECRET_KEY = 'zse4dcft67yhnmki90ol.90-[";l./'

MONGO_URI = getenv('MONGO_URI', default=f'mongodb://127.0.0.1:27017/{APP_NAME}')
MONGODB_SETTINGS = dict(host=MONGO_URI)
