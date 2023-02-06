from flask_table import Table, Col


class Ftable(Table):
    no_items = 'هیچی'


class User(Ftable):
    username = Col('نام کاربری')
    fname = Col('نام')
    lname = Col('فامیل')
