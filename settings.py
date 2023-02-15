from os import getenv


# Avalable languages: farsi, arabic, english
LANGUAGE = 'farsi'
TABLE_SIZE = 10
MENU = ['article', 'super_user']

APP_NAME = 'flasket'
APP_TITLE = dict(
    farsi = 'سایت آزمایشی',
    arabic = 'اختبار الموقع',
    english = 'Test website',
)[LANGUAGE]

SECRET_KEY = 'zse4dcft67yhnmki90ol.90-[";l./'

MONGO_URI = getenv('MONGO_URI', default=f'mongodb://127.0.0.1:27017/{APP_NAME}?authSource=admin')
MONGODB_SETTINGS = dict(host=MONGO_URI)
