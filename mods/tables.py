from flask_table import Table, Col


class Ftable(Table):
    no_items = 'هیچی'

    @classmethod
    def get_tr_attrs(cls, item):
        return dict(
            onclick = f"window.location='/panel/f/{cls.__name__.lower()}/{item.id}'",
        )


class User(Ftable):
    username = Col('نام کاربری')
    fname = Col('نام')
    lname = Col('فامیل')
